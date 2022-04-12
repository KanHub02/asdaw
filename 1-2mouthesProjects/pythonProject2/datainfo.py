
class Bank:
    def __init__(self, cash):
        self.__cash = cash

        @property
        def cash(self):
            return self.__cash

        @cash.setter
        def cash(self, value):
            self.__cash = value
