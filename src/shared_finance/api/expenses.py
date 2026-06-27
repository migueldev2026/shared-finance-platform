from dataclasses import asdict
from flask import Blueprint, jsonify

from shared_finance.application.services.expense_service import ExpenseService
from shared_finance.infrastructure.repositories.in_memory_expense_repository import (
    InMemoryExpenseRepository,
)

expenses_bp = Blueprint("expenses", __name__)

repository = InMemoryExpenseRepository()
service = ExpenseService(repository)


@expenses_bp.get("/expenses")
def list_expenses():
    expenses = service.list_expenses()

    return jsonify([asdict(expense) for expense in expenses])

