from src.core.extractor_utils import ContactExtractor
from src.models.resume_schema import ResumeProfile

def build_profile(raw_text: str, name: str):
    # Initialize the new extractor
    contact_tool = ContactExtractor()
    contacts = contact_tool.extract_all(raw_text)
    
    # Map your data to the Pydantic model
    profile = ResumeProfile(
        name=name,
        email=contacts["email"],  # Will now find aswinhkk@gmail.com
        phone=contacts["phone"],  # Will now find your mobile number
        skills=[], # Use your SkillMapper here
        summary=f"Candidate with profiles: {contacts['github']} | {contacts['linkedin']}"
    )
    
    return profile