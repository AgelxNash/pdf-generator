# PDF Generator
![Ruff](https://github.com/AgelxNash/pdf-generator/actions/workflows/ruff.yml/badge.svg)
![Mypy](https://github.com/AgelxNash/pdf-generator/actions/workflows/mypy.yml/badge.svg)
![Docker Publish](https://github.com/AgelxNash/pdf-generator/actions/workflows/docker-build.yml/badge.svg)
[![Docker Pulls](https://img.shields.io/docker/pulls/agelnash/pdf-generator.svg)](https://hub.docker.com/r/agelnash/pdf-generator)


## Описание
Генерация PDF из шаблона

Не текущий момент доступна генерация справки по форме <a href="https://www.nalog.gov.ru/html/sites/www.new.nalog.ru/2023/about_fts/docs_fts/pril1_14112652.pdf">КНД 1151158</a>
об оплате образовательных услуг для представления в налоговый орган.

## Использование Docker

```bash
docker pull agelnash/pdf-generator:latest
docker run -p 8000:8000 agelnash/pdf-generator:latest
```

## Установка и запуск
```bash
pip install -r app/requirements.txt
uvicorn app.index:app --reload
```

## Пример Payload
```
{
  "first_page": {
    "org_inn": "1234567890",
    "org_kpp": "987654321",
    "spravka_number": "13776 120325",
    "korr_number": "001",
    "otchet_period": "2024",
    "org_desc_first": "ООО Ромашка",
    "org_desc_second": "ИНН 1234567890, КПП 987654321",
    "org_desc_third": "Россия, Москва, ул. Примерная, д. 1",
    "org_desc_four": "Тел.: +7 (495) 123-45-67",
    "study_form": "Очная",
    "taxpayer_lastname": "Иванов",
    "taxpayer_firstname": "Иван",
    "taxpayer_surname": "Иванович",
    "taxpayer_inn": "123456789012",
    "taxpayer_date_birth": "01",
    "taxpayer_month_birth": "01",
    "taxpayer_year_birth": "1990",
    "taxpayer_document_code": "21",
    "taxpayer_document_serial_number": "1234 567890",
    "taxpayer_document_date_issue": "15",
    "taxpayer_document_month_issue": "03",
    "taxpayer_document_year_issue": "2010",
    "taxpayer_is_student": "1",
    "summa_rashodov_before_dot": "15000",
    "summa_rashodov_after_dot": "00",
    "authenticity_first": "Достоверность подтверждаю",
    "authenticity_second": "Подпись налогоплательщика",
    "authenticity_third": "Дата подачи справки",
    "signature_date": "10",
    "signature_month": "03",
    "signature_year": "2025",
    "pages_count": "2"
  },
  "second_page": {
    "org_inn": "1234567890",
    "org_kpp": "987654321",
    "student_lastname": "Петров",
    "student_firstname": "Петр",
    "student_surname": "Петрович",
    "student_inn": "123456789012",
    "student_date_birth": "01",
    "student_month_birth": "01",
    "student_year_birth": "2000",
    "student_document_code": "21",
    "student_document_serial_number": "1234 567890",
    "student_document_date_issue": "15",
    "student_document_month_issue": "03",
    "student_document_year_issue": "2020"
  }
}

```