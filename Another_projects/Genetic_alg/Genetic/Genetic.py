import numpy as np
import copy
from tqdm import tqdm

data = np.loadtxt('data/eil51.tsp.txt', usecols=[1,2])

def coordinates_to_adjacency_matrix(data): # заполняем двумерную матрицу расстояний
    a = np.zeros((len(data),len(data)))
    for i in range(len(a)):
        for j in range(len(a)):
            if not i == j:
                a[i][j] = np.linalg.norm(data[i] - data[j])
    return a

class Chromosome():
    
    # Random generated Chromosome
    #  m - number of traveling salesmans
    def __init__(self, number_of_cities, number_of_traveling_salesman, adj = coordinates_to_adjacency_matrix(data)):
        self.n = number_of_cities
        self.m = number_of_traveling_salesman
        self.adj = adj
        c = np.array(range(1,number_of_cities))
        np.random.shuffle(c)                                     # заполняем наш массив рандомными значениями
        self.solution = np.array_split(c, self.m)                # делим массив на колличество продавцов
        for i in range(len(self.solution)):
            self.solution[i] = np.insert(self.solution[i],0,0)   # добавляем нули в начало и конец каждого образовавшегося подмассива
            self.solution[i] = np.append(self.solution[i],0)
        self.fitness()
            
    # Evaluate the Chromosome - Fitness function
    #  based on 2 features: 
    #   - overall cost (cumulated from all salesman)
    #   - worst (longest) salesman cost
    #  adj - adjacency matrix
    def fitness(self):
        self.cost = 0
        longest_salesman_fitness = []
        longest_salesman_length = 0
        for i in range(self.m):
            salesman = self.solution[i]      # присваиваем тут подмассив
            salesman_fitness = 0
            for j in range(len(salesman) - 1):
                salesman_fitness = salesman_fitness + self.adj[salesman[j]][salesman[j+1]]   # считаем показатель фитнесс
            self.cost = self.cost + salesman_fitness                                         # считаем затраты
            if len(salesman) > longest_salesman_length or (len(salesman) == longest_salesman_length and salesman_fitness > self.minmax):
                longest_salesman_length = len(salesman)
                self.minmax = salesman_fitness
        self.score = self.cost + self.minmax
    
    # Mutation operator - mutates a single Traveling Salesman
    #  by swaping 2 cities
    def mutate_local(self):
        index = np.random.randint(0,self.m) # рандомный номер подмассива
        mutant = self.solution[index]       # подмассив с рандомным номером
        i,j = np.random.randint(1,len(mutant)-1), np.random.randint(1,len(mutant)-1)
        mutant[i], mutant[j] = mutant[j], mutant[i]    # меняем 2 значения внутри подмассива
        old_cost = self.cost
        self.fitness()
    
    # Mutation operator - mutates 2 Traveling Salesmans
    #  by removing a city from a salesman and asigning it to the second one
    def mutate_global(self):
        for i in range(self.m):
            if len(self.solution[i]) < 3:    # если длина подмассива меньше 3х
                print(i, self.solution[i])
        
        
        index1, index2 = np.random.randint(0,self.m), np.random.randint(0,self.m)          # рандомные значения номера подмассива
        while index1 == index2:                                                            # если равны то еще раз
            index1, index2 = np.random.randint(0,self.m), np.random.randint(0,self.m)      #
        while len(self.solution[index1]) < 4:                                              # если длина подмассива 1 меньше 4ч делаем еще раз
            index1, index2 = np.random.randint(0,self.m), np.random.randint(0,self.m)
        mutant1, mutant2 = self.solution[index1], self.solution[index2]                    # присваиваем 2 подмассива
        i,j = np.random.randint(1,len(mutant1)-1), np.random.randint(1,len(mutant2)-1)     # рандомные значения элементов в подмассивк
        self.solution[index2] = np.insert(mutant2, j, mutant1[i])                          # вставляем в рандомное место 2го подмассива значение 1го подмассив
        self.solution[index1] = np.delete(mutant1, i)                                      # удаляем это значение у 1го подмассвиа
        old_cost = self.cost
        self.fitness()
    
    # PMX Crossover
    def crossover(self, chromosome):
        for index in range(self.m):
            salesman1, salesman2 = self.solution[index], chromosome.solution[index]        # присваиваем подмассивы из рзаных классов
            for i in range(1,min(len(salesman1),len(salesman2))-1):
                if salesman2[i] in salesman1:                                              # если обнаруживаем элемент 2го подмассива в 1м подмассиве
                    salesman1[i], salesman1[salesman1.tolist().index(salesman2[i])] = salesman1[salesman1.tolist().index(salesman2[i])], salesman1[i] # меняеем их местами??
        self.fitness()
        

