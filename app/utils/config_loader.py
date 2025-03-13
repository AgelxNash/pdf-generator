import os
import yaml
from configs.models import ProjectConfig
from configs.default_config import DEFAULT_CONFIG


def load_project_config() -> ProjectConfig:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, 'project_config.yaml')

    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            return ProjectConfig(**data)

    return DEFAULT_CONFIG
