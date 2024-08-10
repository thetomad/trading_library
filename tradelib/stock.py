import pandas as pd
import sqlite3


class Stock:
    def __init__(self, name: str, data: pd.core.frame.DataFrame = pd.DataFrame()) -> None:
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
        
        if "Close" in self.data.columns:
            self.refactor_db()

    def __str__(self) -> str:
        """Returning the dataframe"""
        return str(self.data)

    def __repr__(self) -> str:
        """Returning the dataframe"""
        return str(self.data)


    # Markers

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
    
    def add_other_markers(self, period: int = 20) -> None:
        "Adding different markers."
        self.data["Prev 7 days minim low"] = self.data["Low"].shift(1).rolling(7).min()
        self.data["Prev 7 days maxim high"] = self.data["High"].shift(1).rolling(7).max()
        self.data['Previous_Close'] = self.data['Close'].shift(1)
        self.data['TR'] = self.data[['High', 'Low', 'Previous_Close']].apply(
            lambda x:   max(x['High'] - x['Low'], 
                        abs(x['High'] - x['Previous_Close']), 
                        abs(x['Low'] - x['Previous_Close'])), 
            axis=1)
        self.data['ATR'] = self.data['TR'].rolling(window=period).mean()


    # Database Table managment. IMPORTANT: always disconnect from db.

    def connect(self, db_name: str = "stock_data.db") -> None:
        "A method that connects to the specified db."
        
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        
    def create_table(self) -> None:
        "Creates the table if it does not already exists."
        
        self.connect()
        try:
            self.data.to_sql(self.name, self.connection, if_exists="fail")
        except ValueError as e:
            print(e)
            
        self.connection.close()

    def read_table(self, conditions: str = "") -> None:
        "Reads values from the database."
        
        self.connect()
        self.data = pd.read_sql_query(f"SELECT * from {self.name} {conditions} ;", self.connection)
        self.calculate_sma()
        self.calculate_ema()
        self.add_crosses()
        self.add_other_markers()

        self.connection.close()

    def update_table(self) -> None:
        "Updates a database table with new values/updated values. Adds on top of historical data."
         
        self.connect()

        self.data.to_sql(self.name, self.connection, if_exists="replace")

        self.connection.close()

    # Refactoring methods.

    def refactor_db(self):
        "Method for refactoring the data for specified stock. This will ensure that the data has the same format in all cases."
        self.calculate_sma()
        self.calculate_ema()
        self.add_crosses()
        self.add_other_markers()






    

    # Buying and selling mehtods
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





