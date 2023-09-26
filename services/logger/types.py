from dataclasses import dataclass


@dataclass(frozen=True)
class LogLevel:
    CRITICAL: str = "[CRITICAL]"
    ERROR: str = "[ERROR]"
    INFO: str = "[INFO]"
    WARNING: str = "[WARNING]"
