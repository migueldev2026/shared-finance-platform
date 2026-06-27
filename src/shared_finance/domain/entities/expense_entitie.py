from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Expense:
    date: date
    category: str
    description: str
    amount: float
    paid_by: str