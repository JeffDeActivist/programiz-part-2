class Shop(Exception):
    Sales = []

    def __init__(self, proName, price, sales):
        self.proName = proName
        self.price = price
        self.sales = sales
        Shop.Sales.append(self.daily_sales())

    def daily_sales(self):
        if self.sales > 0:
            return f"{self.proName}, {self.price}, {self.sales},and the total earns from sales are {self.sales * self.price}"
        if self.sales <= 0:
            raise InvalidSales("Sales should be more than 0")


class InvalidSales(Shop):
    pass


s1 = Shop("Baking powder", 300, 20)
s2 = Shop("Laptop", 35000, 2)
s3 = Shop("calculator", 1200, 0)  # raises an error of InvalidSales
for i in Shop.Sales:
    print(i)
