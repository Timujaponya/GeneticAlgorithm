import class_Gene as gene
from typing import List
import data as df
import random as rnd
import ga_functions as ga

class Individual:
    def __init__(self, X=None, Y=None):
        self.price_list = df.dict_data["Kapanış"]
        self.dates_list = df.dict_data["Tarih"]
        if X is None and Y is None:
            while True:
                self.ma_XY = sorted(rnd.randint(1, 150) for i in range(2))
                if self.ma_XY[0] < self.ma_XY[1]:
                    break
        self.window = self.ma_XY[1] - self.ma_XY[0]
        self.ma_list = [self.calc_moving_average(self.price_list, self.ma_XY[0]),
                        self.calc_moving_average(self.price_list, self.ma_XY[1])]
        self.buy_sell_list, self.list_dates = self.buy_sell_funch(self.ma_list)
        self.trades, self.trade_dates = self.calc_trades(self.price_list, self.buy_sell_list)
        self.prof_loss = self.calculate_prof_loss(self.trades)
        self.success_rate = self.calculate_success_rate(self.trades)
        self.fitness = self.calc_fitness()

    def calc_moving_average(self, price_list: List[float], ma: int) -> List[float]:
        ma_list = []
        for idx in range(len(price_list)):
            if idx < ma - 1:
                ma_list.append(0)
            else:
                sum = 0
                for i in range(idx - ma + 1, idx + 1):
                    sum += price_list[i]
                ma_value = (sum / ma, 3)
                ma_list.append(ma_value)
        return ma_list

    def buy_sell_funch(self, ma_list: List[List[float]]) -> (List[int], List[str]):
        min_length = min(len(ma_list[0]), len(ma_list[1]))
        signals = []
        signal_dates = []
        for i in range(min_length):
            if ma_list[0][i] == 0 or ma_list[1][i] == 0:
                signals.append("değer yok")
            elif ma_list[0][i] > ma_list[1][i]:
                signals.append(1)
            else:
                signals.append(0)
            signal_dates.append(self.dates_list[i])
        return signals, signal_dates

    def calc_trades(self, price_list: List[float], buy_sell_list: List[int]) -> (List[float], List[str]):
        trades = []
        trade_dates = []
        position = None  # None if no position, 'buy' if we have bought

        for i in range(len(buy_sell_list)):
            if buy_sell_list[i] == 1 and position is None:
                # Buy signal and no position
                buy_price = price_list[i]
                buy_date = self.dates_list[i]
                position = 'buy'
            elif buy_sell_list[i] == 0 and position == 'buy':
                # Sell signal and currently holding a position
                sell_price = price_list[i]
                sell_date = self.dates_list[i]
                profit_loss = round(sell_price - buy_price, 3)
                trades.append(profit_loss)
                trade_dates.append((buy_date, sell_date))
                position = None  # Reset position

        return trades, trade_dates

    def calculate_prof_loss(self, trades: List[float]) -> float:
        profit_loss = sum(trades)
        return profit_loss

    def calculate_success_rate(self, trades: List[float]) -> float:
        successable = sum(1 for trade in trades if trade > 0)
        return successable / len(trades) * 100 if trades else 0

    def calc_fitness(self):
        # Use constants for consistency
        return (self.prof_loss * df.PROFIT_VALUE) + (self.success_rate / 100 * df.MAINTAINABILITY_VALUE)

    def print_indv(self):
        print(self.price_list)
        print(self.ma_XY)
        print(self.ma_list)
        print(self.buy_sell_list)
        print(self.list_dates)
        print(self.trades)
        print(self.trade_dates)
        print(self.prof_loss)
        print(self.success_rate)
        print(self.fitness)
