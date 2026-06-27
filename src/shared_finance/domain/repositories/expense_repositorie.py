from abc import ABC, abstractmethod

from shared_finance.domain.entities.expense_entitie import Expense


class ExpenseRepository(ABC):
    """
    Contract for expense repositories.
    """

    @abstractmethod
    def get_all(self) -> list[Expense]:
        """
        Returns every expense.
        """