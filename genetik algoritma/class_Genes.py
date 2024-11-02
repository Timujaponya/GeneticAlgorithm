import data_file as df

class Genes:
    def __init__(self, genes: {dict} = None, mutation_strength: float = df.MUTATION_STRENGTH, mutation_rate: float = df.MUTATION_RATE):
        self.genes = genes if genes is not None else {"Alış durumundan satış durumuna geçiş": [0, 0, 0],
                                                              "Açılış - Kapanış": 0,
                                                              "Kapanış - Kapanış": 0,
                                                              "Kapanış - Açılış": 0,
                                                              "Sıralama": "1,2,3",
                                                              "Standart Sapma": 0}
        self.mutation_strength = mutation_strength
        self.mutation_rate = mutation_rate



    def decide_genes(self) -> None:
        prompt = (
            "Test eilmesini istediğiniz indikatörleri seçiniz (virgülle ayırın):\n"
            "1 -> Açılış - Kapanış\n"
            "2 -> Kapanış - Kapanış\n"
            "3 -> Kapanış - Açılış\n"
        )
        while True:
            test_list_index = input(prompt).split(',')
            if len(test_list_index) >= 2:
                break
            print("En az iki indikatör seçiniz (virgülle ayırın):")
        for i in range(len(test_list_index)):
            if test_list_index[i] in ["1", "2", "3"]:
                match test_list_index[i]:
                    case "1":
                        self.genes["Açılış - Kapanış"] = 1
                    case "2":
                        self.genes["Kapanış - Kapanı"] = 1
                    case "3":
                        self.genes["Kapanış - Açılış"] = 1
            else:
                while "1" not in test_list_index and "2" not in test_list_index and "3" not in test_list_index:
                    prompt = (
                        "Test eilmesini istediğiniz indikatörleri seçiniz (virgülle ayırın):\n"
                        "1 -> Açılış - Kapanış\n"
                        "2 -> Kapanış - Kapanış\n"
                        "3 -> Kapanış - Açılış\n"
                    )
                    while True:
                        test_list_index = input(prompt).split(',')
                        if len(test_list_index) >= 2:
                            break
                        print("En az iki indikatör seçiniz (virgülle ayırın):")
        df.active_genes = self.genes