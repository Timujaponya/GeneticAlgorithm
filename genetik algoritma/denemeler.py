from data_file import *
import statistics

genes = {"Alış durumundan satış durumuna geçiş": [9, 19, 0.68],
         "Açılış - Kapanış": 2.64,
         "Kapanış - Kapanış": 3.05,
         "Kapanış - Açılış": 0.40,
         "sıralama": "1,2,3",
         "standart sapma": 0}
std= statistics.stdev(dict_data["Kapanış"][genes["Alış durumundan satış durumuna geçiş"][0]:genes["Alış durumundan "
                                                                                                  "satış durumuna "
                                                                                                  "geçiş"][1]])
genes["standart sapma"] = std

print(std)
print(genes["standart sapma"])