# Finding a shared spliced motif
'''Given two DNA strings in FASTA format, find a longest common
substring of each. (Only one solution is needed)
Link: https://rosalind.info/problems/lcsq/'''

from Bio import SeqIO

def longest_common(input_fasta):
    # open fasta files with SeqIO.parse.seq
    fasta_seqs = list(SeqIO.parse(input_fasta, 'fasta'))
    seq1 = str(fasta_seqs[0].seq)  # AACCTTGG
    seq2 = str(fasta_seqs[1].seq)  # ACACTGTGA    possible: AACTTG, AACTGG
    
    # loop thru seqs, find common bases
    c1 = 0
    c2 = 0
    common_i = 0
    common_substring = ''
    # subseq1 = seq1[c1:]
    # subseq2 = seq2[c2:]
    while (c1 < len(seq1)) and (c2 < len(seq2)):
        if seq1[c1] == seq2[c2]:
            common_substring += seq1[c1]
            c1 += 1
            c2 += 1
            common_i += 1
            print(c1, seq1[c1:], c2, seq2[c2:], common_substring)
        elif (seq1[c1] != seq2[c2]) and (c2 > len(seq2)):
            c2 += 1
            print(c1, seq1[c1:], c2, seq2[c2:], common_substring)
        else:
            c1 += 1
            c2 = common_i
            common_i = c1
            print(c1, seq1[c1:], c2, seq2[c2:], common_substring)
    print(common_substring) # AACTGG len = 6
    

if __name__ == '__main__':
    longest_common('/Users/jakeharris/Desktop/lcsq_example.fasta.txt')