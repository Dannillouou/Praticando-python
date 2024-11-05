
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass

class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

        @property
        def total(self) -> float:
            return self._total

        @property
        def total_discounted(self) -> float:
            return self._discount.calculate(self.total)

class StdDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.9

class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value

class AgeDiscount(DiscountStrategy):
    def __init__(self, age: int) -> None:
        self.discount = age / 100
    
    def calculate(self, value: float) -> float:
        return value * (1 - self.discount)

std_discount = StdDiscount()
no_discount = NoDiscount()
age_discount = AgeDiscount(20)

order_1 = Order(100, std_discount)
print(order_1.total, order_1.total_discounted)

order_2 = Order(100, no_discount)
print(order_2.total, order_2.total_discounted)

order_3 = Order(480, age_discount)
print(order_3.total, order_3.total_discounted)

