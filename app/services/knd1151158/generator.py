from typing import Dict, Any, List
from PyPDF2 import PdfMerger
from pdf2image import convert_from_path
from PIL import ImageDraw, ImageFont, Image, UnidentifiedImageError
import os
import time
import logging
from configs.models import ProjectConfig
from services.knd1151158.formatter import Formatter
from services.knd1151158.mappings import MAPPINGS
from utils.file_utils import clean_text
from exceptions import (
    PDFTemplateNotFoundError,
    PDFFontNotFoundError,
    PDFProcessingError,
    PDFPermissionError,
    PDFNotCreatedError
)

logger = logging.getLogger(__name__)


def generator(data: Dict[str, Any], config: ProjectConfig) -> str:
    tmp_dir = config.paths.tmp_dir
    storage_dir = config.paths.storage_dir
    form_file = config.knd_1151158.form_file
    font_file = config.knd_1151158.font_file

    try:
        os.makedirs(tmp_dir, exist_ok=True)
        os.makedirs(storage_dir, exist_ok=True)
    except PermissionError:
        logger.exception("Нет прав на создание директорий.")
        raise PDFPermissionError("Нет прав на создание директорий.")

    try:
        images: List[Image.Image] = convert_from_path(form_file)
    except FileNotFoundError:
        logger.exception(f"Шаблон PDF не найден: {form_file}")
        raise PDFTemplateNotFoundError("Шаблон PDF не найден.")
    except (OSError, UnidentifiedImageError):
        logger.exception(f"Ошибка чтения шаблона PDF: {form_file}")
        raise PDFProcessingError("Ошибка чтения шаблона PDF.")

    try:
        font: ImageFont.FreeTypeFont = ImageFont.truetype(font_file, 44)
    except FileNotFoundError:
        logger.exception(f"Шрифт не найден: {font_file}")
        raise PDFFontNotFoundError("Шрифт для генерации PDF не найден.")
    except OSError:
        logger.exception(f"Ошибка загрузки шрифта: {font_file}")
        raise PDFProcessingError("Ошибка загрузки шрифта для PDF.")

    generated_files: List[str] = []

    try:
        taxpayer_is_student = int(data.get("taxpayer_is_student", 1))
        pages_count = 1 if taxpayer_is_student == 1 else 2

        for i, img in enumerate(images[:pages_count]):
            draw = ImageDraw.Draw(img)
            filler = Formatter(draw, font, data, MAPPINGS)

            if i == 0:
                filler.fill_page("first_page")
            elif i == 1:
                filler.fill_page("second_page")

            taxpayer_lastname = clean_text(data.get("taxpayer_lastname", ""))
            taxpayer_firstname = clean_text(data.get("taxpayer_firstname", ""))
            taxpayer_surname = clean_text(data.get("taxpayer_surname", ""))
            reference_id = clean_text(data.get("spravka_number", ""))

            output_filename = os.path.join(tmp_dir,
                                           f"{taxpayer_lastname}_{taxpayer_firstname}_{taxpayer_surname}_{i}.pdf")
            img.save(output_filename, "PDF")
            generated_files.append(output_filename)
    except Exception:
        logger.exception("Ошибка при формировании страниц PDF.")
        raise PDFProcessingError("Ошибка при генерации содержимого PDF.")

    date = time.strftime("%d.%m.%Y")
    final_filename = os.path.join(
        storage_dir,
        f"{reference_id}_{taxpayer_lastname}_{taxpayer_firstname}_{taxpayer_surname}_справка_КНД_1151158_{date}.pdf"
    )

    try:
        merger = PdfMerger()
        for file in generated_files:
            merger.append(file)
        merger.write(final_filename)
        merger.close()
    except Exception:
        logger.exception("Ошибка при объединении PDF.")
        raise PDFProcessingError("Ошибка при создании итогового PDF.")
    finally:
        for file in generated_files:
            try:
                os.remove(file)
            except OSError:
                logger.warning(f"Не удалось удалить временный файл: {file}")

    if not os.path.exists(final_filename):
        logger.error(f"Итоговый PDF не найден: {final_filename}")
        raise PDFNotCreatedError("Итоговый PDF не создан.")

    return final_filename
