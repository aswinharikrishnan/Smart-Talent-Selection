
## 🚀 Getting Started

### 1. Setup Environment

Ensure your execution policy allows for script running, then activate the virtual environment:

**PowerShell**

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

This project requires  **Sentence-Transformers** ,  **Streamlit** ,  **Ollama** , and  **Plotly** .

**PowerShell**

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Local AI Engine (Day 4)

Install [Ollama](https://ollama.com/) and download the localized DeepSeek-R1 model:

**PowerShell**

```
ollama run deepseek-r1:1.5b
```

### 4. Launch the Dashboard

Run the Streamlit frontend to upload resumes and view real-time analytics:

**PowerShell**

```
streamlit run app.py
```

---

## 📅 Development Roadmap

### **Day 1-2: Foundation & Semantic Intelligence**

* **PDF Ingestion** : Robust text extraction and Pydantic data modeling.
* **AI Brain** : Integrated `all-MiniLM-L6-v2` for contextual skill matching.
* **Semantic Scoring** : Implemented **Cosine Similarity** for ECE-specific fields like VLSI and DSP.

### **Day 3: LLM Architecture & Security**

* **Generative Layer** : Integrated LLMs for complex entity extraction (Name, 9.05+ CGPA, Email).
* **Provider-Agnostic Design** : Support for Gemini, DeepSeek, and OpenRouter via a unified interface.
* **Security** : Implemented `python-dotenv` for secure credential management.

### **Day 4-7: Local AI & Professional Dashboard**

* **Edge AI Integration** : Migrated to **Local LLM (DeepSeek-R1 via Ollama)** to bypass cloud API rate limits and costs.
* **ECE Skill Taxonomy** : Deep mapping for core domains (Embedded Systems, FPGA, VLSI, and Signal Processing).
* **Streamlit UI/UX** : Built a professional HR dashboard with drag-and-drop resume uploading.
* **Talent Analytics** : Integrated **Plotly** visualizations, including competency radar charts and academic-vs-skill bar graphs.
* **Weighted Ranking 2.0** : Refined scoring logic with a 70/30 skill-to-academic ratio, featuring automated status tags (🚀 Must Hire, ✅ Strong Fit).

---

## 📂 Project Structure

* `app.py`: The main Streamlit web application and analytics dashboard.
* `src/core/intent_extractor.py`: Logic for local LLM metadata extraction.
* `src/core/rank_engine.py`: Weighted scoring and ECE taxonomy mapping.
* `tests/fixtures/`: Storage for sample resumes (Drop any PDF here to test).
* `test_run.py`: CLI entry point for batch processing.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **AI Models:** DeepSeek-R1 (Local), Sentence-Transformers, Llama 3.1
* **Frontend:** Streamlit, Plotly (Visualizations)
* **Infrastructure:** Ollama, OpenAI SDK, Pydantic
