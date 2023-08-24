# Find all locations of a substring motif within a string of DNA
# Note: the problem wants locations, meaning index+1 due to 0-indexing
# Link: https://rosalind.info/problems/subs/

import numpy as np

def motif_locations(dna_file):
    # open full DNA string + motif, remove '\n'
    with open(dna_file) as f:
        dna = f.readline().strip()
        motif = f.readline().strip()
    
    # search thru DNA string for locations of first motif occurences between i:len(dna)
    motif_locs = []
    i = 0
    dna_search = dna[i:]
    while i < len(dna):
        loc = dna_search.find(motif, i, len(dna))
        if loc not in motif_locs:
            motif_locs.append(int(loc) + 1)
            i += 1
        else:
            i += 1
    motif_locs = np.unique(motif_locs)
    motif_locs = [str(m) for m in motif_locs]
    motif_locs.remove('0')
    results = " ".join(motif_locs)

    return results

if __name__ == '__main__':
    print(motif_locations('/Users/jakeharris/Downloads/rosalind_subs (2).txt'))
