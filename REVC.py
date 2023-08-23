# Given a DNA string, find its reverse complement (reverse of the string and then its complementing bases)
# Link: https://rosalind.info/problems/revc/

def rev_complement(dna_file):
    # open downloaded file
    with open(dna_file, 'r') as f:
        dna = f.read()
    rev_dna = dna[::-1] # reverse of original DNA strand
    
    # create reverse complement strand based on base pairing
    rev_comp = ''
    for base in rev_dna:
        if base == 'A':
            rev_comp = rev_comp + 'T'
        if base == 'T':
            rev_comp = rev_comp + 'A'
        if base == 'G':
            rev_comp = rev_comp + 'C'
        if base == 'C':
            rev_comp = rev_comp + 'G'

    print(rev_comp)

if __name__ == '__main__':
    print(rev_complement('/Users/jakeharris/Downloads/rosalind_revc (1).txt'))