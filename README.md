## Getting Started

### 1. Setup Environment

Ensure your execution policy allows for script running, then activate the virtual environment:

**PowerShell**

```
.\venv\Scripts\activate
```

### 2. Install Dependencies

**PowerShell**

```
pip install -r requirements.txt
```

### 3. Run Validation Test

To verify the **Intelligent Parsing** results (expecting >6,000 chars for standard engineering resumes):

**PowerShell**

```
python test_run.py
```

---

## 📂 Project Structure

* `src/ingestion/parsers/`: Logic for PDF and DocX extraction.
* `tests/fixtures/`: Sample resumes used for engine validation.
* `requirements.txt`: Environment inventory.
