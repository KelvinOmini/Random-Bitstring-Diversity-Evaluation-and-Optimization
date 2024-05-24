import random
import itertools
import matplotlib.pyplot as plt

random.seed(1234)

def generate_random_bitstring(n):
    return [random.randint(0, 1) for _ in range(n)]

# print(generate_random_bitstring(5))

def hamming_distance(bitstring1, bitstring2):
    return sum(bit1 != bit2 for bit1, bit2 in zip(bitstring1, bitstring2))

'''
def evaluate_diversity(population):
    n = len(population)
    total_distance = 0
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            total_distance += hamming_distance(population[i], population[j])
            count += 1

    average_distance = total_distance / count
    return average_distance
'''


# Evaluate the diversity of a population of bitstrings using a more Pythonic approach
def evaluate_diversity(population):
    pairs = itertools.combinations(population, 2)
    distances = [hamming_distance(pair[0], pair[1]) for pair in pairs]
    average_distance = sum(distances) / len(distances)
    return average_distance


def random_search(pop_size, bitstring_length, max_iterations):
    best_solution = None
    best_fitness = -1

    for i in range(max_iterations):
        population = [generate_random_bitstring(bitstring_length) for _ in range(pop_size)]
        fitness = round(evaluate_diversity(population), 2)

        if fitness > best_fitness:
            best_solution = population
            best_fitness = fitness

    return best_solution, best_fitness

# Set the random seed for reproducibilitymk


# Define parameters
while True:
    bitstring_length = int(input("Enter bitstring length: "))
    pop_size = int(input("Enter population size: "))
    max_iterations = int(input("Enter the maxixmum interation value: "))

    # Perform random search
    best_solution, best_fitness = random_search(pop_size, bitstring_length, max_iterations)

    # Calculate average best fitness score for each bitstring length
    fitness_dict = {}
    for _ in range(int(input("Runs: "))):  # Number of runs for averaging
        best_solution, best_fitness = random_search(pop_size, bitstring_length, max_iterations)
        if bitstring_length not in fitness_dict:
            fitness_dict[bitstring_length] = [best_fitness]
        else:
            fitness_dict[bitstring_length].append(best_fitness)

    # Calculate average fitness score for each bitstring length
    average_fitness_scores = {}
    for length, scores in fitness_dict.items():
        average_fitness_scores[length] = sum(scores) / len(scores)

    # Print the results
    for length, avg_fitness in average_fitness_scores.items():
        print(f"Bitstring Length: {length}, Average Best Fitness: {avg_fitness}")


    # Plotting the results
    plt.figure(figsize= (10, 5))
    plt.plot(length, avg_fitness, marker = 'o')
    plt.title("Random Search Performance Analysis")
    plt.xlabel("Bitstring length")
    plt.ylabel("Average Best Fitness Score")
    plt.grid(True)
    plt.show()