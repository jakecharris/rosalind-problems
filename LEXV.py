# Ordering strings of different lengths lexicographically
'''Given a set of alphabet and an integer n<=4, return a set 
of all strings of up to length n ordered lexicogrpahically.
Link: https://rosalind.info/problems/lexv/'''

from itertools import product, chain
from operator import itemgetter

def custom_order(s):
    return ['D', 'N', 'A']

def ordered_strings(input_file):
    
    # open file with alphabet & n
    with open(input_file) as f:
        input = f.readlines()
        alphabet = input[0].replace(' ', '').rstrip()  # custom lexi. alphabet order
        n = int(input[1].strip())
    print(alphabet, n)
    
    # loop thru n value, add letter combos
    i = 1
    combos = []
    while i <= n:
        combos.append([''.join(l) for l in product(alphabet, repeat=i)])
        i += 1
    combos = list(chain.from_iterable(combos))  # melt list of list into one list of combos
    lexi_combos = sorted(combos, key=lambda word: [alphabet.index(c) for c in word])  # key returns sorted index from custom alphabet
    
    # write to file 
    with open('/Users/jakeharris/Desktop/lexv_output.txt', 'w') as output_file:
        output_file.writelines(line + '\n' for line in lexi_combos)

if __name__ == '__main__':
    ordered_strings('/Users/jakeharris/Downloads/rosalind_lexv.txt')