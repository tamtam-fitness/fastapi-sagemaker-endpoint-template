import logging
import os

from .config import read_yaml
from .logger import init_logger

env = os.environ["ENV"]
settings = read_yaml(f"{os.getcwd()}/src/common/yaml_configs/{env}.yaml")

# loggerの初期化
init_logger(settings.LOGGER_CONFIG_PATH)
logger = logging.getLogger(__name__)
