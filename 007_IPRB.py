#!/usr/bin/env python

'''
Mendel's First Law
'''

def prob(population, first, second=None):
    '''
    Returns the probability that two mating organisms are both randomly selected.
    If second=None, this implies that the two mating organisms have the same
    allele make-up.
    
    Input:
    - population: total population of mating organisms
    - first: int, number of individuals in grouping of first parent
    - second: int, number of individuals in grouping of second parent given the 
              first parent
    
    Output:
    - p: float, conditional probability that both the first and second parent 
            are selected
    '''       
    prob_first = first/population
    
    if second is None:
        second = first - 1
    
    p = prob_first * second/(population - 1)
    
    return p
    
def prob_dom(k, m, n):
    '''
    Returns the probability that two randomly selected mating organisms will produce
    an individual with a domininant allele.
    
    Calculated by computing the probability of having an offspring with only recessive
    alleles.
    
    Input:
    - k: int >0, individuals homozygous dominant for a factor
    - m: int >0, individuals heterozygous for a factor
    - n: int >0, individuals homozygous recessive for a factor
    
    Output:
    - p: float, probability two mating organisms will have an offspring with a 
            dominant allele
    '''
    
    pop = k + m + n
    
    if pop <= 1:
        return 0

    p = 1 - (prob(pop, n) + .25*prob(pop, m) + .5*(prob(pop, m, n) + prob(pop, n, m)))
    
    return p
    
def main():

    with open('datasets/rosalind_iprb.txt', 'r') as file:
        k, m, n = map(float, file.read().split(' '))
        
    result = str(prob_dom(k, m, n))
            
    with open('output/007_IPRB.txt', 'w') as output:
        output.write(result)
        

if __name__ == '__main__':
    main()