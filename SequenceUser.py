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