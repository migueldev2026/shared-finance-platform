from dataclasses import asdict
from flask import Blueprint, jsonify

from shared_finance.api.mappers.expense_mapper import to_response
from shared_finance.application.services.expense_service import ExpenseService
from shared_finance.infrastructure.repositories.in_memory_expense_repository import (
    InMemoryExpenseRepository,
)

expenses_bp = Blueprint("expenses", __name__)

repository = InMemoryExpenseRepository()
service = ExpenseService(repository)


@expenses_bp.get("/expenses")
def list_expenses():
    responses = [
    asdict(to_response(expense))
    for expense in service.list_expenses()
]

    return jsonify(responses)

