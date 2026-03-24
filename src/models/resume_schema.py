from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional

class Experience(BaseModel):
    title: str
    company_or_org: str
    is_professional: bool = True
    description: Optional[str] = None

class ResumeProfile(BaseModel):
    name: str
    # Use str if you haven't installed 'email-validator' yet
    email: Optional[str] = None 
    phone: Optional[str] = None
    skills: List[str] = Field(default_factory=list)
    experience: List[Experience] = Field(default_factory=list)
    education: List[str] = Field(default_factory=list)
    summary: Optional[str] = None