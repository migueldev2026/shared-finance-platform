from datetime import date
from unittest.mock import Mock

from shared_finance.application.services.expense_service import ExpenseService
from shared_finance.domain.entities.expense_entitie import Expense
from shared_finance.domain.repositories.expense_repositorie import ExpenseRepository


def test_list_expenses_returns_repository_data():
    # Arrange
    repository = Mock(spec=ExpenseRepository)

    expected_expenses = [
        Expense(
            date=date(2026, 6, 20),
            category="Food",
            description="Pizza",
            amount=50000,
            paid_by="Miguel",
        )
    ]

    repository.get_all.return_value = expected_expenses

    service = ExpenseService(repository)

    # Act
    result = service.list_expenses()

    # Assert
    repository.get_all.assert_called_once()
    assert result == expected_expenses