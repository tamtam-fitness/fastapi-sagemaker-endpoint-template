# please delete module dir because of meaningless code
from src.common import logger


class TempClass:
    def add_temp(self, input_str: str) -> str:
        logger.info("temp")
        return input_str + "temp"
