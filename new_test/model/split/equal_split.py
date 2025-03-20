from model.split.split import Split


class EqualSplit(Split):

    def __init__(self, user, amount=0):
        super().__init__(user)