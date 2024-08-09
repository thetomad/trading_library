"""
DEPRICATED.

"""


import sqlite3
import pandas as pd

from .stock import Stock


class DBTable:
    def __init__(self, stock: Stock, db_name: str = "stock_data.db") -> None:
        """
        This class will serve as a db table for different stocks. It will be updateable.

        :param stock:   A stock object that will represent the stock.
        :param db_name: The name of the database in which we are finding the table
        """
        self.stock = stock
        self.db_name = db_name

    def __str__(self) -> str:
        return f"DB Table representation for {self.stock.name} stock."
    
    def __repr__(self) -> str:
        return f"DB Table representation for {self.stock.name} stock."
    
    def connect(self) -> None:
        "A method that connects to the specified db."
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
    

    def create_table(self) -> None:
        "Creates the table if it does not already exists."
        
        self.connect()
        try:
            self.stock.data.to_sql(self.stock.name, self.connection, if_exists="fail")
        except ValueError as e:
            print(e)
            
        self.connection.close()

    def read_table(self, conditions: str = "") -> None:
        "Reads values from the database."
        
        self.connect()

        self.stock.data = pd.read_sql_query(f"SELECT * from {self.stock.name} {conditions} ;", self.connection)
        self.stock.calculate_sma()
        self.stock.calculate_ema()
        self.stock.add_crosses()
        self.stock.add_other_markers()

        self.connection.close()
    
    def update_table(self) -> None:
        "Updates a database table with new values/updated values. Adds on top of historical data."
         
        self.connect()

        self.stock.data.to_sql(self.stock.name, self.connection, if_exists="replace")

        self.connection.close()