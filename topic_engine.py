import re
import json
from pdf_proccessor import extract_text_from_pdf

topics = {
    "Linked List": ["linked list", "node", "insertion", "deletion"],
    "Stack": ["stack", "push", "pop", "parentheses"],
    "Queue": ["queue", "enqueue", "dequeue"],
    "Trees": ["tree", "binary tree", "bst", "traversal"],
    "Graphs": ["graph", "bfs", "dfs", "dijkstra"],
    "Sorting": ["sorting", "bubble sort", "merge sort", "quick sort"],
    "Searching": ["binary search", "linear search"],
}

def extract_questions(text):
    pattern = r'(?:\n|^)\s*(?:Q?\.?\d+[\.\)])\s*'
    parts = re.split(pattern, text)
    questions = [p.strip().replace("\n", " ") for p in parts if p.strip()]
    return questions

def match_topics(questions):
    counts = {topic: 0 for topic in topics}
    for q in questions:
        q_lower = q.lower()
        for topic, keywords in topics.items():
            if any(kw in q_lower for kw in keywords):
                counts[topic] += 1
    return counts

def analyze(text):
    questions = extract_questions(text)
    counts = match_topics(questions)
    result = {k: v for k, v in counts.items() if v > 0}
    return result

def generate_7day_plan(counts):
    sorted_topics = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    days = [f"Day {i+1}" for i in range(7)]
    plan = {}
    for i, day in enumerate(days):
        if i < len(sorted_topics):
            topic, freq = sorted_topics[i]
            plan[day] = f"{topic} (appeared {freq}x in PYQs)"
        else:
            plan[day] = "Revision + mock test"
    return plan

if __name__ == "__main__":
    with open("sample.pdf", "rb") as file:
        text = extract_text_from_pdf(file)
    result = analyze(text)
    plan = generate_7day_plan(result)
    output = {"topic_frequency": result, "seven_day_plan": plan}
    with open("output.json", "w") as f:
        json.dump(output, f, indent=2)
    print(json.dumps(output, indent=2))