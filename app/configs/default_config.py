import os

from configs.models import ProjectConfig, PathsConfig, PdfGeneratorConfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEFAULT_CONFIG = ProjectConfig(
    paths=PathsConfig(
        tmp_dir=os.path.join(BASE_DIR, "data", "tmp"),
        storage_dir=os.path.join(BASE_DIR, "data", "storage")
    ),
    knd_1151158=PdfGeneratorConfig(
        form_file=os.path.join(BASE_DIR, "resources", "pdf", "knd-1151158.pdf"),
        font_file=os.path.join(BASE_DIR, "resources", "fonts", "CourierNew.ttf")
    )
)
