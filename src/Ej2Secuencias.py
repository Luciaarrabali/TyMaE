from src.readFasta import readFasta

# Cálculo de secuencias
def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A',
                  'C': 'G', 'G': 'C'}
    rc = ''
    for base in seq:
        rc += complement[base]
    return ''.join(reversed(rc))
