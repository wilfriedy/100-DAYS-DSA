unique = {'AAAA'}
dna  = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
unique.add(dna[1:10+1])
unique.add('AAAA')
print('AAAAs'in unique)
print(len(dna))