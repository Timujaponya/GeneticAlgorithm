import numpy as np
from typing import List
import data as df
from class_Individual import Individual

class Population:
    def __init__(self, genes=None, population_size=None):
        self.population_size = population_size or df.POPULATION_SIZE
        self.genes = genes or df.ACTIVE_GENES
        self.population = [Individual(self.genes) for _ in range(self.population_size)]
        self.evaluated_list = self.evaluate()

    def evaluate(self) -> List[Individual]:
        return sorted(self.population, key=lambda individual: individual.fitness, reverse=True)

    def select_parents(self) -> List[List[Individual]]:
        num_individuals = len(self.evaluated_list)
        segment_size = int(num_individuals * 0.2)
        return [
            self.evaluated_list[:segment_size],
            self.evaluated_list[segment_size:2*segment_size],
            self.evaluated_list[2*segment_size:3*segment_size]
        ]

    def crossover(self, parent1: Individual, parent2: Individual) -> List[Individual]:
        for i in range(len(parent1.genes)):
            if np.random.random() < df.CROSSOVER_RATE:
                parent1.genes[i].value, parent2.genes[i].value = parent2.genes[i].value, parent1.genes[i].value
        return [parent1, parent2]

    def generate_new_population(self, parents_lists: List[List[Individual]]) -> List[Individual]:
        new_population = []
        for i in range(1, len(parents_lists)):
            for j in range(len(parents_lists[0])):
                new_population.extend(self.crossover(parents_lists[0][j], parents_lists[i][j]))
        return new_population