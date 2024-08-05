import pandas as pd
import matplotlib.pyplot as plt
from stock import Stock
import numpy as np

class Graph:
    def __init__(self, stock: Stock) -> None:
        """
        Initializing the Graph for the specific stock.

        :param stock: The specific stock we are interested in.
        """

        self.name = f"{stock.name} graph"
        self.fig, self.ax = plt.subplots()
        self.stock = stock

    def __str__(self) -> str:
        return f"Graphic for {self.stock.name} stock."

    def __repr__(self) -> str:
        return f"Graphic for {self.stock.name} stock."

    def plot_boxplot(self, title: str = "") -> None:
        """
        Creating the plot for the stock.

        :param title: Title of the plot.
        """
        self.ax.boxplot([[
            self.stock.data["Open"].iloc[i],
            self.stock.data["Close"].iloc[i],
            self.stock.data["High"].iloc[i],
            self.stock.data["Low"].iloc[i],]
            for i in range(len(self.stock.data["Open"]))],
            labels=self.stock.data.index.tolist()
            )
        
        self.ax.set_title(title if title != "" else f"Trading data for {self.stock.name} stock")
        
        self.ax.set_ylabel("Values")
        self.ax.set_xlabel("Datetime")
        
    def show_plot(self, rotation_xlabel: int = 90) -> None:
        """
        Display the plot.

        :param rotation_xlabel: The rotation for the x-labels.
        """
        plt.xticks(rotation=rotation_xlabel)
        plt.legend()
        plt.show()
        

    def plot_sma(self, *args: int) -> None:
        """Plotting the SMA graph for the stock."""
        try:
            if (len(args)) == 0:
                args =  (10, 20, 50, 100, 200)
            
            if not all(isinstance(arg, int) for arg in args):
                raise TypeError(f"For the {self.name}: Please insert a valid amound of days (integers).")  

            for arg in args:
                if f"SMA{arg}" not in self.stock.data.columns:
                    raise KeyError(f"No data for SMA{arg}. Please revisit the Stock object")
                self.ax.plot(self.stock.data[f"SMA{arg}"], label=f"SMA{arg}")
                
        except TypeError as e:
            print(e)
        except KeyError as e:
            print(e)

    def plot_ema(self, *args: int) -> None:
        """Plotting the EMA graph for the stock."""
        try:
            if (len(args)) == 0:
                args =  (10, 20, 50, 100, 200)
            
            if not all(isinstance(arg, int) for arg in args):
                raise TypeError(f"For the {self.name}: Please insert a valid amound of days (integers).")  

            for arg in args:
                if f"EMA{arg}" not in self.stock.data.columns:
                    raise KeyError(f"No data for EMA{arg}. Please revisit the Stock object")
                self.ax.plot(self.stock.data[f"EMA{arg}"], label = f"EMA{arg}")
                
        except TypeError as e:
            print(e)
        except KeyError as e:
            print(e)
    
    def show_crosses(self):
        """Method for showing golden and death crosses."""
        self.ax.scatter(self.stock.data[self.stock.data["Golden Cross"]]["Close"].index, self.stock.data[self.stock.data["Golden Cross"]]["Close"], label="Golden Cross")
        self.ax.scatter(self.stock.data[self.stock.data["Death Cross"]]["Close"].index, self.stock.data[self.stock.data["Death Cross"]]["Close"], label="Death Cross")