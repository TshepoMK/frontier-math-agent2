from dataclasses import dataclass
import os


@dataclass
class Settings:
    model: str = os.getenv("MODEL", "gpt-5")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
