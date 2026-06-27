from shared_finance.domain.repositories.expense_repositorie import (
    ExpenseRepository,
)


class ExpenseService:

    def __init__(
        self,
        repository: ExpenseRepository,
    ):
        self._repository = repository

    def list_expenses(self):
        return self._repository.get_all()