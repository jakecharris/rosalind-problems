'''Create FASTA dictionary from given text file in format:
>FASTA_0001
ACATCGATTCGGATC
>FASTA_0002
GGCCTAGCTATCGAT
'''

# Custom class to convert input sequences into useable formats for problems
class SequenceUser:
    def __init__(self, text):
        self.text = text
    
    # convert downloaded FASTA .txt file into Python dict 
    def fasta_dictionary(self):
        fasta_dict = {}
        header = None
        seq_list = []
        with open(self.text, 'r') as f:
            for line in f:
                if line.startswith('>'):    # define headers for each gene
                    if header:  # <- 'None' means that make k:v for new gene
                        fasta_dict[header] = ''.join(seq_list)   # gene header: joined segments within seq_list
                        del seq_list[:]   # empty the seq_list to allow for next gene
                    header = line.strip().split('>')[1]  # create new dict key for gene name
                else:
                    seq_list.append(line.strip())  # add sequence segments to list
            # meant for final gene since there is no last ">" marker
            fasta_dict[header] = ''.join(seq_list)
        return fasta_dict
    
    # translate RNA string into protein
    def mrna_translation(self):
        with open(self.text, 'r') as f:
            seq_list = []
            for line in f:
                seq_list.append(line.strip())
            mrna = ''.join(seq_list)
        aa_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
                    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
                    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
                    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
                    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
                    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
                    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
                    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
                    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
                    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
                    'UAA': '_', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
                    'UAG': '_', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
                    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
                    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
                    'UGA': '_', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
                    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}
        protein = ''
        start = mrna.find('AUG')
        for i in range(start, len(mrna), 3):
            codon = mrna[i:3+i]
            if codon == 'UAG' or codon == 'UAA' or codon == 'UGA':
                break
            else:
                protein += aa_table[codon]
        return protein