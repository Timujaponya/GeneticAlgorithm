import pandas as pd

# Genetic Algorithm Constants
PROFIT_VALUE = 0.45
MAINTAINABILITY_VALUE = 0.55
TERMINATION_RULE = 0.95
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.8
CHROMOSOME_LENGTH = 4
ELITISM_RATE = 0.1
FITNESS_THRESHOLD =45
SELECTION_METHOD = 'fitness and random'
MAX_EVALUATIONS = 10000
MUTATION_STEP_SIZE = 0.05
ACTIVE_GENES = {"Alış durumundan satış durumuna geçiş": 0,
                "Açılış - Kapanış": 0,
                "Kapanış - Açılış": 0,
                "Sıralama": 0,
                "Standart Sapma": 0}

# Load data
data = pd.read_excel(r"C:\Users\ardaa\Documents\GitHub\JB\PyCharm\genetik_temiz\GARAN_yuzdesel.xlsx")
dict_data = data.to_dict(orient='list')
data_long = len(dict_data["Kapanış"])
