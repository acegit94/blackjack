class Card:

    def __init__(self, suit: str, value: int):
        self.__suit = suit
        self.__value = value

    def getValue(self) -> int:
        return self.__value

    def __str__(self):
        return f"Suit: {self.__suit}, Value: {self.__value}"