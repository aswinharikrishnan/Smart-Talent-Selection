
# 🤖 Smart Talent Selection Engine

An AI-powered recruitment engine designed to process unstructured resume data, extract key entities, and perform semantic skill mapping using Transformer models and Large Language Models (LLMs).

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

This project requires  **Sentence-Transformers** ,  **spaCy** ,  **OpenAI-SDK** , and  **python-dotenv** .

**PowerShell**

**PowerShell**

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory to store your API credentials. **Note:** This file is ignored by Git for security.

**Plaintext**

```
OPENROUTER_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

### 4. Run the Batch Analysis

The engine scans the `tests/fixtures/` folder for PDF resumes and generates a ranked AI analysis report.

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
* **Precision Extraction** : Built Regex utilities to identify Indian mobile numbers and professional emails.
* **Dynamic Batching** : Upgraded `test_run.py` to process multiple files in the `tests/fixtures/` directory automatically.
* **Semantic Scoring** : Moved beyond keyword counts to **Cosine Similarity** scores for ECE-specific fields like VLSI, DSP, and ML.

### **Day 3: LLM Integration & API Architecture**

* **Generative AI Layer** : Integrated LLMs (Gemini/Llama) to perform complex entity extraction (Name, CGPA, Email) with higher reasoning than traditional Regex.
* **Provider-Agnostic Design** : Re-engineered the `IntentExtractor` to support multiple backends (Google Gemini, DeepSeek, OpenRouter) using the OpenAI-compatible standard.
* **Security Layer** : Implemented `python-dotenv` to decouple sensitive API keys from the codebase.
* **Ranking Logic 2.0** : Enhanced the `Ranker` engine with weighted scoring (70% Skills / 30% CGPA) and automated hiring status tags (🚀 Must Hire, ✅ Strong Fit).

## 📂 Project Structure

* `src/ingestion/`: Logic for PDF extraction and text cleaning.
* `src/core/intent_extractor.py`: The LLM interface for intelligent metadata extraction.
* `src/core/rank_engine.py`: Weighted scoring logic and candidate categorization.
* `tests/fixtures/`: Storage for sample resumes (Drop any PDF here to test).
* `.env`: (Local only) Secure storage for API keys.
* `test_run.py`: The main entry point for batch AI processing.
