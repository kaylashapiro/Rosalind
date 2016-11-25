#!/usr/bin/env python

'''
Counting DNA Nucleotides
'''

def count_dna_nucleobases(data):
    '''
    Count the number of times each DNA nucleobase occurs in data.
    
    Input:
    - data: string of DNA nucleotides
    
    Output:
    - A: number of times A occurs in data
    - C: number of times C occurs in data
    - G: number of times G occurs in data
    - T: number of times T occurs in data
    '''
    count = {'A':0, 'C':0, 'G':0, 'T':0}

    for base in data:
        count[base] += 1
        
    A, C, G, T = count['A'], count['C'], count['G'], count['T']
            
    return A, C, G, T

def main():

    with open('datasets/rosalind_dna.txt', 'r') as file:
        data = file.read().rstrip('\n')
        
    results = map(str, count_dna_nucleobases(data))
            
    with open('output/001_DNA.txt', 'w') as output:
        output.write(' '.join(results))


if __name__ == '__main__':
    main()