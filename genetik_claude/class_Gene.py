import data as df
import numpy as np
from dataclasses import dataclass

@dataclass
class Gene:
    name: str
    value: float

    def print_gene(self) -> None:
        print(f"{self.name}: {self.value}")

    def mutate(self):
        self.value += np.random.uniform(-df.MUTATION_STEP_SIZE, df.MUTATION_STEP_SIZE)