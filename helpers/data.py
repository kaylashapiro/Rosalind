#!/usr/bin/env python

def parse_FASTA(data):
    '''
    Returns a dictionary with FASTA label keys and DNA string values.
    
    Input:
    - data: DNA strings given in FASTA format
    
    Output:
    - results: dictionary of (key, value) pairs with
               key = string, FASTA label
               value = string, DNA
    '''
    results = {}
    
    lines = data.split('>')
    
    for line in lines:
        if line == '':
            continue
        
        fasta = line.strip().split('\n', 1)
        label = fasta[0]
        DNA = fasta[1].replace('\n','')
        
        results[label] = DNA
    
    return results