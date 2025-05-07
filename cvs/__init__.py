from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Location(BaseModel):
    """Represents a geographical location."""

    city: Optional[str] = Field(None, description="City name")
    country: Optional[str] = Field(None, description="Country name")

    class Config:
        title = "Location"
        description = "Represents a geographical location."


class SocialMediaProfiles(BaseModel):
    """Links to social media profiles."""

    github: Optional[str] = Field(None, description="GitHub profile URL")
    behance: Optional[str] = Field(None, description="Behance profile URL")
    other: List[str] = Field(
        default_factory=list, description="Other social media links"
    )

    class Config:
        title = "Social Media Profiles"
        description = "Links to various social media profiles."


class ContactInformation(BaseModel):
    """Contact and professional information."""

    full_name: str = Field(..., description="Full name")
    job_title: Optional[str] = Field(None, description="Current job title")
    phone_number: Optional[str] = Field(None, description="Phone number")
    email_address: str = Field(..., description="Email address")
    location: Location = Field(..., description="Current location")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL")
    professional_website: Optional[str] = Field(
        None, description="Professional website URL"
    )
    social_media_profiles: SocialMediaProfiles = Field(
        ..., description="Social media links"
    )

    class Config:
        title = "Contact Information"
        description = "Contact and professional information."


class WorkExperience(BaseModel):
    """Work experience history."""

    job_title: Optional[str] = Field(None, description="Title of the job position")
    company_name: Optional[str] = Field(None, description="Company name")
    location: Location = Field(..., description="Location of the company")
    start_date: Optional[datetime] = Field(None, description="Start date of employment")
    end_date: Optional[datetime] = Field(None, description="End date of employment")
    responsibilities_and_achievements: List[str] = Field(
        default_factory=list, description="Tasks and accomplishments"
    )

    class Config:
        title = "Work Experience"
        description = "Work experience history and job details."


class Education(BaseModel):
    """Educational background."""

    degree: Optional[str] = Field(None, description="Degree earned")
    major: Optional[str] = Field(None, description="Major or field of study")
    institution_name: Optional[str] = Field(
        None, description="Name of the educational institution"
    )
    location: Location = Field(..., description="Institution location")
    enrollment_date: Optional[datetime] = Field(None, description="Enrollment date")
    graduation_date: Optional[datetime] = Field(None, description="Graduation date")
    honors_or_awards: List[str] = Field(
        default_factory=list, description="Academic honors or awards"
    )
    relevant_coursework: List[str] = Field(
        default_factory=list, description="Relevant coursework completed"
    )

    class Config:
        title = "Education"
        description = "Educational background details."


class LanguageSkill(BaseModel):
    """Language proficiency."""

    language: str = Field(..., description="Language name")
    proficiency: Optional[str] = Field(None, description="Proficiency level")

    class Config:
        title = "Language Skill"
        description = "Language spoken and proficiency."


class Skills(BaseModel):
    """Technical and soft skills."""

    technical: List[str] = Field(
        default_factory=list, description="Technical skills list"
    )
    soft: List[str] = Field(default_factory=list, description="Soft skills list")
    languages: List[LanguageSkill] = Field(
        default_factory=list, description="Languages spoken"
    )

    class Config:
        title = "Skills"
        description = "Technical, soft skills, and language proficiencies."


class Certification(BaseModel):
    """Certifications or licenses earned."""

    name: Optional[str] = Field(None, description="Certification name")
    issuing_organization: Optional[str] = Field(
        None, description="Issuing organization"
    )
    date_obtained: Optional[datetime] = Field(
        None, description="Date certification was obtained"
    )

    class Config:
        title = "Certification"
        description = "Professional certifications or licenses earned."


class ProfessionalAssociation(BaseModel):
    """Professional memberships."""

    organization: Optional[str] = Field(None, description="Association name")
    role: Optional[str] = Field(None, description="Role within the association")
    membership_start_date: Optional[datetime] = Field(
        None, description="Membership start date"
    )
    membership_end_date: Optional[datetime] = Field(
        None, description="Membership end date"
    )

    class Config:
        title = "Professional Association"
        description = "Professional organization memberships."


