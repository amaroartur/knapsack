import numpy as np
import re
import time

def knapsack(size, value, weight, capacity, dp):
    if size == 0 or capacity == 0:
        return 0
    if dp[size - 1][capacity] != -1:
        return dp[size - 1][capacity]
    if weight[size - 1] > capacity:
        dp[size - 1][capacity] = knapsack(size - 1, value, weight, capacity, dp)
        return dp[size - 1][capacity]
    a = value[size - 1] + knapsack(size - 1, value, weight, capacity - weight[size - 1], dp)
    b = knapsack(size - 1, value, weight, capacity, dp)
    dp[size - 1][capacity] = max(a, b)
    return dp[size - 1][capacity]

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
    
    dp = np.full((n, capacity + 1), -1, dtype=int)
    max_value = knapsack(n, value, weight, capacity, dp)
    return max_value

def main():
    output_max_values = []
    execution_times_pd = []  # List to store PD execution times
    execution_times_ag = []  # List to store AG execution times

    for iterator in range(1, 6):
        input_file_path = f"input/input{iterator}.in"

        # Execute PD
        start_time = time.time()
        max_value = solve_knapsack_problem(input_file_path)
        end_time = time.time()
        execution_time_pd = end_time - start_time
        execution_times_pd.append(execution_time_pd)

        # Store the knapsack value (solution) for PD
        output_max_values.append(max_value)
        output_line = f"Instance {iterator} - PD: {max_value}, Time: {execution_time_pd} s\n"
        
        with open("output/dynamic.out", "a+") as output_file:
            output_file.write(output_line)

        # Execute AG and measure execution time
        start_time = time.time()
        # Replace the line below with the actual call to your AG algorithm
        # max_value_ag = solve_knapsack_problem_with_ag(input_file_path)
        end_time = time.time()
        execution_time_ag = end_time - start_time
        execution_times_ag.append(execution_time_ag)

        # Store the knapsack value (solution) for AG
        # output_max_values_ag.append(max_value_ag)
        # output_line_ag = f"Instance {iterator} - AG: {max_value_ag}, Time: {execution_time_ag} s\n"
        # with open("output/genetic.out", "a+") as output_file_ag:
        #     output_file_ag.write(output_line_ag)

    # Calculate performance metrics for execution time
    mean_execution_time_pd = np.mean(execution_times_pd)
    std_dev_execution_time_pd = np.std(execution_times_pd)
    mean_execution_time_ag = np.mean(execution_times_ag)
    std_dev_execution_time_ag = np.std(execution_times_ag)

    # Calculate performance metrics for knapsack value (solution)
    mean_max_value_pd = np.mean(output_max_values)
    std_dev_max_value_pd = np.std(output_max_values)
    # mean_max_value_ag = np.mean(output_max_values_ag)
    # std_dev_max_value_ag = np.std(output_max_values_ag)

    print(f"Performance Metrics - Dynamic Programming (PD):")
    print(f"Average Execution Time: {mean_execution_time_pd} s")
    print(f"Execution Time Standard Deviation: {std_dev_execution_time_pd} s")
    print(f"Average Knapsack Value (PD): {mean_max_value_pd}")

    # Uncomment this part if you want to calculate metrics for AG
    # print(f"\nPerformance Metrics - Genetic Algorithm (AG):")
    # print(f"Average Execution Time: {mean_execution_time_ag} s")
    # print(f"Execution Time Standard Deviation: {std_dev_execution_time_ag} s")
    # print(f"Average Knapsack Value (AG): {mean_max_value_ag}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    execution_time = time.time() - start_time
    print(f"Total Execution Time: {execution_time} seconds")
