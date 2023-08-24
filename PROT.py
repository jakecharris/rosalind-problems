# Translate an mRNA string into a protein string based on codons
# Link: https://rosalind.info/problems/prot/

# Import SeqUser tool 
from SequenceUser import *

def mrna_translation(rna_file):
    
    # open mRNA sequence file, translate into protein
    mrna = SequenceUser(rna_file)
    protein = mrna.mrna_translation()
    return protein


if __name__ == '__main__':
    print(mrna_translation('/Users/jakeharris/Downloads/rosalind_prot.txt'))