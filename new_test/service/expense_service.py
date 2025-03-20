from typing import List
from constants.expense_type import ExpenseType
from model.expenses.equal_expense import EqualExpense
from model.expenses.exact_expense import ExactExpense
from model.expenses.percent_expense import PercentExpense
from model.expenses.expense_data import ExpenseData
from model.split.percent_split import PercentSplit
from model.split.split import Split
from model.user import User


class ExpenseService:

    @staticmethod
    def create_expense(expense_type: ExpenseType, amount: float, expense_paid_by: User, splits: List[Split], expense_data: ExpenseData):

        if expense_type== ExpenseType.EXACT:
            return ExactExpense(amount, expense_paid_by, splits, expense_data)

        elif expense_type== ExpenseType.PERCENT:
            for split in splits:
                if isinstance(split, PercentSplit):
                    percent_split = split
                    split.amount = (amount*percent_split.percent)/100.0

            return PercentExpense(amount, expense_paid_by, splits, expense_data)
        
        elif expense_type== ExpenseType.EQUAL:
            total_splits = len(splits)
            split_amount = round(amount * 100/total_splits)/100.0
            for split in splits:
                split.amount  = split_amount
            
            return EqualExpense(amount, expense_paid_by, splits, expense_data)
        
        else:
            return "please enter valid split Type"