# Finding a shared spliced motif
'''Given two DNA strings in FASTA format, find a longest common
subsequence between them. (Only one solution is needed)
Link: https://rosalind.info/problems/lcsq/'''

from Bio import SeqIO

def longest_common_subseq(input_fasta):
    # open fasta files with SeqIO.parse.seq
    fasta_seqs = list(SeqIO.parse(input_fasta, 'fasta'))
    seq1 = str(fasta_seqs[0].seq)  # AACCTTGG
    seq2 = str(fasta_seqs[1].seq)  # ACACTGTGA    possible: AACTTG, AACTGG (len = 6)
    
    # loop thru seqs, find common bases
    c1 = 0
    c2 = 0
    common_substring = ''
    while (c1 < len(seq1)) and (c2 < len(seq2)):
        # if same letters, add to substring, move index window for both
        if seq1[c1] == seq2[c2]:
            common_substring += seq1[c1]
            c1 += 1
            c2 += 1
            # print(c1, seq1[c1:], c2, seq2[c2:], common_substring)
        # if seq1 letter isn't in the remainder of seq2, move seq1 window only
        elif (seq1[c1] != seq2[c2]) and (seq1[c1] not in seq2[c2:]):
            c1 += 1
        # if seq1 & seq2 letters don't match, move seq2 window only
        else:
            c2 += 1
    
    print(common_substring)
    

if __name__ == '__main__':
    longest_common_subseq('/Users/jakeharris/Downloads/rosalind_lcsq (3).txt')