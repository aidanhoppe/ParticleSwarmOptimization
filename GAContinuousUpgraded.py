import math
import random
import time
MAX = 999999
POP_SIZE = 100
PARENTS_SIZE = 20

#Different Optimization Test Functions
#Levi Function N. 13 - minimum 0 at (1,1)
def levi13(genes):
    if(abs(genes[0])>=10 or abs(genes[1])>=10):
        return(MAX)
    else:
        return(math.sin(3*math.pi*genes[0])**2+((genes[0]-1)**2)*(1+math.sin(3*math.pi*genes[1])**2)+(genes[1]-1)**2*(1+math.sin(2*math.pi*genes[1])))

#Booth Function - minimum 0 at (1,3)
def booth(genes):
    if(abs(genes[0])>=10 or abs(genes[1])>=10):
        return(MAX)
    else:
        return((genes[0]+2*genes[1]-7)**2 + (2*genes[0]+genes[1]-5)**2)

def fitness(genes):
    return levi13(genes)

def getParents(population):
    parents = []
    for _ in range(PARENTS_SIZE):
        temp = random.choices(population, k=10)
        temp.sort()
        parents.append(temp[0])
        population.remove(temp[0])
    return parents

def getOffspring(parents, iterations):
    offspring = []
    for _ in range(40):
        ps = random.choices(parents, k=2)
        #crossover
        off1 = [MAX, [ps[0][1][0], ps[1][1][1]]]
        off2 = [MAX, [ps[1][1][0], ps[0][1][1]]]
        #mutation
        if random.random()>.4:
            off1[1][0] += random.uniform((-1/math.sqrt(iterations)),(1/math.sqrt(iterations)))
            off1[1][1] += random.uniform((-1/math.sqrt(iterations)),(1/math.sqrt(iterations)))
        if random.random()>.4:
            off2[1][0] += random.uniform((-1/math.sqrt(iterations)),(1/math.sqrt(iterations)))
            off2[1][1] += random.uniform((-1/math.sqrt(iterations)),(1/math.sqrt(iterations)))
        offspring.append(off1)
        offspring.append(off2)
    return offspring

def geneticAlgorithm(population, iterations):
    newpop = []
    best = MAX
    for p in population:
        p[0] = fitness(p[1])
        if p[0]<best:
            best = p[0]
    parents = getParents(population)
    for p in parents:
        newpop.append(p)
    offspring = getOffspring(parents, iterations)
    for o in offspring:
        newpop.append(o)
    return best, newpop

times = []
for i in range(25):
    timestart = time.time()

    #Initialize Population
    population = []
    for _ in range(POP_SIZE):
        newg = [random.uniform(-10,10), random.uniform(-10,10)]
        fit = fitness(newg)
        population.append([fit, newg])

    
    best = MAX
    iterations = 0
    while(best>.000001):
        iterations += 1
        best, population = geneticAlgorithm(population, iterations)
    times.append(time.time()-timestart)

print("AVG TIME: ", sum(times)/len(times))