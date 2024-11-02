from interface_menu import menu
def main() -> None:
    menu()
    while criteria not in fitness_list:
        get_termination_crit()
        init_population()
        selection()
        crossover()
        mutation()
        fitness_list = fitness_func()

    for individual in fitness_list:
        if individual == criteria:
            print(individual)





if __name__ == '__main__':
    main()
