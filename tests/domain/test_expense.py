from datetime import date

from shared_finance.domain.entities.expense_entitie import Expense


def test_create_expense():

    expense = Expense(
        date=date.today(),
        category="Food",
        description="Pizza",
        amount=50000,
        paid_by="Miguel",
    )

    assert expense.category == "Food"
    assert expense.amount == 50000