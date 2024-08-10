from .stock import Stock

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
        self.available_money = 200
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
        
        test_value = int(self.available_money / price_stock/ 4)
        val = (test_value if test_value <= 100 else 100)
        # input(str(val) +" " +  str(test_value))
        if test_value != 0:
            self.available_money = self.available_money - val * price_stock
            stock.buy(val)
            # if stock.name not in self.owned_stocks.keys():
            self.owned_stocks[stock.name] = {"amount": val, "total value": val * price_stock, "value unit": price_stock}
            # else:
            #     self.owned_stocks[stock.name]["total value"] += val * price_stock
            #     self.owned_stocks[stock.name]["amount"] += val
            stock.active = True
            
            

    def sell_stocks(self, stock: Stock, price_stock: float) -> None:
        """
        Method for selling stocks.

        :param stock: Object of class Stock (see stock.py file). Stores all necesarry information.
        """
        
        self.available_money += price_stock * stock.amount
        self.owned_stocks.pop(stock.name)
        stock.sell()
        stock.active = False