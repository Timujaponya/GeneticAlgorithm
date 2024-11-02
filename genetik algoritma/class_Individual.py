from class_Genes import Genes
import data_file as df
from typing import List
import numpy as np

class Individual:
    def __init__(self, genes: {dict} , x: int, y: int, data_dict, mutation_rate = float(df.MUTATION_RATE)):
        self.enter = 0
        self.exit = 0
        self.profitloss = 0
        self.proximity = 0
        self.maintainability = 0
        self.care_treshold = 1.0
        self.fitness = (self.proximity * 0.45) + (self.maintainability * 0.55)
        self.genes = Genes(genes, mutation_rate)
        self.ma_X_list = self.calculate_moving_average(data_dict["Kapanış"], x)
        self.ma_Y_list = self.calculate_moving_average(data_dict["Kapanış"], y)

    def calculate_moving_average(self, data: List[float], window: int) -> List[float]:
        return [round(sum(data[i - window:i]) / window, 3) for i in range(window, len(data))]

    def buy_to_sell_points(self) -> List[int]:
        min_len = min(len(self.ma_X_list), len(self.ma_Y_list))
        return [
            1 if (self.ma_X_list[i - 1] > self.ma_Y_list[i - 1]) and (self.ma_X_list[i] < self.ma_Y_list[i]) else 0
            for i in range(min_len)
        ]

    def calculate_percentage(self, column1: str, column2: str) -> List[float]:
        return [
            round(((df.dict_data[column1][i] - df.dict_data[column2][i]) / df.dict_data[column2][i]) * 100, 2)
            for i in range(df.data_long)
        ]

    def calculate_percentage_shifted(self, column1: str, column2: str) -> List[float]:
        return [
            round(((df.dict_data[column1][i] - df.dict_data[column2][i - 1]) / df.dict_data[column2][i - 1]) * 100, 2)
            for i in range(1, df.data_long)
        ]

    def create_indicator(self, values: List[float]) -> List[int]:
        return [1 if np.abs(value) < df.treshold else 0 for value in values]

    def acilis_kapanis(self) -> List[float]:
        return self.calculate_percentage("Kapanış", "Açılış")

    def acilis_kapanis_indicator(self) -> List[int]:
        return self.create_indicator(self.acilis_kapanis())

    def kapanis_kapanis(self) -> List[float]:
        return self.calculate_percentage_shifted("Kapanış", "Kapanış")

    def kapanis_kapanis_indicator(self) -> List[int]:
        return self.create_indicator(self.kapanis_kapanis())

    def support_sell(self) -> List[float]:
        return self.calculate_percentage_shifted("Açılış", "Kapanış")

    def support_sell_indicator(self) -> List[int]:
        return self.create_indicator(self.support_sell())
