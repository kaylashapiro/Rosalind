#!/usr/bin/env python

''''
Complementing a Strand of DNA
'''

def revc(data):    
    '''
    Returns the reverse complement of a DNA string.
    
    Input:
    - data: string of DNA nucleotides
    
    Output:
    - rev_comp: string formed by reversing data, then taking 
                the complement of each nucleobase
    '''
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    
    rev_comp = ''
    
    for char in data[::-1]:
        rev_comp += complement.get(char)
        
    return rev_comp

def main():

    with open('datasets/rosalind_revc.txt', 'r') as file:
        data = file.read().rstrip('\n')
        
    rev_comp = revc(data)
            
    with open('output/003_REVC.txt', 'w') as output:
        output.write(rev_comp)


if __name__ == '__main__':
    main()

