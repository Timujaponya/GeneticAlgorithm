import pandas as pd

# Constants
MUTATION_RATE = 0.01
POPULATION_SIZE = 100
GENERATION_SIZE = 100
active_genes = {"Alış durumundan satış durumuna geçiş": [0, 0, 0],
                "Açılış - Kapanış": 0,
                "Kapanış - Kapanış": 0,
                "Kapanış - Açılış": 0,
                "Sıralama": "1,2,3",
                "Standart Sapma": 0}
test_range = [0, 100]
treshold = 3
treshold_range = [0, 5]
MUTATION_STRENGTH = 0.1
# Load data
data = pd.read_excel(r"C:\Users\ardaa\Documents\GitHub\JB\PyCharm\genetik algoritma\data\GARAN_yuzdesel.xlsx")
dict_data = data.to_dict(orient='list')
data_long = len(dict_data["Kapanış"])
