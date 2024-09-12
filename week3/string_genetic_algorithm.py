import random

# Constants
TARGET_STRING = "Hello, Genetic Algorithms!"
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000

# Helper functions
def random_char():
    return chr(random.randint(32, 126))

def create_individual(length):
    return ''.join(random_char() for _ in range(length))

def create_population(size, length):
    return [create_individual(length) for _ in range(size)]

def fitness(individual):
    return sum(1 for a, b in zip(individual, TARGET_STRING) if a == b)

def mutate(individual):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random_char()
    return ''.join(individual)

def crossover(parent1, parent2):
    midpoint = random.randint(0, len(parent1) - 1)
    child = parent1[:midpoint] + parent2[midpoint:]
    return child

# Main Genetic Algorithm
def genetic_algorithm():
    population = create_population(POPULATION_SIZE, len(TARGET_STRING))
    for generation in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) == len(TARGET_STRING):
            break
        next_generation = population[:2]
        for _ in range(POPULATION_SIZE // 2 - 1):
            parent1, parent2 = random.sample(population[:50], 2)
            child1 = mutate(crossover(parent1, parent2))
            child2 = mutate(crossover(parent2, parent1))
            next_generation += [child1, child2]
        population = next_generation
        print(f"Generation {generation} - Best fitness: {fitness(population[0])}")
    print(f"Best solution: {population[0]}")

if __name__ == "__main__":
    genetic_algorithm()
