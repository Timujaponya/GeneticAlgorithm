import pandas as pd
from typing import List,Dict
# data.py

# Genetic Algorithm Constants
PROFIT_VALUE = 0.45
MAINTAINABILITY_VALUE = 0.55
TERMINATION_RULE = 0
POPULATION_SIZE = 100
NUM_GENERATIONS = 50
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.8
CHROMOSOME_LENGTH = 4
ELITISM_RATE = 0.1
FITNESS_THRESHOLD = 0.95
SELECTION_METHOD = 'fitness and random'
MAX_EVALUATIONS = 10000
MUTATION_STEP_SIZE = 0.05
ACTIVE_GENES = [["Alış durumundan satış durumuna geçiş", "Açılış - Kapanış",
                 "Kapanış - Açılış", "Sıralama", "Standart Sapma"],
                [0, 0, 0, 0, 0]]
# Load data
data = pd.read_excel(r"C:\Users\ardaa\Documents\GitHub\JB\PyCharm\genetik_temiz\GARAN_yuzdesel.xlsx")
dict_data = data.to_dict(orient='list')
data_long = len(dict_data["Kapanış"])


class Gene:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def print_gene(self) -> None:
        print(self.name, self.value)

    def mutata(self):  # mutata :D
        self.value += rnd.randrange(-df.MUTATION_STEP_SIZE, df.MUTATION_STEP_SIZE)


class Individual:
    def __init__(self, genes: List[gene] = None):
        self.genes = genes
        if not any(g.name == 'ma_X-ma_Y' for g in self.genes):
            self.genes.append(gene.Gene('ma_X-ma_Y', [0, 0]))
        self.enter = [0, 0]  # Satom alım işleminin yapıldığı nokta ["listedeki sırası","alış fiyatı"]
        self.exit = [0, 0]  # Satış işleminin yapıldığı nokta ["listedeki sırası","satış fiyatı"]
        self.ma_list = [self.calc_moving_average(df.dict_data["Kapanış"], ga.get_gene(genes, 'ma_X-ma_Y', 0)),
                        self.calc_moving_average(df.dict_data["Kapanış"], ga.get_gene(genes, 'ma_X-ma_Y', 1))]
        self.fitness = self.evaluate_fitness()  # Fitness değerinin hesaplanması
        self.buy_sell_list = self.check_buy_sell(self.ma_list)
        self.profit_loss = self.profitloss(self.buy_sell_list, df.dict_data["Kapanış"])
        self.maintainability = self.check_success_rate(self.profit_loss)  # Yapılan işlemin başarı oranı

    def calc_moving_average(self, liste: List[float],
                            interval):  # MA değerleri hesaplanacak (hesaplanacak liste, ma aralığı)_
        return [round(sum(liste[i: i + interval], ) / interval, 3) for i in range(interval - 1, len(liste))]

    def check_buy_sell(self, ma_list: List[
        List[float]]):  # Verilen iki ma listesini karşılaştırıp 1,0 değerleri ile bir tablo veriyor
        return [1 if ((ma_list[i][0] < ma_list[i][1]) +
                      self.create_indicator(self.func_indicator([df.dict_data["Kapanış"], df.dict_data["Açılış"]]))[i]
                      + self.create_indicator(self.func_indicator([df.dict_data["Açılış"], df.dict_data["Kapanış"]]))[i]
                      + self.create_indicator(self.func_closing_closing([df.dict_data["Kapanış"]]))[i]) else 0 for i in
                range(len(ma_list) - 1)]

    def profitloss(self, buy_sell_list: List[float], price_list: List[float]) -> List[
        float]:  # Diğer indikatörleri ayarlayınca burayı değiştir
        # Verilen 1,0 ve fiyat listelerini kullanarak alınan,satılan noktaları
        liste = []  # buluyor ve kar/zarar durumunu hesaplıyor ve kar/zarar listesi return ediyor
        enter: int = 0
        exit_point: int = 0
        for i in range(len(buy_sell_list)):

            if buy_sell_list[i - 1] == 0 and buy_sell_list[i] == 1:
                enter = i
            elif buy_sell_list[i - 1] == 1 and buy_sell_list[i] == 0:
                exit_point = i
            liste.append(
                price_list[exit_point] - price_list[enter]) if enter is not None and exit_point is not None else 0
        return liste

    def create_indicator(self, indicator_list: List[float]) -> List[int]:
        return [1 if indicator_list[i] > 0 else 0 for i in range(len(indicator_list) - 1)]

    def func_indicator(self, prices: List[List[float]]):
        liste = []
        for i in range(len(prices[0])):
            liste.append((prices[0][i] - prices[1][i]) / prices[1][i] * 100)
        return liste

    def func_closing_closing(self, price_list: List[float]):
        liste = []
        for i in range(len(price_list)):
            liste.append((price_list[i] - price_list[i]) / price_list[i] * 100)
        return liste

    def check_success_rate(self, profit_loss: List[float]) -> float:
        count = 0
        for i in range(len(profit_loss)):
            if profit_loss[i] > 0:
                count += 1
        return count / (len(profit_loss) + 1) * 100

    def evaluate_fitness(self):

        return (self.profit_loss * df.PROFIT_VALUE) + (self.maintainability * df.MAINTAINABILITY_VALUE)

    def mutate(self):
        for gne in range(rnd.randint(0, len(self.genes) - 1)):
            if rnd.random() < df.MUTATION_RATE:
                gne.mutata()
