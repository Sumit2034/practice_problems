from model.user import User
from repository.expense_repository import ExpenseRepository


class UserService:
    def __init__(self, expense_repositiory: ExpenseRepository):
        self.expense_repositiory = expense_repositiory
    
    def add_user(self, user: User):
        self.expense_repositiory.add_user(user)
    
    def get_user(self, user_name):
        return self.expense_repositiory.get_user(user_name)