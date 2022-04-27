# fitness function : total number of non attacking pair
# 8 queen 7 pair each total pair = 56
# unique non attacking pair =56/2 = 28 (Goal)
# diagonal check :  abs(col1 - col2) == abs(row2 - row1)

import random



        
# this method will discard any poor performing choromosome 
# apply survival of the fitterst , only higher fitness 
# solution are selected
def selection(population,survivalRate):
    newPopulation = []
    
    #sort the population based on fitness value
    selected = sorted(population,key=lambda x: x["fval"],reverse=True)
    
    #create a population of best fitness value solution
    #based on the survival rate
    for i in range(survivalRate):
        newPopulation.append(selected[i]['chromosome'])
    
    return newPopulation




# mix genetic materials of two parent chromosome
# this is done by merging two list value for each parent solution
def crossOver(population):
    
    # select a parent chromosome pair randomly
    p1 = population[random.randint(1,len(population)-1)]
    p2 = population[random.randint(1,len(population)-1)]
    
    #select a random crossover point
    crossOverPoint = random.randint(3, 7)
    
    
    # divding the parts of parent chromosome based on the crossover point
    # each part is called a gene
    p1part1 = p1[0:crossOverPoint]
    p1part2 = p1[crossOverPoint:]
    p2part1 = p2[0:crossOverPoint]
    p2part2 = p2[crossOverPoint:]
    
    # merge the different gene from two parent 
    # produce two offspring
    off1 = p1part1 + p2part2;
    off2 = p2part1 + p1part2;
    
    return [off1,off2]
    

# this method will modify a solution/list/string/chromosome value
# maintain diveresity in the population
def mutation(population,mutationRate):
    for i in range(mutationRate):
        
        #get a random chromosome to mutate
        rand_idx = random.randint(1, len(population)-1)
        
        #pick a random place in the chromosome to mutate the value
        m_idx = random.randint(1, 8)
        
        #generate a random value to mutate with current value
        m_val = random.randint(1, 8)
        
        #mutate the choromosome
        population[rand_idx][m_idx] = m_val
        
    return population;


# this value ranks a particular solution
# against all other solution by calculating 
# the utility
def fitness(chromosome):
    out = 0
    # row check
    for k in range(1,9):
        r1 = chromosome[k]
        c1 = k
        for j in range(1,9):
            match = False
            r2 = chromosome[j]
            c2 = j
            # only check when the queens are 
            # not in same coloumn
            if c2 != c1:
                # check row attack
                if r2 == r1:
                    match = True
                # check diagonal attack
                if abs(c1-c2) == abs(r2 - r1):
                    match = True
            # increment if non attacking queens
            if c2 != c1 and match == False:
                out += 1
    
    # since a every time two queens are checked
    return int(out/2)
        
                
# main driver code  
def eightQueenGA(initialPopulation,survivalRate,mutationRate,generation):
    
    population = [];
    rankPopulation = []
    
    # generate an list of chromosome called inital population 
    # each chromosome is a solution to the problem
    for i in range(initialPopulation):
        lst = random.sample([1,2,3,4,5,6,7,8], 8);
        lst.insert(0, '-')
        population.append(lst);
    
    
    # rank each solution based on their fitness
    for board in population :
        rankedBoard = {}
        rankedBoard["fval"] = fitness(board)
        rankedBoard["chromosome"] = board
        rankPopulation.append(rankedBoard)
    
    
    # main genetic operation happen in this loop
    for gen in range(generation):
        
        # at first check whether any solution meets the criteria
        # gives fitness value of 28 so search is complete
        for board in rankPopulation:
            if board['fval'] == 28:
                return [board,gen]
        
      
        #code below is to select only the fittest solution from the population
        population = selection(rankPopulation,survivalRate)
        print("Generation : ",gen);
        print("Best performing : ", population[0], "fitness : ",fitness(population[0]))
        nextGeneration = []
        
        #code below is to produce the offspring for the next generation
        while len(nextGeneration) < survivalRate:
            offspring1,offspring2 = crossOver(population)
            nextGeneration.append(offspring1);
            nextGeneration.append(offspring2);
            
        
        #code below is for mutating the population based on mutation rate
        newGeneration = mutation(nextGeneration, mutationRate)
        
        rankPopulation = []
        
        # after mutation a new generation population of chromosome is produced
        # that population each solution is ranked again
        for board in newGeneration :
            rankedBoard = {}
            rankedBoard["fval"] = fitness(board)
            rankedBoard["chromosome"] = board
            rankPopulation.append(rankedBoard)
        
        

if __name__ == '__main__':
    
    # update the intital population size, mutation rate and selection rate
    # to get result ealier in the generation
    
    best_result,generation = eightQueenGA(100, 70, 50, 20000)

    print("Best result :",best_result,"Generation : ",generation)

