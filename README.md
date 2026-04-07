# MEC Smart Talent Selection Engine 🚀

A high-speed, semantic recruitment pipeline designed to automate resume parsing and candidate ranking for engineering roles. Built for the **Cymonic.ai Hackathon**.

## 🔴 The Problem

Traditional Applicant Tracking Systems (ATS) rely on rigid keyword matching, often rejecting elite engineering talent due to unstructured PDF layouts or non-standard formatting. Recruiters spend an average of only 6 seconds per resume, leading to a high "False Negative" rate for specialized roles like VLSI and Embedded Systems.

## 🟢 The Solution

This engine replaces keyword-counting with a **Weighted Semantic Ranking Model**:

- **70/30 Scoring:** Prioritizes Technical Competency (70%) over Academic Excellence (30%) to find "Must Hire" talent.
- **Entity Extraction:** Custom Regex-based parser to reliably identify high-value markers .
- **Skill Clustering:** Automatically maps skills into specialized ECE domains (VLSI, ML, Embedded) for density analysis.

## 🛠️ Tech Stack

- **Language:** Python 3.10
- **UI Framework:** Streamlit
- **Data Visualization:** Plotly
- **Data Processing:** Pandas, PyPDF, Regex
- **Deployment:** Streamlit Community Cloud

## ⚙️ Setup Instructions

Follow these steps to run the HR Dashboard locally:

```bash
# 1. Clone the repository
git clone https://github.com/aswinhkk/Smart-Talent-Selection-Engine

# 2. Navigate to the project folder
cd Smart-Talent-Selection-Engine

# 3. Create and activate a virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
# source venv/bin/activate

# 4. Install all dependencies
pip install streamlit==1.31.0 pypdf==4.0.1 plotly==5.18.0 pandas==2.2.0 python-dotenv==1.0.1

# 5. Launch the application
streamlit run app.py
```
