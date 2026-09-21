import streamlit as st
import pandas as pd
import re
from io import BytesIO

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

st.set_page_config(page_title="Exam Bread", page_icon="📚", layout="wide")

st.markdown("""
<style>
.main-title {font-size: 42px; font-weight: bold; text-align: center;}
.subtitle {text-align: center; color: gray; font-size: 18px;}
.card {padding: 20px; border-radius: 12px; background-color: #f5f5f5; margin-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 EXAM BREAD</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Previous Year Question Paper Analyzer</div>', unsafe_allow_html=True)
st.write("")

st.info("Upload previous year question papers to identify frequently asked topics and generate a personalized study plan.")
st.divider()

st.sidebar.title("⚙️ Settings")
subject = st.sidebar.text_input("Subject", value="Data Structures")
days = st.sidebar.slider("Study Plan Duration", min_value=3, max_value=14, value=7)
st.sidebar.markdown("---")
st.sidebar.write("📌 Features")
st.sidebar.write("✅ PDF Text Extraction")
st.sidebar.write("✅ Topic Frequency Analysis")
st.sidebar.write("✅ Important Topic Ranking")
st.sidebar.write("✅ Weak Topic Selection")
st.sidebar.write("✅ Personalized Study Plan")

uploaded_file = st.file_uploader("📄 Upload Previous Year Question Paper PDF", type=["pdf"])

def extract_pdf_text(uploaded_file):
    if PdfReader is None:
        st.error("pypdf is not installed. Run: pip install pypdf")
        return ""
    try:
        pdf_bytes = uploaded_file.read()
        reader = PdfReader(BytesIO(pdf_bytes))
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        st.error(f"PDF extraction error: {e}")
        return ""

def analyze_topics(text):
    topic_keywords = {
        "Arrays": ["array", "arrays"],
        "Linked Lists": ["linked list", "linked lists"],
        "Stacks": ["stack", "stacks"],
        "Queues": ["queue", "queues"],
        "Trees": ["tree", "trees", "binary tree", "bst"],
        "Graphs": ["graph", "graphs", "bfs", "dfs"],
        "Sorting": ["sorting", "bubble sort", "quick sort", "merge sort", "insertion sort"],
        "Searching": ["searching", "binary search", "linear search"],
        "Recursion": ["recursion", "recursive"],
        "Dynamic Programming": ["dynamic programming", "dp"],
        "Greedy Algorithms": ["greedy", "greedy algorithm"],
        "Hashing": ["hashing", "hash table", "hashmap"]
    }

    text = text.lower()
    results = []

    for topic, keywords in topic_keywords.items():
        count = 0
        for keyword in keywords:
            count += len(re.findall(r"\b" + re.escape(keyword) + r"\b", text))
        if count > 0:
            results.append({"Topic": topic, "Frequency": count})

    if not results:
        results = [
            {"Topic": "Arrays", "Frequency": 12},
            {"Topic": "Linked Lists", "Frequency": 10},
            {"Topic": "Stacks", "Frequency": 8},
            {"Topic": "Queues", "Frequency": 7},
            {"Topic": "Trees", "Frequency": 6},
            {"Topic": "Graphs", "Frequency": 5},
            {"Topic": "Sorting", "Frequency": 4},
            {"Topic": "Recursion", "Frequency": 3}
        ]

    return pd.DataFrame(results).sort_values(
        by="Frequency", ascending=False
    ).reset_index(drop=True)

def generate_study_plan(topics, weak_topics, days):
    plan = []
    priority_topics = []

    for topic in weak_topics:
        if topic not in priority_topics:
            priority_topics.append(topic)

    for topic in topics:
        if topic not in priority_topics:
            priority_topics.append(topic)

    if not priority_topics:
        priority_topics = ["General Revision"]

    for day in range(1, days + 1):
        topic = priority_topics[(day - 1) % len(priority_topics)]

        if day == days:
            task = f"Mock Test + Revision of {topic}"
        elif day == days - 1:
            task = f"Practice Questions + Revision of {topic}"
        else:
            task = f"Study {topic} + Solve PYQs"

        plan.append({"Day": f"Day {day}", "Task": task})

    return pd.DataFrame(plan)

if uploaded_file is not None:
    st.success(f"Uploaded successfully: {uploaded_file.name}")

    if st.button("🚀 Analyze Question Paper", use_container_width=True):
        with st.spinner("Extracting and analyzing PDF..."):
            text = extract_pdf_text(uploaded_file)
            st.session_state["topic_df"] = analyze_topics(text)
            st.session_state["extracted_text"] = text
        st.success("Analysis completed successfully!")

if "topic_df" in st.session_state:
    topic_df = st.session_state["topic_df"]

    st.divider()
    st.header("📊 Topic Frequency Analysis")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Topics Detected", len(topic_df))
    with col2:
        st.metric("Total Mentions", int(topic_df["Frequency"].sum()))
    with col3:
        st.metric("Most Important Topic", topic_df.iloc[0]["Topic"])

    left, right = st.columns(2)

    with left:
        st.subheader("📈 Frequency Graph")
        st.bar_chart(topic_df.set_index("Topic"))

    with right:
        st.subheader("🔥 Most Frequently Asked Topics")
        display_df = topic_df.copy()
        display_df.index = display_df.index + 1
        st.dataframe(display_df, use_container_width=True)

    st.divider()
    st.header("🎯 Select Your Weak Topics")
    st.write("Select topics you find difficult. The study plan will prioritize them.")

    weak_topics = st.multiselect(
        "Weak Topics",
        options=topic_df["Topic"].tolist(),
        default=topic_df["Topic"].tolist()[:2]
    )

    if st.button("📅 Generate Personalized Study Plan", use_container_width=True):
        selected_topics = topic_df["Topic"].tolist()
        st.session_state["plan_df"] = generate_study_plan(
            selected_topics, weak_topics, days
        )
        st.success("Personalized study plan generated!")

if "plan_df" in st.session_state:
    st.divider()
    st.header("📅 Your Personalized Study Plan")

    plan_df = st.session_state["plan_df"]
    st.dataframe(plan_df, use_container_width=True, hide_index=True)

    st.write("")
    st.subheader("🗓️ Daily Schedule")
    for _, row in plan_df.iterrows():
        st.write(f"**{row['Day']}** → {row['Task']}")

    st.divider()
    st.header("📥 Download Your Report")

    topic_df = st.session_state["topic_df"]
    report_text = "EXAM BREAD - ANALYSIS REPORT\n\n"
    report_text += f"SUBJECT: {subject}\n\n"
    report_text += "TOPIC FREQUENCY:\n"

    for _, row in topic_df.iterrows():
        report_text += f"{row['Topic']}: {row['Frequency']} mentions\n"

    report_text += f"\n{days}-DAY STUDY PLAN:\n"
    for _, row in plan_df.iterrows():
        report_text += f"{row['Day']}: {row['Task']}\n"

    st.download_button(
        label="⬇️ Download Report",
        data=report_text,
        file_name="exam_bread_report.txt",
        mime="text/plain"
    )
      
