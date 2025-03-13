from pydantic import BaseModel

class PathsConfig(BaseModel):
    tmp_dir: str
    storage_dir: str


class PdfGeneratorConfig(BaseModel):
    form_file: str
    font_file: str


class ProjectConfig(BaseModel):
    paths: PathsConfig
    knd_1151158: PdfGeneratorConfig
