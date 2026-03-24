import re
from typing import Dict, Optional

class ContactExtractor:
    def __init__(self):
        self.patterns = {
            "email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            "linkedin": r'linkedin\.com/in/[a-zA-Z0-9_-]+',
            "github": r'github\.com/[a-zA-Z0-9_-]+'
        }

    def extract_all(self, text: str) -> Dict[str, Optional[str]]:
        results = {}
        
        # 1. Standard Extraction
        for key, pattern in self.patterns.items():
            match = re.search(pattern, text)
            results[key] = match.group(0) if match else None

        # 2. Precision Phone Extraction
        # Step A: Remove common prefixes and non-digits
        # This turns "+91 7559803806" into "7559803806"
        clean_text = text.replace("+91", "").replace(" ", "").replace("-", "")
        
        # Step B: Find all 10-digit numbers starting with 6-9
        all_numbers = re.findall(r'[6-9]\d{9}', clean_text)
        
        # Step C: Filter out the '9876543210' placeholder
        real_numbers = [n for n in all_numbers if "9876543210" not in n]
        
        # Assign your real number (7559803806)
        results["phone"] = real_numbers[0] if real_numbers else None
        
        return results