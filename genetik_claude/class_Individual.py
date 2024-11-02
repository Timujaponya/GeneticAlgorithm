import numpy as np
from typing import List
import data as df
import ga_functions as ga
from class_Gene import Gene


class Individual:
    def __init__(self, genes: List[Gene]):
        self.genes = genes
        if not any(g.name == 'ma_X-ma_Y' for g in self.genes):
            self.genes.append(Gene('ma_X-ma_Y', [0, 0]))
        self.enter = np.array([0, 0])
        self.exit = np.array([0, 0])
        self.ma_list = self._calc_moving_averages()
        self.buy_sell_list = self._check_buy_sell()
        self.profit_loss = self._calc_profit_loss()
        self.maintainability = self._check_success_rate()
        self.fitness = self._evaluate_fitness()

    def _calc_moving_averages(self) -> np.ndarray:
        closing_prices = np.array(df.dict_data["Kapanış"])
        ma_x = ga.get_gene(self.genes, 'ma_X-ma_Y', 0)
        ma_y = ga.get_gene(self.genes, 'ma_X-ma_Y', 1)
        return np.array([
            np.convolve(closing_prices, np.ones(ma_x), 'valid') / ma_x,
            np.convolve(closing_prices, np.ones(ma_y), 'valid') / ma_y
        ])

    def _check_buy_sell(self) -> np.ndarray:
        closing_prices = np.array(df.dict_data["Kapanış"])
        opening_prices = np.array(df.dict_data["Açılış"])

        indicator1 = self._create_indicator(self._func_indicator(closing_prices, opening_prices))
        indicator2 = self._create_indicator(self._func_indicator(opening_prices, closing_prices))
        indicator3 = self._create_indicator(self._func_closing_closing(closing_prices))

        conditions = (self.ma_list[0] < self.ma_list[1]) + indicator1 + indicator2 + indicator3
        return np.where(conditions > 0, 1, 0)[:-1]

    def _calc_profit_loss(self) -> np.ndarray:
        price_list = np.array(df.dict_data["Kapanış"])
        buy_sell_diff = np.diff(self.buy_sell_list)
        buy_indices = np.where(buy_sell_diff == 1)[0]
        sell_indices = np.where(buy_sell_diff == -1)[0]

        if len(buy_indices) > len(sell_indices):
            buy_indices = buy_indices[:len(sell_indices)]
        elif len(sell_indices) > len(buy_indices):
            sell_indices = sell_indices[:len(buy_indices)]

        return price_list[sell_indices] - price_list[buy_indices]

    @staticmethod
    def _create_indicator(indicator_list: np.ndarray) -> np.ndarray:
        return np.where(indicator_list > 0, 1, 0)

    @staticmethod
    def _func_indicator(prices1: np.ndarray, prices2: np.ndarray) -> np.ndarray:
        return (prices1 - prices2) / prices2 * 100

    @staticmethod
    def _func_closing_closing(price_list: np.ndarray) -> np.ndarray:
        return (price_list[1:] - price_list[:-1]) / price_list[:-1] * 100

    def _check_success_rate(self) -> float:
        return np.mean(self.profit_loss > 0) * 100

    def _evaluate_fitness(self) -> float:
        return (np.sum(self.profit_loss) * df.PROFIT_VALUE) + (self.maintainability * df.MAINTAINABILITY_VALUE)

    def mutate(self):
        for gene in np.random.choice(self.genes, size=np.random.randint(1, len(self.genes)), replace=False):
            if np.random.random() < df.MUTATION_RATE:
                gene.mutate()