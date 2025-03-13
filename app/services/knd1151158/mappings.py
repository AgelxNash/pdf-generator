from typing import Dict, Tuple

FieldMapping = Dict[str, Tuple[float, float]]

MAPPINGS: Dict[str, FieldMapping] = {
    "first_page": {
        "org_inn": (558, 40),
        "org_kpp": (558, 102),
        "spravka_number": (244, 360),
        "korr_number": (1071, 360),
        "otchet_period": (1466, 360),
        "org_desc_first": (46, 482),
        "org_desc_second": (46, 545),
        "org_desc_third": (46, 608),
        "org_desc_four": (46, 671),
        "study_form": (678, 787),
        "taxpayer_lastname": (204, 903),
        "taxpayer_firstname": (204, 973),
        "taxpayer_surname": (204, 1045),
        "taxpayer_inn": (205, 1115),
        "taxpayer_date_birth": (1030, 1115),
        "taxpayer_month_birth": (1149, 1115),
        "taxpayer_year_birth": (1268, 1115),
        "taxpayer_document_code": (322, 1242),
        "taxpayer_document_serial_number": (835, 1242),
        "taxpayer_document_date_issue": (322, 1312),
        "taxpayer_document_month_issue": (440, 1312),
        "taxpayer_document_year_issue": (560, 1312),
        "taxpayer_is_student": (756, 1382),
        "summa_rashodov_before_dot": (756, 1462),
        "summa_rashodov_after_dot": (1307, 1462),
        "authenticity_first": (48, 1630),
        "authenticity_second": (48, 1692),
        "authenticity_third": (48, 1754),
        "signature_date": (456, 1868),
        "signature_month": (573, 1868),
        "signature_year": (694, 1868),
        "pages_count": (364, 1948)
    },
    "second_page": {
        "org_inn": (520, 40),
        "org_kpp": (520, 102),
        "student_lastname": (204, 293),
        "student_firstname": (204, 363),
        "student_surname": (204, 433),
        "student_inn": (204, 503),
        "student_date_birth": (1033, 503),
        "student_month_birth": (1150, 503),
        "student_year_birth": (1271, 503),
        "student_document_code": (323, 638),
        "student_document_serial_number": (836, 638),
        "student_document_date_issue": (321, 708),
        "student_document_month_issue": (437, 708),
        "student_document_year_issue": (559, 708)
    }
}