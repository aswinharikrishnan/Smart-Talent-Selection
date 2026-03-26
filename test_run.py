import sys
import os
from src.core.intent_extractor import IntentExtractor
from src.core.skill_mapper import AISkillMatcher
from src.core.semantic_engine import SemanticBrain
from src.core.rank_engine import Ranker
from src.ingestion.parsers.pdf_parser import extract_text_from_pdf

def main():
    print("🏆 Starting Smart Talent Selection (Day 3)...")
    
    # Initialize Engines
    ai_parser = IntentExtractor()
    brain = SemanticBrain()
    matcher = AISkillMatcher(brain)
    
    fixtures_path = "tests/fixtures"
    pdf_files = [f for f in os.listdir(fixtures_path) if f.endswith('.pdf')]
    leaderboard = []

    for filename in pdf_files:
        path = os.path.join(fixtures_path, filename)
        text = extract_text_from_pdf(path)
        
        # 1. Get Metadata via Gemini
        metadata = ai_parser.extract_metadata(text)
        
        # 2. Get Skill Scores via Sentence-Transformers
        skill_scores = matcher.get_ai_score(text)
        
        # 3. Calculate Final Rank
        final_score = Ranker.calculate_total_score(skill_scores, metadata['cgpa'])
        status = Ranker.get_status(final_score)
        
        leaderboard.append({
            "name": metadata['name'],
            "cgpa": metadata['cgpa'],
            "score": final_score,
            "status": status
        })

    # Display Leaderboard
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    print("\n" + "="*60)
    print(f"{'NAME':<20} | {'CGPA':<6} | {'SCORE':<8} | {'STATUS'}")
    print("-" * 60)
    for entry in leaderboard:
        print(f"{entry['name']:<20} | {entry['cgpa']:<6} | {entry['score']}% | {entry['status']}")
    print("="*60)

if __name__ == "__main__":
    main()