import data as df
import ga_functions as ga
import class_Population
# programın kendisi burada çalışacak
def menu_Case1():
    ga.genetic_algorithm()

# data.py dosyasından değişken verilerini çekip ekrana yazdırıyor
def menu_Case2():
    print(f"Popülasyon Genişliği: {df.POPULATION_SIZE}\n"
          f"Jenerasyon Sayısı: {df.NUM_GENERATIONS}\n"
          f"Mutasyon Oranı: {df.MUTATION_RATE}\n"
          f"Fitness Sınırı: {df.FITNESS_THRESHOLD}\n"
          f"Maksimum Değerlendirme: {df.MAX_EVALUATIONS}\n"
          f"Aktif Genler: {df.ACTIVE_GENES.items()}\n")

    print("")

def menu_Case3():

    input_user = int(input("1- Popülasyon Genişliği\n"
                           "2- Jenerasyon Sayısı\n"
                           "3- Mutasyon Oranı\n"
                           "4- Fitness Sınırı\n"
                           "5- Maksimum Değerlendirme\n"
                           "6- Aktif Genler\n"
                           "Geri Dön(0)\n"
                           "Giriniz: "))
    while input_user not in [1, 2, 3, 4, 5, 6, 0]:
        input_user = int(input("1- Popülasyon Genişliği\n"
                               "2- Jenerasyon Sayısı\n"
                               "3- Mutasyon Oranı\n"
                               "4- Fitness Sınırı\n"
                               "5- Maksimum Değerlendirme\n"
                               "6- Aktif Genler\n"
                               "Geri Dön(0)\n"
                               "Giriniz: "))

    match input_user:
        case 1:
            df.POPULATION_SIZE = int(input("Popülasyon genişliğini giriniz: "))
        case 2:
            df.NUM_GENERATIONS = int(input("Jenerasyon sayısını giriniz: "))
        case 3:
            df.MUTATION_RATE = float(input("Mutasyon oranını giriniz: "))  # Mutasyon oranı genellikle ondalıklı bir sayı olmalıdır
        case 4:
            df.FITNESS_THRESHOLD = int(input("Fitness sınırını giriniz: "))
        case 5:
            df.MAX_EVALUATIONS = int(input("Maksimum değerlendirme sayısını giriniz: "))
        case 6:
            prompt = (
                "Test edilmesini istediğiniz indikatörleri seçiniz (virgülle ayırın):\n"
                "1 -> Alış durumundan satış durumuna geçiş\n"
                "2 -> Açılış - Kapanış\n"
                "3 -> Önceki Gün Kapanış Eksi Bugünkü Kapanış\n"
                "4 -> Satışı Destekle\n"
            )
            while True:
                test_list_index = input(prompt).split(',')
                if len(test_list_index) >= 2:
                    break
                print("En az iki indikatör seçiniz (virgülle ayırın):")

            genes = [0, 0, 0, 0]
            for idx in map(str.strip, test_list_index):
                if idx in {"1", "2", "3", "4"}:
                    genes[int(idx) - 1] = 1

            df.ACTIVE_GENES = genes
        case 0:
            return [df.POPULATION_SIZE, df.NUM_GENERATIONS, df.MUTATION_RATE, df.FITNESS_THRESHOLD, df.MAX_EVALUATIONS, df.ACTIVE_GENES]
# data.py dosyasından değişken verilerini çekip kullanıcı isteğine göre üzerinde değişiklikler yapıyor


def menu():

    while True:
        input_user = int(input("1- Programı Başlat\n"
                               "2- Değişkenleri Göster\n"
                               "3- Değişkenleri Değiştir\n"
                               "4- Programı Bitir\n"
                               "Giriniz: "))
        if input_user == 1:
            menu_Case1()
        elif input_user == 2:
            menu_Case2()
        elif input_user == 3:
            menu_Case3()
        elif input_user == 4:
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

    # Program sonlandığında yapılacak işlemler (gerekiyorsa)
    print("Program sonlandırıldı.")