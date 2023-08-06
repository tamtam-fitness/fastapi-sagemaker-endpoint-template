import logging
import os

from .config import read_yaml
from .logger import init_logger

env = os.environ["ENV"]
base_dir = os.environ["BASE_DIR"]

settings = read_yaml(os.path.join(base_dir, f"program/common/yaml_configs/{env}.yaml"))

# loggerの初期化
init_logger(
    os.path.join(settings.BASE_DIR, "program/common/logger/logging_config.yaml")
)
app_logger = logging.getLogger(__name__)
