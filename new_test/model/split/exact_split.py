from model.split.split import Split


class ExactSplit(Split):

    def __init__(self, user, amount=0):
        super().__init__(user, amount)
        self.amount = amount