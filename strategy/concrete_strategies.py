from strategy import AbsStrategy


class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3.00


class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.00


class UPSStrategy(AbsStrategy):
    def calculate(self, order):
        return 4.00
