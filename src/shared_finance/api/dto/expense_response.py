from dataclasses import dataclass


@dataclass
class ExpenseResponse:

    date: str
    category: str
    description: str
    amount: float
    paid_by: str