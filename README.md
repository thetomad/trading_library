# Trading Bot

This project is my own implementation using a trading bot. It will be developed using my own skills with limited inside in other peoples projects.

I aim to gradually evolve my algorithmic skills, as well as obtain a better understanding of the trading market. 

## Strategies

I will start by reading about different trading strategies. During my journey, I will gradually evolve my algorithms. The first thing I would take into consideration are Indicators.

### Moving Averages (MA)

MA are a trend-following indicator, which means it depends on the values and movement on past prices. It also helps by eliminating the noise created by short term fluctuations.

There are esentially 2 main MAs: 

1. Simple Moving Average - The SMA selects the number of periods prior (common choices are 10, 20, 50, 100, 200) and makes the simple average for this period. The formula used will be 

$$ SMA = \frac{\sum \text{Price over N periods}}{N}$$

1. Exponential Moving Average - The EMA selects the number of periods prior (common choices are 10, 20, 50, 100, 200) and makes the exponential moving average for this period, with the smoothing factor of $2/(n + 1)$ (where n is 10, 20, 50, 100 or 200 respectively). The EMA calculation then goes as follows:

$$ EMA_{current} = (Price_{today} \times \text{Smoothing Factor}) + (EMA_{previous} \times (1 - \text{Smoothing Factor}))$$ 



