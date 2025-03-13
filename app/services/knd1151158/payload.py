from pydantic import BaseModel, model_validator
from typing import Optional, Self


class FirstPage(BaseModel):
    org_inn: str
    org_kpp: str
    spravka_number: str
    korr_number: str
    otchet_period: str
    org_desc_first: str
    org_desc_second: str
    org_desc_third: str
    org_desc_four: str
    study_form: str
    taxpayer_lastname: str
    taxpayer_firstname: str
    taxpayer_surname: str
    taxpayer_inn: str
    taxpayer_date_birth: str
    taxpayer_month_birth: str
    taxpayer_year_birth: str
    taxpayer_document_code: str
    taxpayer_document_serial_number: str
    taxpayer_document_date_issue: str
    taxpayer_document_month_issue: str
    taxpayer_document_year_issue: str
    taxpayer_is_student: str
    summa_rashodov_before_dot: str
    summa_rashodov_after_dot: str
    authenticity_first: str
    authenticity_second: str
    authenticity_third: str
    signature_date: str
    signature_month: str
    signature_year: str
    pages_count: str


class SecondPage(BaseModel):
    org_inn: Optional[str] = None
    org_kpp: Optional[str] = None
    student_lastname: Optional[str] = None
    student_firstname: Optional[str] = None
    student_surname: Optional[str] = None
    student_inn: Optional[str] = None
    student_date_birth: Optional[str] = None
    student_month_birth: Optional[str] = None
    student_year_birth: Optional[str] = None
    student_document_code: Optional[str] = None
    student_document_serial_number: Optional[str] = None
    student_document_date_issue: Optional[str] = None
    student_document_month_issue: Optional[str] = None
    student_document_year_issue: Optional[str] = None

    @model_validator(mode="after")
    def check_all_or_none(self: Self) -> Self:
        values = self.dict()
        filled = [v for v in values.values() if v not in (None, "")]
        if 0 < len(filled) < len(values):
            missing = [k for k, v in values.items() if v in (None, "")]
            raise ValueError(
                f"Если указано одно поле из второй страницы, "
                f"то должны быть заполнены все: {', '.join(missing)}"
            )
        return self


class Payload(BaseModel):
    first_page: FirstPage
    second_page: Optional[SecondPage] = None
