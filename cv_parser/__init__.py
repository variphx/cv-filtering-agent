from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from google import genai

from ..cvs import CurriculumVitae

class CVParser:
    def __init__(self):
        self._prompt = ChatPromptTemplate([
            ("system", "You are a skillful headhunter who reads CVs and extracts relevant information of the candidate. Your task is to analyze the candidate's CV and extract their skills, experience, education, contact information and further information should they have been mentioned."),
            ("user", "Extract the information of the candidate in the following CV: {cv_file}")
        ])
        self._structured_llm = ChatGoogleGenerativeAI(model="models/gemini-flash-2.0").with_structured_output(CurriculumVitae)
        self._runtime = self._prompt | self._structured_llm

        self._client = genai.Client()


    def parse(self, path: str | Path):
        cv_file = self._client.files.upload(file=path)
        prompt = """
<|SYSYEM|>
You are a skillful headhunter who reads CVs and extracts relevant information of the candidate.
Your task is to analyze the candidate's CV and extract their skills, experience, education, contact information and further information should they have been mentioned.
<|SYSTEM|>
<|SPECIFICATION|>
Note that the date time format is DD/MM/YYYY in the CVs, and the date or month may be omitted. The dash (-) between dates indicates a range of time.
Examples:
    - 2018 - 2020 means start at 2018 and end at 2020.
    - 02/2025 means February 2025.
    - 10/2022 - 02/2023 means October 2022 to February 2023.
<|SPECIFICATION|>
Extract the information of the candidate in the following CV, be concise and precise.
"""
        response = self._client.models.generate_content(
            model="models/gemini-2.0-flash",
            contents=[prompt, cv_file],
            config={
                "response_mime_type": "application/json",
                "response_schema": CurriculumVitae,
            }
        )

        return response
