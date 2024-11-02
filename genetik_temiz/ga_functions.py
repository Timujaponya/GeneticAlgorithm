import numpy as np
import data as df
from typing import List
import class_Gene as gene
import random
import class_Individual
import class_Population
import pandas as pd

def proximity_func(individual_score, criteria) -> float:
    return np.abs(criteria - individual_score) / criteria * 100


def print_mutation_rate() -> None:
    print(df.MUTATION_RATE)


def get_xy() -> List[int]:
    xy = [0, 0]
    xy[0] = int(input("ma_X değerini giriniz: "))
    xy[1] = int(input("ma_y değerini giriniz: "))
    return xy


def print_genes() -> None:
    print(df.CLASS_ACTIVE_GENES)


def get_gene(genes: List[gene], gne, index=None):
    if index is None:
        for gen in genes:
            if gen.name == gne:
                return gen.value
    elif index is not None:
        for gen in genes:
            if gen.name == gne:
                return gen.value[index]


def get_random(a: int, b: int, count: int):
    return [random.randint(a, b) for i in range(count)]

def genetic_algorithm():
    population = class_Population.Population()
    print(population.best_fitness)
    generation = 1
    while population.best_fitness < 50 and generation < df.NUM_GENERATIONS:
        population.generate_new_population()
        print(f"Generation {generation}: "
              f"Best fitness = {population.best_fitness} "
              f"Success Rate: {population.population_list[0].success_rate} "
              f"Profit: {population.population_list[0].prof_loss} "
              f"MA_X: {population.population_list[0].ma_XY[0]} "
              f"MA_Y: {population.population_list[0].ma_XY[1]} "
              f"İşlem Sayısı: {(len(population.population_list[0].trades))} ")
        generation+=1

"""def calculate_moving_average(data: List[float], window: int) -> List[float]:
    return [round(sum(data[i - window:i]) / window, 3) for i in range(window, len(data))]


def buy_to_sell_points(self) -> List[int]:
    min_len = min(len(self.ma_X_list), len(self.ma_Y_list))
    return [
        1 if (self.ma_X_list[i - 1] > self.ma_Y_list[i - 1]) and (self.ma_X_list[i] < self.ma_Y_list[i]) else 0
        for i in range(min_len)
    ]

def calc_profitlosses(self) -> List[float]:
    buysells = self.buy_to_sell_points()
    for i in range(1,len(buysells)):
        if buysells[i] > 0 and buysells[i - 1] < 0:
            enter = buysells[i]
        elif buysells[i] < 0 and buysells[i - 1] > 0:
            exit = buysells[i]
def create_indicator(self, values: List[float]) -> List[int]:
    return [1 if np.abs(value) < df.FITNESS_THRESHOLD else 0 for value in values]


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
"""