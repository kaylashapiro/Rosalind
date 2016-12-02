#!/usr/bin/env python
'''
Computing GC Content
'''

from helpers.data import parse_FASTA

def get_GC(DNA):
    '''
    Returns DNA string and GC content of that string.
    
    /!\ GC content is given as a percentage rather than a fraction. /!\
    
    Input:
    - DNA: string of DNA nucleotides
    
    Output:
    - DNA: string of DNA nucleotides
    - GC_content: float, percentage of symbols in the string that are 'C' or 'G'
    '''
    GC_sum = 0
    total = len(DNA)
    
    for char in DNA:
        if char == 'C' or char == 'G':
            GC_sum += 1
            
    GC_content = 100 * float(GC_sum)/total
            
    return DNA, GC_content
    
def get_max_GC(data):
    '''
    Returns ID of the string having the highest GC content, followed by 
    the GC content of that string.
    
    Input:
    - data: string of DNA nucleotides in FASTA format
    
    Output:
    - max_label: ID of the DNA string having the highest GC content
    - max_GC: float, highest GC content percentage for set of DNA strings
    '''
    results = dict([(label, get_GC(DNA)) for label, DNA in parse_FASTA(data).iteritems()])
    
    max_label = None
    max_GC = 0
    
    for label, result in results.iteritems():
        if (result[1] > max_GC):
            max_label = label
            max_GC = result[1]
            
    return max_label, max_GC
    
def main():    
    with open('datasets/rosalind_gc.txt', 'r') as file:
        data = file.read().rstrip('\n')

    result = map(str, get_max_GC(data))
    
    with open('output/005_GC.txt', 'w') as output:
        output.write('\n'.join(result))
            

if __name__ == "__main__":
    main()