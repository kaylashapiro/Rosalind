#!/usr/bin/env python

'''
Transcribing DNA into RNA
'''

def dna_to_rna(data):  
    '''
    Transcribe a DNA string into an RNA string.
    
    Input:
    - data: string of DNA nucleotides
    
    Output:
    - RNA: string of RNA nucleotides
    '''
    RNA = data.replace('T', 'U')
    
    return RNA

def main():

    with open('datasets/rosalind_rna.txt', 'r') as file:
        data = file.read().rstrip('\n')
        
    RNA = dna_to_rna(data)
            
    with open('output/002_RNA.txt', 'w') as output:
        output.write(RNA)


if __name__ == '__main__':
    main()