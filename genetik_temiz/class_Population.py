from class_Individual import Individual
from typing import List
import random as rnd
import data as df

class Population:
    def __init__(self, population_size=None):
        self.population_size = population_size or df.POPULATION_SIZE
        self.population_list = [Individual() for _ in range(self.population_size)]
        self.evaluated_list = self.evaluate()
        self.best_fitness = self.evaluated_list[0].fitness
        self.best_individuals = self.get_unique_best_individuals()

    def evaluate(self) -> List[Individual]:
        # Ensure evaluation is correct and consistent
        return sorted(self.population_list, key=lambda x: x.fitness, reverse=True)

    def get_unique_best_individuals(self) -> List[Individual]:
        best_fitness = self.evaluated_list[0].fitness
        return [ind for ind in self.evaluated_list if ind.fitness == best_fitness]

    def select_parent(self) -> List[List[Individual]]:
        segment_size = max(1, round(len(self.evaluated_list) * 0.1))
        return [self.evaluated_list[i*segment_size:(i+1)*segment_size] for i in range(min(3, len(self.evaluated_list) // segment_size))]

    def crossover(self, parent1: List[Individual], parent2: List[Individual]) -> List[Individual]:
        offspring = []
        for i in range(min(len(parent1), len(parent2))):
            if parent1[i].ma_XY[1] > parent2[i].ma_XY[0] and parent2[i].ma_XY[1] > parent1[i].ma_XY[0]:
                gene = rnd.randint(0, 1)
                # Swap genes
                parent1[i].ma_XY[gene], parent2[i].ma_XY[gene] = parent2[i].ma_XY[gene], parent1[i].ma_XY[gene]
            # Create new individuals from parents
            offspring.extend([parent1[i], parent2[i]])
        return offspring

    def generate_new_population(self):
        segment_size = max(1, round(self.population_size * 0.1))
        save = self.evaluated_list[:segment_size]
        parents_lists = self.select_parent()
        new_population = []

        for parents in parents_lists:
            offspring = self.crossover(parents_lists[0], parents)
            new_population.extend(offspring)

        # Ensure population size does not exceed the desired count
        new_population = new_population[:self.population_size]  # Trim to fit population size

        # Add new individuals to meet the population size if necessary
        while len(new_population) < self.population_size:
            new_population.append(Individual())

        self.population_list = new_population + save[:self.population_size - len(new_population)]
        self.evaluated_list = self.evaluate()
        self.best_fitness = self.evaluated_list[0].fitness
        self.best_individuals = self.get_unique_best_individuals()

        # Debug information
        print(f"New population size: {len(self.population_list)}")
        print(f"Best fitness after generation: {self.best_fitness}")
