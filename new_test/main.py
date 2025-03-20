from constants.expense_type import ExpenseType
from model.expenses.expense_data import ExpenseData
from model.split.equal_split import EqualSplit
from model.user import User
from repository.expense_repository import ExpenseRepository
from service.splitwise_service import SplitWiseService
from service.user_service import UserService


def main():
    user1 = User(user_id=1, user_name="Sumit", email="sdkjsdh@ajks.com", mobile_number="900909090")
    user2 = User(user_id=2, user_name="Arjun", email="fg@ajks.com", mobile_number="900909091")
    user3 = User(user_id=3, user_name="Kunal", email="dfg@ajks.com", mobile_number="900909092")
    user4 = User(user_id=4, user_name="Satyam", email="sfgd@ajks.com", mobile_number="900909093")

    expense_repository = ExpenseRepository()
    user_service = UserService(expense_repository)
    user_service.add_user(user1)
    user_service.add_user(user2)
    user_service.add_user(user3)
    user_service.add_user(user4)

    service = SplitWiseService(expense_repository)
    user_name = "Sumit"
    amout_spent = 400
    splits = [EqualSplit(user=user_service.get_user("Sumit"))]
    total_members = 3 
    expense_type = ExpenseType.EQUAL
    service.add_expense(expense_type, amout_spent, user_name, splits, ExpenseData("TRIP1"))

    print(service.show_balance("SUMIT"))
    

if __name__=="__main__":
    main()