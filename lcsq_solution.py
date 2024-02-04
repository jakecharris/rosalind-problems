# Example solution to longest common subsequence
# Link: https://saradoesbioinformatics.blogspot.com/2016/08/finding-shared-spliced-motif.html

from Bio import SeqIO

def longest_common_subseq(input_fasta):
    # open fasta files with SeqIO.parse.seq
    fasta_seqs = list(SeqIO.parse(input_fasta, 'fasta'))
    s = str(fasta_seqs[0].seq)  # AACCTTGG
    t = str(fasta_seqs[1].seq)  # ACACTGTGA    possible: AACTTG, AACTGG (len = 6)
    
    # create array of len(s) containing arrays of len(t) filled with zeros
    lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    # enumerate thru lengths array of zeros (index, char)
    for i, x in enumerate(s):
        for j, y in enumerate(t):
            # if letters (x, y) are same, add 1 to index of next index within sub-array
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            # ekse, set the rest of index values in sub-array to max value of previous/current sub-array
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])
    # print(lengths)

    # loop thru len of seqs s & t until len of either == 0
    spliced_motif = ''
    x, y = len(s), len(t)
    while x * y != 0:
        # if (array x, index y) == (array x-1, index y), move to previous array x 
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        # elif (array x, index y) == (array x, index y-1), move to previous index y
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        # else, add letter to spliced_motif from index [array x - 1]
        else:
            spliced_motif = s[x - 1] + spliced_motif
            x -= 1
            y -= 1
        print(f'x={x}, y={y}, spliced_motif={spliced_motif}')
    print(spliced_motif)
    
    
if __name__ == '__main__':
    longest_common_subseq('/Users/jakeharris/Downloads/rosalind_lcsq (4).txt')
    