class Card:

    def __init__(self, suit: str, value: int, rank: str):
        self.__suit = suit
        self.__value = value
        self.__rank = rank

    def get_value(self):
        return self.__value

    def get_rank(self):
        return self.__rank

    def set_ace_value(self):
        self.__value = 1
        return self

    def __str__(self):
        return f"{self.__value} of {self.__suit}"