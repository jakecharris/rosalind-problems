# Transcribe a string of DNA into its corresponding RNA string (replace 'T' for 'U')
# Link: https://rosalind.info/problems/rna/

def dna_to_rna(dna_file):
    # open downloaded file
    with open(dna_file, 'r') as f:
        dna = f.read()
    
    # replace each thymine ('T') in DNA coding strand for mRNA uracil ('U')
    rna = dna.replace('T', 'U')
    print(rna)

if __name__ == '__main__':
    dna_to_rna('/Users/jakeharris/Downloads/rosalind_rna (1).txt')
