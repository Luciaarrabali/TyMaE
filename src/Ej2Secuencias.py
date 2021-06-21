from src.readFasta import readFasta

# Cálculo de la secuencia reversa
def reverse(seq):
    return seq[::-1]

# Cálculo de la secuencia reversa complementaria
def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A',
                  'C': 'G', 'G': 'C'}
    rc = ''
    for base in seq:
        rc += complement[base]
    return ''.join(reversed(rc))
