import numpy as np
from typing import List
from class_Gene import Gene

def proximity_func(individual_score: float, criteria: float) -> float:
    return np.abs(criteria - individual_score) / criteria * 100

def get_xy() -> List[int]:
    return [
        int(input("ma_X değerini giriniz: ")),
        int(input("ma_y değerini giriniz: "))
    ]

def get_gene(genes: List[Gene], gene_name: str, index: int = None):
    for gene in genes:
        if gene.name == gene_name:
            return gene.value[index] if index is not None else gene.value
    raise ValueError(f"Gene {gene_name} not found")

def calculate_moving_average(data: np.ndarray, window: int) -> np.ndarray:
    return np.convolve(data, np.ones(window), 'valid') / window

def create_indicator(values: np.ndarray) -> np.ndarray:
    return np.where(np.abs(values) < FITNESS_THRESHOLD, 1, 0)

def calculate_percentage(data1: np.ndarray, data2: np.ndarray) -> np.ndarray:
    return (data1 - data2) / data2 * 100

def calculate_percentage_shifted(data: np.ndarray) -> np.ndarray:
    return (data[1:] - data[:-1]) / data[:-1] * 100