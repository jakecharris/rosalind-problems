# k-Mer Composition
'''For an integer k=4, order all posible k-mers of a DNA string in FASTA
format lexicographically in an array A where A[m] is the number of times
that the mth k-mer appears in the DNA string.
Link: https://rosalind.info/problems/kmer/'''

# from SequenceUser import fasta_dictionary
import itertools

def kmer_composition(k):
    
    # create k-mer combinations of DNA bases
    bases = 'ACGT'
    kmers = [''.join(b) for b in itertools.product(bases, repeat=k)]
    v = 0  # initial value
    kmer_counts = {k:v for k in kmers}
    # print(kmer_counts)
    
    # open downloaded FASTA sequences into Python dict 
    # fasta_dict = SequenceUser(fasta_file)
    # fasta_dict = fasta_dict.fasta_dictionary()
    # dna_seq = str(fasta_dictionary.items()[0])
    
    # # parse thru dna_seq in segments of len(k) & count occurences of each kmer
    # for j in kmers:
    #     dna_seq.count()
    # kmer_counts = 

if __name__ == '__main__':
    kmer_composition(2)