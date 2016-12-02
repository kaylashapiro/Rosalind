#!/usr/bin/env python

'''
Counting Point Mutations
'''

def count_point_mutations(s, t):
    '''
    Returns the number of corresponding symbols that differ in two
    given DNA strings.
    
    Input:
    - s: string of DNA nucleotides
    - t: string of DNA nucleotides
    
    Output:
    -no_point_mutations: int, the Hamming distance between s and t
    '''
    no_point_mutations = 0
    
    for x, y in zip(s, t):
        if x != y:
            no_point_mutations += 1
            
    return no_point_mutations

def main():

    with open('datasets/rosalind_hamm.txt', 'r') as file:
        s, t = file.read().rstrip('\n').split('\n')
       
    result = str(count_point_mutations(s, t))
       
    with open('output/006_HAMM.txt', 'w') as output:
        output.write(result)


if __name__ == '__main__':
    main()