from shared_finance.domain.repositories.expense_repositorie import (
    ExpenseRepository,
)


class ExpenseService:

    def __init__(self, repository: ExpenseRepository):
        self.repository = repository

    def get_expenses(self):
        return self.repository.get_all()