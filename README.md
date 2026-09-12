# Exam-Bread
# 🍞 Exam Bread

## 📌 Project Overview

Exam Bread is an intelligent exam preparation assistant that analyzes previous-year question papers and identifies frequently repeated topics. It helps students understand important exam trends and generates a structured 7-day study plan based on topic frequency and weak areas.

The goal of the project is to help students prepare efficiently by focusing on high-priority and frequently asked topics.

## 🎯 Problem Statement

Students often spend a lot of time manually checking previous-year question papers to identify repeated questions and important topics. This process is time-consuming and may cause students to miss high-priority topics.

Exam Bread automates this analysis and provides useful insights in a simple and interactive interface.

## ✨ Features

* Upload or provide previous-year question paper data
* Extract and organize questions from the input
* Identify frequently occurring topics
* Analyze topic-wise repetition
* Display frequency charts and statistics
* Highlight important topics for preparation
* Generate a 7-day study plan
* Simple and interactive Streamlit interface

## 🏗️ Project Workflow

```text
Question Papers
      ↓
Data Extraction
      ↓
Question and Topic Processing
      ↓
Frequency Analysis
      ↓
Topic-wise Visualization
      ↓
Priority Identification
      ↓
7-Day Study Plan
```

## 🧰 Technologies Used

* Python
* Streamlit
* Pandas
* Matplotlib
* Natural Language Processing / Keyword-Based Topic Analysis
* GitHub

## 👥 Team Contributions

### 👤 Person 1 – Frontend & Streamlit Development

* Designed and developed the Streamlit web application
* Created the main user interface and page layout
* Added the project title, description, upload section, and interactive elements
* Integrated different components into one working interface
* Tested the application locally
* Fixed UI-related issues

### 👤 Person 2 – Data Processing & Question Paper Analysis

* Processed uploaded question paper data
* Developed logic for extracting and organizing questions
* Implemented analysis to identify frequently occurring topics and questions
* Prepared data for charts, statistics, and topic-wise analysis
* Tested the analysis using sample question papers
* Verified the correctness of the results

### 👤 Person 3 – Visualization, Testing & Documentation

* Developed graphs and visualizations
* Added charts to display frequently occurring topics
* Tested the application using different inputs
* Identified and fixed errors
* Prepared and maintained the README documentation
* Added project explanation, setup instructions, and screenshots

## 🤝 Team Collaboration

All three team members contributed to the development, testing, debugging, and improvement of the project.

The work was divided into frontend development, data processing, visualization, testing, and documentation to create a functional and user-friendly exam preparation application.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/exam-bread.git
cd exam-bread
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

For macOS/Linux:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in the browser.

## 📂 Project Structure

```text
exam-bread/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_data/
│   └── sample_questions.txt
│
└── screenshots/
    └── app_screenshot.png
```

## 📊 Expected Output

The application provides:

* List of frequently occurring topics
* Topic-wise frequency count
* Graphical representation of important topics
* Priority-based topic analysis
* A 7-day preparation schedule

## 🔮 Future Improvements

* Better PDF text extraction
* Advanced NLP-based topic modeling
* Automatic detection of weak topics using quiz performance
* Support for multiple subjects
* AI-generated explanations for important topics
* Personalized study plans
* Export study plan as PDF
* Cloud deployment
* Improved question similarity detection

## ⚠️ Current Limitations

* Topic identification may depend on keywords in the question papers
* Scanned PDFs may require OCR support
* Weak-topic detection may require student input or performance data
* The current version focuses on a basic working prototype

## 🏁 Conclusion

Exam Bread simplifies exam preparation by analyzing previous-year question papers, identifying repeated topics, visualizing exam trends, and generating a focused 7-day study plan. It helps students save time and prioritize their preparation more effectively.

## 📜 License

This project is developed for educational and hackathon purposes.


