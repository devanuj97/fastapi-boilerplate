from __future__ import annotations

from abc import ABC, abstractmethod


class BaseLogger(ABC):
    @abstractmethod
    def critical(self, message: str) -> None: ...

    @abstractmethod
    def error(self, message: str) -> None: ...

    @abstractmethod
    def info(self, message: str) -> None: ...

    @abstractmethod
    def warning(self, message: str) -> None: ...

    @classmethod
    @abstractmethod
    def get_logger(cls) -> BaseLogger: ...
