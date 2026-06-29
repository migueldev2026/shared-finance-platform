from shared_finance.api.dto.expense_response import ExpenseResponse


def to_response(expense):

    return ExpenseResponse(
        date=expense.date.isoformat(),
        category=expense.category,
        description=expense.description,
        amount=expense.amount,
        paid_by=expense.paid_by,
    )