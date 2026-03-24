import sys
import os

# Ensure the 'src' directory is in the path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from core.semantic_engine import SemanticBrain
from core.skill_mapper import AISkillMatcher
from ingestion.parsers.pdf_parser import extract_text_from_pdf

def process_all_resumes():
    # 1. Initialize the AI Brain once (Saves memory on your Acer Aspire 3)
    print("🧠 Initializing Semantic Engine...")
    brain = SemanticBrain()
    matcher = AISkillMatcher(brain)
    
    # 2. Define the folder where you drop your PDFs
    fixtures_dir = os.path.join("tests", "fixtures")
    
    if not os.path.exists(fixtures_dir):
        print(f"❌ Error: Folder '{fixtures_dir}' not found!")
        return

    # 3. Get a list of all PDF files in that folder
    pdf_files = [f for f in os.listdir(fixtures_dir) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("⚠️ No PDF files found in tests/fixtures/. Add some files!")
        return

    print(f"🚀 Found {len(pdf_files)} resumes. Starting Batch AI Analysis...\n")

    # 4. Loop through every PDF and generate unique scores
    for filename in pdf_files:
        file_path = os.path.join(fixtures_dir, filename)
        print(f"--- 📄 Processing: {filename} ---")
        
        try:
            # Extract the actual text for THIS specific file
            resume_text = extract_text_from_pdf(file_path)
            
            # Run AI Semantic Analysis
            ai_scores = matcher.get_ai_score(resume_text)
            
            # Display Results
            for category, score in ai_scores.items():
                print(f"  - {category}: {score}%")
            print("\n")
            
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    process_all_resumes()