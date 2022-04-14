import math
import random
import time
POP_SIZE = 100
ACCELERATION = .5
INERTIA = .5
MAX = 999999
class Particle:
    def __init__(self, pos, velocity, pbest):
        #pos = [x, y]
        self.pos = pos
        #velocity = [vx, vy]
        self.velocity = velocity
        #pbest = [eval, pos]
        self.pbest = pbest

#Different Optimization Test Functions
#Levi Function N. 13 - minimum 0 at (1,1)
def levi13(par): 
    if(abs(par.pos[0])>10 or abs(par.pos[1])>10):
        return(MAX)
    else:
        return(math.sin(3*math.pi*par.pos[0])**2+((par.pos[0]-1)**2)*(1+math.sin(3*math.pi*par.pos[1])**2)+(par.pos[1]-1)**2*(1+math.sin(2*math.pi*par.pos[1])))

#Matyas Function - minimum 0 at (0,0)
def matyas(par):
    if(par.pos[0]<-10 or par.pos[0]>10 or par.pos[1]>10 or par.pos[1]<-10):
        return(MAX)
    else:
        return(.26*(par.pos[0]**2+par.pos[1]**2)-.48*par.pos[0]*par.pos[1])

#Booth Function - minimum 0 at (1,3)
def booth(par):
    if(abs(par.pos[0])>10 or abs(par.pos[1])>10):
        return(MAX)
    else:
        return((par.pos[0]+2*par.pos[1]-7)**2 + (2*par.pos[0]+par.pos[1]-5)**2)

#Particle Swarm Function
def particleSwarm(population, gbest):
    for par in population:
        #eval = booth(par)
        eval = levi13(par)
        #eval = matyas(par)
        #Update Personal Best if applicable
        if eval < par.pbest[0]:
            par.pbest = [eval, par.pos]
        #Update Global Best if applicable
        if eval < gbest[0]:
            gbest = [eval, par.pos]
        #UPDATE VELOCITY
        vnewx = INERTIA * par.velocity[0] + ACCELERATION*(random.random()*(par.pbest[1][0]-par.pos[0])+random.random()*(gbest[1][0]-par.pos[0]))
        vnewy = INERTIA * par.velocity[1] + ACCELERATION*(random.random()*(par.pbest[1][1]-par.pos[1])+random.random()*(gbest[1][1]-par.pos[1]))
        par.velocity = [vnewx, vnewy]
        #UPDATE POSITION
        par.pos = [par.pos[0]+vnewx, par.pos[1]+vnewy]
    return population, gbest

times = []
for i in range(500):
    timestart = time.time()

    #Initialize Population
    population = []
    for _ in range(POP_SIZE):
        newp = Particle([random.uniform(-10,10), random.uniform(-10,10)], [0,0], [MAX, [MAX,MAX]])
        #newp.pbest[0] = booth(newp)
        newp.pbest[0] = levi13(newp)
        #newp.pbest[0] = matyas(newp)
        newp.pbest[1] = newp.pos
        population.append(newp)

    #Iterate Particle Swarm Until Acceptance Threshold is Hit
    gbest = [MAX, [MAX,MAX]]
    while(gbest[0]>.000001):
        population, gbest = particleSwarm(population, gbest)
    times.append(time.time()-timestart)
    
print("AVG TIME: ", sum(times)/len(times))
