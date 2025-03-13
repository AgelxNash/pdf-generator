from utils.config_loader import load_project_config
from configs.models import ProjectConfig

project_config: ProjectConfig = load_project_config()

def get_config() -> ProjectConfig:
    return project_config
