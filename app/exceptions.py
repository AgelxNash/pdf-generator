class PDFGenerationError(Exception):
    """Базовая ошибка генерации PDF"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class PDFTemplateNotFoundError(PDFGenerationError):
    """Шаблон PDF не найден."""


class PDFFontNotFoundError(PDFGenerationError):
    """Шрифт для PDF не найден."""


class PDFProcessingError(PDFGenerationError):
    """Ошибка обработки PDF (рисование, слияние, сохранение)."""


class PDFPermissionError(PDFGenerationError):
    """Ошибка прав доступа при генерации PDF."""


class PDFNotCreatedError(PDFGenerationError):
    """Итоговый файл PDF не создан."""
