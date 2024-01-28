# k-Mer Composition
'''For an integer k=4, order all posible k-mers of a DNA string in FASTA
format lexicographically in an array A where A[m] is the number of times
that the mth k-mer appears in the DNA string.
Link: https://rosalind.info/problems/kmer/'''

from itertools import product
import regex as re
import numpy as np

def kmer_composition(input_file, k):
    
    # create k-mer combinations of DNA bases
    bases = 'ACGT'
    kmers = [''.join(b) for b in product(bases, repeat=k)]
    
    # open downloaded FASTA sequences
    with open(input_file) as f:
        dna_lines = f.readlines()[1:]
        # dna_lines_split = dna_lines.split()
        dna = ''.join([l.strip() for l in dna_lines])
    
    # parse thru each kmer in DNA & count overlapping occurences of each kmer
    v = 0  # initial count values
    kmer_dict = {k:v for k in kmers}
    for i in kmers:
        kmer_count = len(re.findall(i, dna, overlapped=True))
        kmer_dict[i] = kmer_count
    count_array = np.array(list(kmer_dict.values()))
    
    return count_array

if __name__ == '__main__':
    print(kmer_composition('/Users/jakeharris/Downloads/rosalind_kmer.txt', 4))