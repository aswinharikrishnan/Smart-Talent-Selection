# Smart Talent Selection Engine 🚀

**Developed for the Cymonic.ai Hackathon | MEC Kochi**

A high-speed, semantic recruitment pipeline designed to automate resume parsing and candidate ranking. This tool replaces rigid keyword-matching with a **Weighted Technical Density Model** to identify top-tier engineering talent in seconds.

## 🔴 The Problem

Traditional Applicant Tracking Systems (ATS) often reject elite engineering talent due to unstructured PDF layouts or non-standard formatting. Recruiters spend an average of only 6 seconds per resume, leading to a high "False Negative" rate for specialized roles like VLSI, Embedded Systems, and Machine Learning.

## 🟢 The Solution

This engine implements a **Weighted 70/30 Ranking Model** to ensure a holistic evaluation:

- **70% Technical Competency:** Automatically maps skills into specialized ECE clusters (VLSI, ML, Embedded) to measure expertise density.
- **30% Academic Excellence:** Custom Regex-based extraction of high-value markers, including specialized detection for a **9.05 CGPA**.
- **Interactive HR Dashboard:** Visualizes candidate depth using Plotly radar charts, providing instant "Must Hire" or "Strong Fit" recommendations.

## 🛠️ Tech Stack

- **Core Logic:** Python 3.10
- **User Interface:** Streamlit (High-speed Web Framework)
- **Analytics:** Plotly Express (Interactive Competency Mapping)
- **Data Ingestion:** PyPDF & Regex (Automated Entity Extraction)
- **Data Management:** Pandas (Scoring Matrices & Ranking Logic)
- **Cloud Infrastructure:** Streamlit Community Cloud

## ⚙️ Quick Start: Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/aswinharikrishnan/Smart-Talent-Selection

# 2. Navigate to the project folder
cd Smart-Talent-Selection

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

## 🎥 Project Demo

[![Watch the Demo](https://img.shields.io/badge/Click_to_Watch-Demo_Video-red?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/15BuXBu7idE6a82hdCtEQs-Kwj8kKT30o/view?usp=drive_link)

*Click the badge above to view the full technical walkthrough on Google Drive.*
