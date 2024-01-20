# Enumerating k-mers lexicographically
'''Given a collection of symbols from the alphabet and an integer n<=10,
Return all ordered strings of length n that can be formed from the alphabet.
Link: https://rosalind.info/problems/lexf/'''

def ordered_letters(input_file):
    # open letters string + num, remove spaces, sort letters
    with open(input_file) as f:
        letters = f.readline().strip().replace(' ', '')
        letters = sorted(letters)
        n = int(f.readline().strip())
    output = []
    for i in range(len(letters)):
        for j in range(len(letters)):
            output.append(letters[i] + letters[j])
    with open('/Users/jakeharris/Desktop/lexf_output.txt', 'w') as output_file:
        output_file.writelines(line + '\n' for line in output)
    # for i in output:
    #     print(i)


ordered_letters('/Users/jakeharris/Downloads/rosalind_lexf (2).txt')