class Population():
    
    def __init__(self, population_size = 50, adj = coordinates_to_adjacency_matrix(data)):
        self.population = []
        self.population_size = population_size
        self.adj = adj
        for i in range(population_size):
            self.population.append(Chromosome(number_of_cities = 51, number_of_traveling_salesman = 2)) # добавляем в список класс ХРОМОСОМ
            
    def run_genetic_algorithm(self, number_of_iterations = 1000, mutation_probability = 0.7, crossover_probability = 0.7):
        
        # Run for a fixed number of iterations
        for it in tqdm(range(number_of_iterations)):
            
            # Tournament selection
            k = self.population_size
            j = (int)(self.population_size * 0.6)
            for _ in range(self.population_size - k):
                del self.population[-np.random.randint(0,len(self.population))]   # удаление рандомного подмассива пока размер
            for _ in range(k - j):  # для 0.4 размера популяции                        # массива не станет равен числу популяций
                worst_chromosome_score = self.population[0].score                 # смотрим значение СКОР у 1го класса хромосом
                worst_chromosome_index = 0                                        # присваиваем индекс худшего скора 
                for i in range(1,len(self.population)):                # в массиве классов хромосом
                    if self.population[i].score > worst_chromosome_score:
                        worst_chromosome_score = self.population[i].score
                        worst_chromosome_index = i
                del self.population[-worst_chromosome_index]             # удаляем худший класс хромосом ??
                
            for _ in range(self.population_size - len(self.population)):        # добавляем в массив недостающе хромосомы
                self.population.append(Chromosome(number_of_cities = 51, number_of_traveling_salesman = 2)) 
            
            # Mutate globally
            for index in range(len(self.population)):       # в массиве классом хромосом
                if np.random.random(1)[0] < mutation_probability:   # если рандомная вероятность меньше заданной
                    chromosome = copy.deepcopy(self.population[index])    # создаем копию класса хромосом
                    chromosome.mutate_global()
                    if chromosome.score < self.population[index].score:
                        self.population[index] = chromosome
                
            # Mutate locally
            for index in range(len(self.population)):
                if np.random.random(1)[0] < mutation_probability:
                    chromosome = copy.deepcopy(self.population[index])
                    chromosome.mutate_local()
                    if chromosome.score < self.population[index].score:
                        self.population[index] = chromosome
                
            # Crossover
            for index1 in range(len(self.population)):
                if np.random.random(1)[0] < crossover_probability:
                    index2 = np.random.randint(0,len(self.population))
                    if index1 == index2:
                        index2 = np.random.randint(0,len(self.population))
                    child1 = copy.deepcopy(self.population[index1])
                    child2 = copy.deepcopy(self.population[index2])
                    child1.crossover(self.population[index2])
                    child2.crossover(self.population[index1])
                    if child1.score < self.population[index1].score:
                        self.population[index1] = child1
                    if child2.score < self.population[index2].score:
                        self.population[index2] = child2
    
    def get_best_result(self):
        best_chromosome = self.population[0]
        for i in range(1,self.population_size):
            if self.population[i].score < best_chromosome.score:
                best_chromosome = self.population[i]
        print("Overall cost: ", best_chromosome.cost)
        print("Minmax cost: ", best_chromosome.minmax)
    



pop = Population(population_size=100)
pop.run_genetic_algorithm(number_of_iterations=10000)
pop.get_best_result()


# Iterate through population and get the best solution
best_chromosome = pop.population[0]
for i in range(1,pop.population_size):
    if pop.population[i].score < best_chromosome.score:
        best_chromosome = pop.population[i]
        
# Print best solution
for i in range(best_chromosome.m):
    print(i+1, ":  ", best_chromosome.solution[i][0]+1, end="", sep="")
    for j in range(1,len(best_chromosome.solution[i])):
        print("-", best_chromosome.solution[i][j]+1, end="", sep="")
    print(" --- #", len(best_chromosome.solution[i]))
print()

# Print cost
print("Cost: ", best_chromosome.cost)
print("Minmax: ", best_chromosome.minmax)
