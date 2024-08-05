import pandas as pd

class Stock:
    def __init__(self, name: str, data: pd.core.frame.DataFrame) -> None:
        """
        Initialize the stock object with an internal pandas dataframe.

        :param name: The name of the stock.

        :param data: A pandas Dataframe of the data pulled from previous API. 
                        It should have the following columns:
                        index: datetime 
                        "Open" 
                        "High" 
                        "Low" 
                        "Close" 
                        "Volume" 
                        
                        Additionally it may have any other columns.
        """
        
        self.name = name
        self.data = data
        self.active = False
        self.amount = 0
        self.initial_value = 0
        
    def __str__(self) -> str:
        """Returning the dataframe"""
        return str(self.data)

    def __repr__(self) -> str:
        """Returning the dataframe"""
        return str(self.data)

    def calculate_sma(self, *args: int) -> None:
        """Calculating the SMA values for eighter standard ones (10, 20, 50, 100, 200) or for specified ones"""
        
        try:
            if (len(args)) == 0:
                args =  (10, 20, 50, 100, 200)
            
            if not all(isinstance(arg, int) for arg in args):
                raise TypeError("Please insert a valid amound of days (integers).")  

            for value in args:
                self.data[f"SMA{value}"] = self.data["Close"].rolling(value).mean()
        except TypeError as e:
            print(e)

    def calculate_ema(self, *args: int) -> None:
        """Calculating the EMA values for eighter standard ones (10, 20, 50, 100, 200) or for specified ones"""
        
        try:
            if len(args) == 0:
                args = (10, 20, 50, 100, 200)

            if not all(isinstance(arg, int) for arg in args):
                raise TypeError("Please insert a valid amound of days (integers).")
            
            for value in args:
                self.data[f"EMA{value}"] = self.data["Close"].ewm(span=value, adjust=False).mean()
        except TypeError as e:
            print(e)

    def add_crosses(self) -> None:
        """Appends 2 boolean columns to the dataframe: Golden Cross and Death Cross."""
        
        # Check for EMA for 50 and 200 and, if it does not exist, create it
        if "EMA10" not in self.data.columns or "EMA200" not in self.data.columns:
            self.calculate_ema()
            
        self.data["Golden Cross"] = (self.data['EMA50'] > self.data['EMA200']) & (self.data['EMA50'].shift(1) <= self.data['EMA200'].shift(1))
        self.data["Death Cross"] = (self.data['EMA50'] < self.data['EMA200']) & (self.data['EMA50'].shift(1) >= self.data['EMA200'].shift(1))
        
    def buy(self, amount: int) -> None:
        """
        Method for buying stocks.
        
        :param amount: The amount of shares to buy.
        """

        self.active = True
        self.amount = amount

    def sell(self) -> None:
        """Method for selling stocks."""
        self.active = False
        self.amount = 0





