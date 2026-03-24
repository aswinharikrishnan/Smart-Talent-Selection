class AISkillMatcher:
    def __init__(self, brain: SemanticBrain):
        self.brain = brain
        self.categories = {
            "Embedded Systems": "Development of firmware, microcontrollers, ESP32, and hardware.",
            "VLSI Design": "Physical design, FPGA, Verilog, and Cadence tools.",
            "Machine Learning": "Neural networks, data science, and predictive modeling."
        }

    def get_ai_score(self, resume_text: str):

        print(f"DEBUG: AI is analyzing text starting with: {resume_text[:50]}")
        scores = {}
        for category, description in self.categories.items():
            # AI compares your resume text against the CONCEPT of the category
            score = self.brain.calculate_similarity(resume_text, description)
            scores[category] = round(score * 100, 2)
        return scores