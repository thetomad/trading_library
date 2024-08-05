from stock import Stock

class Portfolio:
    def __init__(self) -> None:
        """
        Portfolio class will serve as a paer trail emulator of the main portfolio on the buying website.
        This class will emulate the buy and sell of stocks.

        To do:
            - Add historical logs for transactions.
            - If ever connected to any portfolio, add trade confirmations.
            - Decision making.
        """
        self.available_money = 10000
        self.owned_stocks = {}
    
    def __str__(self) -> str:
        return f"You have {self.available_money} dollars."
    
    def __repr__(self) -> str:
        return f"You have {self.available_money} dollars."

    def buy_stocks(self, stock: Stock, price_stock: float) -> None:
        """
        Method for buying stocks.

        :param stock: Object of class Stock (see stock.py file). Stores all necesarry information.
        """
        
        test_value = int(self.available_money / price_stock / 4)
        
        if test_value != 0:
            self.available_money -= (test_value if test_value <= 10 else 10) * price_stock
            stock.buy((test_value if test_value <= 10 else 10))
            self.owned_stocks[stock.name] = {"amount": (test_value if test_value <= 10 else 10), "total value": (test_value if test_value <= 10 else 10) * price_stock}
            stock.active = True
            stock.initial_value = price_stock
            


    def sell_stocks(self, stock: Stock, price_stock: float) -> None:
        """
        Method for selling stocks.

        :param stock: Object of class Stock (see stock.py file). Stores all necesarry information.
        """
        
        self.available_money += price_stock * stock.amount
        self.owned_stocks.pop(stock.name)
        stock.sell()
        stock.active = False
        stock.initial_value = 0