class Publication(BaseModel):
    """Published work."""

    title: Optional[str] = Field(None, description="Title of the publication")
    publication_name: Optional[str] = Field(
        None, description="Name of the publication source"
    )
    publication_date: Optional[datetime] = Field(None, description="Publication date")

    class Config:
        title = "Publication"
        description = "Publications authored."


class Award(BaseModel):
    """Awards and honors received."""

    name: Optional[str] = Field(None, description="Award name")
    issuing_organization: Optional[str] = Field(
        None, description="Awarding organization"
    )
    date_received: Optional[datetime] = Field(
        None, description="Date award was received"
    )

    class Config:
        title = "Award"
        description = "Awards and honors received."


class Project(BaseModel):
    """Personal or professional projects."""

    title: Optional[str] = Field(None, description="Project title")
    description: Optional[str] = Field(None, description="Brief project description")
    technologies_used: List[str] = Field(
        default_factory=list, description="Technologies used"
    )
    outcomes_or_achievements: List[str] = Field(
        default_factory=list, description="Project results or accomplishments"
    )

    class Config:
        title = "Project"
        description = "Details of personal or professional projects."


class VolunteerExperience(BaseModel):
    """Volunteer work experience."""

    organization_name: Optional[str] = Field(
        None, description="Volunteer organization name"
    )
    role: Optional[str] = Field(None, description="Role or position")
    start_date: Optional[datetime] = Field(
        None, description="Start date of volunteer work"
    )
    end_date: Optional[datetime] = Field(None, description="End date of volunteer work")
    key_contributions: List[str] = Field(
        default_factory=list, description="Key contributions during volunteering"
    )

    class Config:
        title = "Volunteer Experience"
        description = "Volunteer activities and contributions."


class ReferenceContactInformation(BaseModel):
    """Contact information for a reference."""

    phone_number: Optional[str] = Field(None, description="Reference's phone number")
    email_address: Optional[str] = Field(None, description="Reference's email address")

    class Config:
        title = "Reference Contact Information"
        description = "Contact details of a reference."


class Reference(BaseModel):
    """Reference details."""

    name: Optional[str] = Field(None, description="Reference name")
    relationship: Optional[str] = Field(None, description="Relationship to reference")
    company: Optional[str] = Field(
        None, description="Company where the reference works"
    )
    contact_information: ReferenceContactInformation = Field(
        ..., description="Reference's contact information"
    )

    class Config:
        title = "Reference"
        description = "Reference details for job applications."


class CurriculumVitae(BaseModel):
    """Complete CV structure."""

    contact_information: ContactInformation = Field(
        ..., description="Contact and basic professional details"
    )
    personal_statement: Optional[str] = Field(
        None, description="Brief personal summary or career goal"
    )
    work_experience: List[WorkExperience] = Field(
        default_factory=list, description="List of work experiences"
    )
    education: List[Education] = Field(
        default_factory=list, description="Educational background"
    )
    skills: Skills = Field(default_factory=Skills, description="Skills summary")
    certifications_and_licenses: List[Certification] = Field(
        default_factory=list, description="Certifications and licenses"
    )
    professional_associations: List[ProfessionalAssociation] = Field(
        default_factory=list, description="Professional association memberships"
    )
    publications: List[Publication] = Field(
        default_factory=list, description="Publications authored"
    )
    awards_and_honors: List[Award] = Field(
        default_factory=list, description="Awards and honors"
    )
    projects: List[Project] = Field(
        default_factory=list, description="Personal or professional projects"
    )
    volunteer_experience: List[VolunteerExperience] = Field(
        default_factory=list, description="Volunteer experience"
    )
    hobbies_and_interests: List[str] = Field(
        default_factory=list, description="Hobbies and personal interests"
    )
    references: List[Reference] = Field(
        default_factory=list, description="Professional references"
    )

    class Config:
        title = "Curriculum Vitae"
        description = "Complete structure for a CV/resume."
