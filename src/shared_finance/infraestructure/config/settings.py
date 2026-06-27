from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    spreadsheet_id: str
    worksheet_name: str


def get_settings() -> Settings:
    return Settings(
        spreadsheet_id=os.getenv("GOOGLE_SPREADSHEET_ID", ""),
        worksheet_name=os.getenv("GOOGLE_WORKSHEET_NAME", "Expenses"),
    )