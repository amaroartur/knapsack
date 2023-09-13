import random
import numpy as np
import time

weights = [2, 3, 4, 5, 6]
values = [3, 4, 5, 6, 7]
knapsack_limit = 10

population_size = 50
mutation_rate = 0.1
num_generations = 100

def fitness(chromosome):
    total_weight = sum(weights[i] * chromosome[i] for i in range(len(chromosome)))
    total_value = sum(values[i] * chromosome[i] for i in range(len(chromosome)))
    if total_weight <= knapsack_limit:
        return total_value
    else:
        return 0

def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda c: -fitness(c))
    return tournament[0], tournament[1]

def one_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

def run_genetic_algorithm():
    start_time = time.time()

    population = [[random.randint(0, 1) for _ in range(len(weights))] for _ in range(population_size)]

    for generation in range(num_generations):
        new_population = []
        
        while len(new_population) < population_size:
            parent1, parent2 = tournament_selection(population, tournament_size=5)
            child1, child2 = one_point_crossover(parent1, parent2)
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        
        population = new_population

    best_solution = max(population, key=fitness)
    best_value = fitness(best_solution)

    end_time = time.time()
    execution_time = end_time - start_time

    return best_solution, best_value, execution_time

def main():
    num_runs = 10
    results = []

    for _ in range(num_runs):
        solution, value, execution_time = run_genetic_algorithm()
        results.append((solution, value, execution_time))

    execution_times = [result[2] for result in results]
    max_values = [result[1] for result in results]

    mean_execution_time = np.mean(execution_times)
    std_dev_execution_time = np.std(execution_times)
    mean_max_value = np.mean(max_values)
    std_dev_max_value = np.std(max_values)

    print("Performance Metrics - Genetic Algorithm (GA):")
    print(f"Average Execution Time: {mean_execution_time} seconds")
    print(f"Execution Time Standard Deviation: {std_dev_execution_time} seconds")
    print(f"Average Knapsack Value (GA): {mean_max_value}")
    print(f"Knapsack Value Standard Deviation: {std_dev_max_value}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    execution_time = time.time() - start_time
    print(f"Total Execution Time: {execution_time} seconds")
