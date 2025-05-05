from pydantic import BaseModel
from typing import List


class BackgroundCV(BaseModel):
    positions_want_to_employ: List[str]
    degree: List[str]
    at_least_experience: int
    foreign_languages: List[str]


class MustHave(BaseModel):
    job_related_skills: List[str]
    something_else: List[str]


class FullForm(BaseModel):
    background_cv: BackgroundCV
    must_have: MustHave
    nice_to_have: List[str]


class Form:
    def __init__(self):
        self.placeholder_dict = {
            List[str]: ["...", "..."],
            str: "...",
            int: 0,
        }

    def create_json(self) -> str:
        backgroundcv = BackgroundCV(
            positions_want_to_employ=self.placeholder_dict[List[str]],
            degree=self.placeholder_dict[List[str]],
            at_least_experience=self.placeholder_dict[int],
            foreign_languages=self.placeholder_dict[List[str]]
        )
        musthave = MustHave(
            job_related_skills=self.placeholder_dict[List[str]],
            something_else=self.placeholder_dict[List[str]]
        )
        fullform = FullForm(
            background_cv=backgroundcv,
            must_have=musthave,
            nice_to_have=self.placeholder_dict[List[str]]
        )

        return fullform.model_dump_json()
