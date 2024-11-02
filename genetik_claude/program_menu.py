import data as df
import numpy as np
from class_Population import Population


def menu_case1():
    population = Population()
    for generation in range(df.NUM_GENERATIONS):
        population.evaluate()
        best_individual = population.evaluated_list[0]
        if best_individual.fitness >= df.TERMINATION_RULE:
            print(f"Optimal solution found in generation {generation}")
            return best_individual
        population.population = population.generate_new_population(population.select_parents())
    print("Maximum generations reached")
    return population.evaluated_list[0]


def menu_case2():
    print(f"Population Size: {df.POPULATION_SIZE}")
    print(f"Number of Generations: {df.NUM_GENERATIONS}")
    print(f"Mutation Rate: {df.MUTATION_RATE}")
    print(f"Fitness Threshold: {df.FITNESS_THRESHOLD}")
    print(f"Maximum Evaluations: {df.MAX_EVALUATIONS}")
    print(f"Active Genes: {df.ACTIVE_GENES}")


def menu_case3():
    options = {
        1: ("Population Size", "POPULATION_SIZE", int),
        2: ("Number of Generations", "NUM_GENERATIONS", int),
        3: ("Mutation Rate", "MUTATION_RATE", float),
        4: ("Fitness Threshold", "FITNESS_THRESHOLD", float),
        5: ("Maximum Evaluations", "MAX_EVALUATIONS", int),
        6: ("Active Genes", "ACTIVE_GENES", list)
    }

    while True:
        print("\n".join(f"{k}- {v[0]}" for k, v in options.items()))
        print("0- Back")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice in options:
            option = options[choice]
            if option[1] != "ACTIVE_GENES":
                value = option[2](input(f"Enter new value for {option[0]}: "))
                setattr(df, option[1], value)
            else:
                print("Select indicators to test (comma-separated):")
                print("1 -> Buy to sell transition")
                print("2 -> Open - Close")
                print("3 -> Previous Day Close - Today's Close")
                print("4 -> Support Sell")
                indices = input("Enter choices: ").split(',')
                genes = [0] * 4
                for idx in map(int, indices):
                    if 1 <= idx <= 4:
                        genes[idx - 1] = 1
                df.ACTIVE_GENES = genes
        else:
            print("Invalid choice. Please try again.")


def menu():
    options = {
        1: ("Start Program", menu_case1),
        2: ("Show Variables", menu_case2),
        3: ("Change Variables", menu_case3),
        4: ("Exit Program", exit)
    }

    while True:
        print("\n".join(f"{k}- {v[0]}" for k, v in options.items()))
        choice = int(input("Enter your choice: "))

        if choice in options:
            options[choice][1]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()