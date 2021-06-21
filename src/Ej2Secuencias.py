from readFasta import readFasta
import sys

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

if __name__ == "__main__":
    sec = readFasta(sys.argv[1])
    print("Secuencia reversa:\n" + reverse(sec) + "\n")
    print("Secuencia reversa complementaria:\n" + reverse_complement(sec))
