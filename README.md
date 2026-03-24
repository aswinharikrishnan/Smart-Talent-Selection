
# 🤖 Smart Talent Selection Engine

An AI-powered recruitment engine designed to process unstructured resume data, extract key entities, and perform semantic skill mapping using Transformer models.

## 🚀 Getting Started

### 1. Setup Environment

Ensure your execution policy allows for script running, then activate the virtual environment:

**PowerShell**

**PowerShell**

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

This project requires **Sentence-Transformers** for the AI Brain and **spaCy** for NLP utilities.

**PowerShell**

**PowerShell**

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Run the Batch Analysis

The engine automatically scans the `tests/fixtures/` folder for any PDF resumes and generates an AI analysis report.

**PowerShell**

**PowerShell**

```
python test_run.py
```

---

## 📅 Development Roadmap

### **Day 1: The Ingestion Pipeline**

* **PDF Extraction** : Implemented robust text extraction from unstructured PDF files.
* **Data Modeling** : Defined Pydantic schemas for Resumes, Experience, and Education to ensure data integrity.
* **Validation** : Successfully processed 6,000+ character engineering resumes.

### **Day 2: Semantic Intelligence & Batch Processing**

* **AI Brain** : Integrated `all-MiniLM-L6-v2` Sentence-Transformer for contextual skill matching.
* **Precision Extraction** : Built Regex utilities to identify Indian mobile numbers (`7559803806`) and professional emails.
* **Dynamic Batching** : Upgraded `test_run.py` to process multiple files in the `tests/fixtures/` directory automatically.
* **Semantic Scoring** : Moved beyond keyword counts to **Cosine Similarity** scores for Embedded Systems, VLSI, and ML.

---

## 📂 Project Structure

* `src/ingestion/parsers/`: Logic for PDF extraction.
* `src/core/`: The "Brain" (Semantic Engine, Skill Mapper, and Extractor Utils).
* `tests/fixtures/`: Storage for sample resumes (Drop any PDF here to test).
* `requirements.txt`: Environment inventory including **Torch** and  **Transformers** .
* `test_run.py`: The main entry point for batch AI processing.
