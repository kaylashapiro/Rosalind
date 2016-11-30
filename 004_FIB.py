#!/usr/bin/env python

'''
Rabbits and Recurrence Relations
'''

def rabbit_pairs(n, k):
    '''
    Returns the total number of rabbit pairs present after n months 
    starting with 1 pair. Rabbits reach reproductive age after 1 month. 
    Each reproduction-age pair produces a litter of k rabbit pairs.
    
    Input:
    - n: integer, month
    - k: integer, rabbit pairs produced by each reproduction-age pair
    
    Output:
    - adults: total number of rabbit pairs present after n months
    '''
    adults = 0
    young = 1
    
    for i in xrange(n):
        adults, young = adults + young, k*adults
    
    return adults
    
def main():
    with open('datasets/rosalind_fib.txt', 'r') as file:
        data = file.read().rstrip('\n')
        
    n, k = map(int,data.split(' '))
    result = str(rabbit_pairs(n,k))
    
    with open('output/004_FIB.txt', 'w') as output:
        output.write(result)

if __name__ == '__main__':
    main()
            
