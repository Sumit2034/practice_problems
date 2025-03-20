class Split:

    def __init__(self, user, amount=0.0):
        self._user = user
        self._amount = amount
    
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount
    

