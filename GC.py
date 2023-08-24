# From a given set of FASTA sequences, find the sequence with the highest GC content.
# Link: https://rosalind.info/problems/gc/

# Import sequence conversion module 
from SequenceUser import *

def highest_gc_content(fasta_file):
    
    # convert downloaded FASTA sequences into Python dict 
    fasta_dict = SequenceUser(fasta_file)
    fasta_dict = fasta_dict.fasta_dictionary()
    
    # Find gene with highest GC content
    highest_gc_gene = ''
    highest_gc_content = 0
    for (header, seq) in fasta_dict.items():
        gc_content = round(((seq.count('G') + seq.count('C')) / len(seq) * 100), 4)
        if gc_content > highest_gc_content:
            highest_gc_gene = header
            highest_gc_content = gc_content
        else:
            continue
    return highest_gc_gene, highest_gc_content


if __name__ == '__main__':
    print(highest_gc_content('/Users/jakeharris/Downloads/rosalind_gc.txt'))
