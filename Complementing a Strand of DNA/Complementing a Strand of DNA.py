import fileinput
bases_pair_table = {'A':'T',
              'C':'G',
              'T':'A',
              'G':'C'}
reverse_complement = ''
lines = [line.strip() for line in fileinput.input('rosalind_revc.txt')]
for base_string in lines:
    reversed_base_string = base_string[::-1]
    for base in reversed_base_string:
        reverse_complement =  reverse_complement + bases_pair_table[base]
print(reverse_complement)
        
    
