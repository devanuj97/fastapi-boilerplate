from services.logger.base_logger import BaseLogger
from services.logger.types import LogLevel


class ConsoleLogger(BaseLogger):
    def critical(self, message: str) -> None:
        print(f"{LogLevel.CRITICAL}: {message}")

    def error(self, message: str) -> None:
        print(f"{LogLevel.ERROR}: {message}")

    def info(self, message: str) -> None:
        print(f"{LogLevel.INFO}: {message}")

    def warning(self, message: str) -> None:
        print(f"{LogLevel.WARNING}: {message}")

    @classmethod
    def get_logger(cls) -> BaseLogger:
        return cls()
