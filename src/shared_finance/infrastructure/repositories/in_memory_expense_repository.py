from datetime import date

from shared_finance.domain.entities.expense_entitie import Expense
from shared_finance.domain.repositories.expense_repositorie import ExpenseRepository


class InMemoryExpenseRepository(ExpenseRepository):

    def get_all(self):

        return [
            Expense(
                date=date(2026, 6, 20),
                category="Mercado",
                description="Éxito",
                amount=85000,
                paid_by="Miguel",
            ),
            Expense(
                date=date(2026, 6, 21),
                category="Transporte",
                description="Uber",
                amount=18000,
                paid_by="Laura",
            ),
        ]