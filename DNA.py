# Given a DNA string, return the numbers of A, C, G, T bases, respectively.
# Link: https://rosalind.info/problems/dna/

def count_dna_bases(dna_file):
    # open downloaded file
    with open(dna_file, 'r') as f:
        dna = f.read()
    # count number of occurences of each base in DNA file
    base_counts = {'A':0, 'C':0, 'G':0, 'T':0}
    for base in base_counts.keys():
        base_counts[base] = dna.count(base)

    print(base_counts) 

if __name__ == '__main__':
    count_dna_bases('/Users/jakeharris/Downloads/rosalind_ini.txt')