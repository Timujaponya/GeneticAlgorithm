from ga_functions import *
import data_file as df


def menu() -> bool:

    while True:
        try:
            input_user = int(input(
                "1- Programı Başlat\n2- Değişkenleri Değiştir\n3- Değişkenleri Göster\n4- Programı Bitir\nEnter: "))
            if input_user == 1:
                menu_case1()
            elif input_user == 2:
                df.POPULATION_SIZE, df.GENERATION_SIZE, df.active_genes, df.test_range, df.MUTATION_RATE = menu_case2()
            elif input_user == 3:
                menu_case3()
            elif input_user == 4:
                print("Program bitiriliyor...")
                return False
            else:
                print("HATA: Lütfen geçerli bir sayı giriniz (1,2,3,4)")
        except ValueError:
            print("HATA: Lütfen geçerli bir sayı giriniz (1,2,3,4)")


def menu_case1():
    rand_numbers = get_random_numbers(df.test_range[0], df.test_range[1], count=2)
    test_population = create_individuals(x=rand_numbers[0], y=rand_numbers[1])
    print(rand_numbers)


def menu_case2():
    program = 1
    while program:
        input_user = input(
            "1- Popülasyon Büyüklüğü\n"
            "2- Jenerasyon Sayısı\n"
            "3- MA_X/Y Aralığı\n"
            "4- Aktif Genler\n"
            "5- Mutasyon Oranı\n"
            "6- Geri Dön"
            "\nEnter: ")
        if input_user == '1':
            df.POPULATION_SIZE = get_size("Enter population size", df.POPULATION_SIZE)
        elif input_user == '2':
            df.GENERATION_SIZE = get_size("Enter generation size", df.GENERATION_SIZE)
        elif input_user == '3':
            df.test_range = get_test_days(df.data_long)
        elif input_user == '4':
            Genes.decide_genes(df.active_genes)
            print(f"Active genes: {df.active_genes}")
        elif input_user == '5':
            df.MUTATION_RATE = get_size("Enter mutation rate", df.MUTATION_RATE)
        elif input_user == '6':
            program = 0
        else:
            print("HATA: Lütfen geçerli bir sayı giriniz (1,2,3,4,5,6)")
    return 0


def menu_case3():
    print(
        f"Popülasyon Büyüklüğü: {df.POPULATION_SIZE} \n"
        f"Jenerasyon Sayısı: {df.GENERATION_SIZE}\n"
        f"Aktif Genler: {df.active_genes} \n"
        f"MA_X/Y Aralığı: {df.test_range}\n"
        f"Mutasyon Oranı: {df.MUTATION_RATE}")
    input_user = int(input("Geri İçin (0) Tuşlayınız: "))
    while input_user != 0:
        print(
            "\n"
            f"Popülasyon Büyüklüğü: {df.POPULATION_SIZE} \n"
            f"Jenerasyon Sayısı: {df.GENERATION_SIZE}\n"
            f"Aktif Genler: {df.active_genes} \n"
            f"MA_X/Y Aralığı: {df.test_range}\n"
            f"Mutasyon Oranı: {df.MUTATION_RATE}")
        input_user = int(input("Geri İçin (0) Tuşlayınız: "))


