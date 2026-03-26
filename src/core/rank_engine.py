class Ranker:
    @staticmethod
    def calculate_total_score(field_scores, cgpa):
        avg_skill = sum(field_scores.values()) / len(field_scores)
        academic_score = (float(cgpa) / 10.0) * 100
        return round((avg_skill * 0.7) + (academic_score * 0.3), 2)

    @staticmethod
    def get_status(score):
        """This function MUST be inside the Ranker class"""
        if score >= 85: return "🚀 Must Hire"
        if score >= 70: return "✅ Strong Fit"
        return "⏳ Keep in Pipeline"