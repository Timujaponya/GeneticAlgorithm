import data as df
import random as rnd


class Gene:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def print_gene(self) -> None:
        print(self.name, self.value)

    def mutata(self):  # mutata :D
        self.value += rnd.randrange(-df.MUTATION_STEP_SIZE, df.MUTATION_STEP_SIZE)
