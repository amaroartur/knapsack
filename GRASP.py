import numpy as np
import re
import time
import random

def knapsack_greedy(solution, value, weight, capacity):
    remaining_capacity = capacity
    total_value = 0
    
    for item in solution:
        if weight[item] <= remaining_capacity:
            total_value += value[item]
            remaining_capacity -= weight[item]
    
    return total_value

def construct_greedy_solution(value, weight, capacity, alpha):
    n = len(value)
    sorted_items = sorted(range(n), key=lambda x: value[x] / weight[x], reverse=True)
    
    solution = []
    remaining_capacity = capacity
    
    for item in sorted_items:
        if weight[item] <= remaining_capacity:
            if random.random() <= alpha:
                solution.append(item)
                remaining_capacity -= weight[item]
    
    return solution

def grasp_knapsack(value, weight, capacity, max_iterations, alpha):
    best_solution = []
    best_value = 0
    
    for _ in range(max_iterations):
        candidate_solution = construct_greedy_solution(value, weight, capacity, alpha)
        candidate_value = knapsack_greedy(candidate_solution, value, weight, capacity)
        
        if candidate_value > best_value:
            best_solution = candidate_solution
            best_value = candidate_value
    
    return best_solution, best_value

def solve_knapsack_problem(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    capacity = int(lines[-1].strip())
    
    id, value, weight = [], [], []
    for line in lines[1:-1]:
        numbers = re.findall(r"[0-9]+", line)
        id.append(int(numbers[0]) - 1)
        value.append(int(numbers[1]))
        weight.append(int(numbers[2]))
    
    return n, value, weight, capacity

def main():
    # Set random seed if needed
    # random.seed(42)

    max_iterations = 100
    alpha = 0.3
    
    output_max_values = []
    execution_times_grasp = []  # List to store GRASP execution times

    for iterator in range(1, 5):
        input_file_path = f"input/input{iterator}.in"
        n, value, weight, capacity = solve_knapsack_problem(input_file_path)

        # Execute GRASP
        start_time = time.time()
        solution, max_value = grasp_knapsack(value, weight, capacity, max_iterations, alpha)
        end_time = time.time()
        execution_time_grasp = end_time - start_time
        execution_times_grasp.append(execution_time_grasp)

        output_max_values.append(max_value)
        output_line = f"Instance {iterator} - GRASP: {max_value}, Time: {execution_time_grasp} s\n"
        
        with open("output/grasp.out", "a+") as output_file:
            output_file.write(output_line)

    # Calculate performance metrics for execution time
    mean_execution_time_grasp = np.mean(execution_times_grasp)
    std_dev_execution_time_grasp = np.std(execution_times_grasp)

    # Calculate performance metrics for knapsack value (solution)
    mean_max_value_grasp = np.mean(output_max_values)
    std_dev_max_value_grasp = np.std(output_max_values)

    print(f"Performance Metrics - GRASP:")
    print(f"Average Execution Time: {mean_execution_time_grasp} s")
    print(f"Execution Time Standard Deviation: {std_dev_execution_time_grasp} s")
    print(f"Average Knapsack Value (GRASP): {mean_max_value_grasp}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    execution_time = time.time() - start_time
    print(f"Total Execution Time: {execution_time} seconds")
