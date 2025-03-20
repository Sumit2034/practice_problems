from typing import List
from constants.expense_type import ExpenseType
from model.expenses.expense_data import ExpenseData
from model.split.split import Split
from repository.expense_repository import ExpenseRepository


class SplitWiseService:

    def __init__(self, expense_repository: ExpenseRepository):
        self.expense_repository = expense_repository
    
    def add_expense(self, expense_type: ExpenseType, amount: float, expense_paid_by: str, splits: List[Split], expense_data: ExpenseData):
        self.expense_repository.add_expense(expense_type, amount, expense_paid_by, splits, expense_data)

    def show_balance(self, user_name):
        balances = self.expense_repository.get_balance(user_name)
        if not balances:
            print("No Balance")
        else:
            for balance in balances:
                print(balance)