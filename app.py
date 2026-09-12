import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(
    page_title="Exam Bread",
    page_icon="🍞",
    layout="wide"
)

# Title
st.title("🍞 EXAM BREAD")
st.subheader("Previous Year Question Paper Analyzer")

st.write(
    "Upload your previous-year question papers "
    "and discover high-frequency and weak topics."
)

st.divider()

# -------------------------------
# PDF UPLOAD
# -------------------------------

st.header("📄 Upload Previous Year Papers")

uploaded_files = st.file_uploader(
    "Upload up to 5 years of question papers",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(
        f"{len(uploaded_files)} paper(s) uploaded successfully!"
    )

    for file in uploaded_files:
        st.write("📄", file.name)

    if st.button("🔍 Analyze Papers"):
        st.success("Analysis completed!")


# -------------------------------
# TOPIC FREQUENCY
# -------------------------------

st.divider()

st.header("📊 Topic Frequency Analysis")

data = {
    "Topic": [
        "Linked List",
        "Trees",
        "Sorting",
        "Graphs",
        "Stack",
        "Queue"
    ],
    "Frequency": [
        12,
        10,
        8,
        6,
        5,
        3
    ]
}

df = pd.DataFrame(data)

st.dataframe(
    df,
    use_container_width=True
)

fig, ax = plt.subplots()

ax.bar(
    df["Topic"],
    df["Frequency"]
)

ax.set_xlabel("Topics")
ax.set_ylabel("Number of Questions")

ax.set_title(
    "Topic Frequency Across Previous Year Papers"
)

plt.xticks(rotation=30)

st.pyplot(fig)


# -------------------------------
# WEAK TOPICS
# -------------------------------

st.divider()

st.header("🎯 Tell Us Your Weak Topics")

topics = [
    "Linked List",
    "Trees",
    "Sorting",
    "Graphs",
    "Stack",
    "Queue"
]

weak_topics = st.multiselect(
    "Select the topics you find difficult:",
    topics
)

if weak_topics:
    st.write("Your weak topics:")

    for topic in weak_topics:
        st.write("⚠️", topic)


# -------------------------------
# 7-DAY STUDY PLAN
# -------------------------------

st.divider()

st.header("📅 Your 7-Day Study Plan")

plan = {
    "Day 1": "Linked List",
    "Day 2": "Trees",
    "Day 3": "Graphs",
    "Day 4": "Sorting",
    "Day 5": "Linked List Practice",
    "Day 6": "Trees + Graphs Practice",
    "Day 7": "Mock Test + Revision"
}

for day, topic in plan.items():

    st.write(
        f"**{day}:** {topic}"
    )