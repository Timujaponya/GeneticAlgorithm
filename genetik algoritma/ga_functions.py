from class_Exceptions import *
from class_Individual import *

import random


def get_size(prompt: str, default_size: int) -> int:
    size = input(f"{prompt} (default = {default_size}): ")
    return int(size) if size else default_size


def get_numbers(prompt: str) -> List[float]:
    while True:
        try:
            input_str = input(prompt)
            return list(map(float, input_str.split(',')))
        except ValueError:
            print("Geçersiz giriş. Lütfen sayı olarak değer giriniz:")


def get_test_days(long: int) -> List[int]:
    while True:
        try:
            input_str = list(input("İstenen gün testi aralığını giriniz: ").split(','))
            if input_str[1] > str(long):
                raise DataLongException("İstenen gün aralığı veri uzunluğundan büyük olamaz")
            return list(map(int, input_str))
        except (ValueError, DataLongException) as e:
            print(e)


def get_random_numbers(start: int, end: int, count: int) -> List[int]:
    return sorted(random.sample(range(start, end + 1), count)) if count > 1 else [random.randint(start, end)]


def create_individuals(x: int, y: int) -> List[Individual]:
    return [Individual(active_genes, x + i, y + i, dict_data, MUTATION_RATE) for i in range(POPULATION_SIZE)]

