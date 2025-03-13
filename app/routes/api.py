from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from services.knd1151158.payload import Payload
from services.knd1151158.generator import generator
from dependencies import get_config
from configs.models import ProjectConfig
from exceptions import (
    PDFTemplateNotFoundError,
    PDFFontNotFoundError,
    PDFProcessingError,
    PDFPermissionError,
    PDFNotCreatedError
)
import os
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/v1/knd1151158", response_class=FileResponse)
def generate_pdf_endpoint(data: Payload, config: ProjectConfig = Depends(get_config)) -> FileResponse:
    try:
        combined_data = {**data.first_page.dict(), **(data.second_page.dict() if data.second_page else {})}

        final_pdf_path = generator(combined_data, config)

        if not os.path.exists(final_pdf_path):
            logger.error(f"Финальный PDF файл не найден: {final_pdf_path}")
            raise HTTPException(status_code=404, detail="Файл не найден.")

        return FileResponse(final_pdf_path, media_type='application/pdf', filename=os.path.basename(final_pdf_path))

    except PDFTemplateNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except PDFFontNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except PDFProcessingError as e:
        raise HTTPException(status_code=422, detail=e.message)
    except PDFPermissionError as e:
        raise HTTPException(status_code=403, detail=e.message)
    except PDFNotCreatedError as e:
        raise HTTPException(status_code=500, detail=e.message)
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Внутренняя ошибка сервера.")
