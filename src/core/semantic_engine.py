from sentence_transformers import SentenceTransformer, util
import torch

class SemanticBrain:
    def __init__(self):
        # Using a lightweight but powerful model for 12 LPA standards
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def calculate_similarity(self, resume_text: str, jd_text: str):
        # Convert text into numerical vectors (Embeddings)
        resume_embedding = self.model.encode(resume_text, convert_to_tensor=True)
        jd_embedding = self.model.encode(jd_text, convert_to_tensor=True)

        # Calculate 'Cosine Similarity' - how close the two vectors are in 3D space
        cosine_scores = util.cos_sim(resume_embedding, jd_embedding)
        return float(cosine_scores[0][0])