import os
import sys

# Ensure the 'src' directory is in the python path for modular imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Updated imports matching the new industry-standard structure
from ingestion.parsers.pdf_parser import extract_text_from_pdf
from ingestion.parsers.docx_parser import extract_text_from_docx

def run_industry_test():
    """
    Validates Feature 1: Multi-Format Resume Ingestion.
    Tests PDF and DocX parsing from the new folder structure.
    """
    print(" Starting Smart Talent Engine Validation...")
    
    # Path to your test files
    fixtures_path = "tests/fixtures/"
    
    if not os.path.exists(fixtures_path):
        print(f" Error: {fixtures_path} not found.")
        return

    # Filter for supported formats as per Requirement 1.17
    files = [f for f in os.listdir(fixtures_path) if f.endswith(('.pdf', '.docx'))]

    if not files:
        print(" No test resumes found in tests/fixtures/")
        return

    for file_name in files:
        file_path = os.path.join(fixtures_path, file_name)
        print(f"\n Processing: {file_name}")
        
        try:
            if file_name.endswith('.pdf'):
                # Fulfills Requirement 1.18: Intelligent Parsing
                content = extract_text_from_pdf(file_path)
            else:
                # Fulfills Requirement 1.17: DocX Support
                content = extract_text_from_docx(file_path)
            
            print(f" Success: Extracted {len(content)} characters.")
            print(f" Preview: {content[:150]}...")
            
        except Exception as e:
            # Fulfills Requirement 1.19: Validation & Feedback
            print(f" Failed to process {file_name}: {str(e)}")

if __name__ == "__main__":
    run_industry_test()