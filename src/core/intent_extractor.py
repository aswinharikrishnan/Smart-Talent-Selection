import re

class IntentExtractor:
    def __init__(self):
        self.professional_keywords = ["internship", "trainee", "engineer", "specialist"]
        self.academic_keywords = ["project", "mini-project", "coursework", "seminar"]

    def categorize_experience(self, title: str, description: str) -> bool:
        """Returns True if professional, False if academic."""
        combined_text = f"{title} {description}".lower()
        
        # Simple heuristic: If 'project' appears more than 'intern', it's likely academic
        if any(word in combined_text for word in self.academic_keywords):
            return False
        return True