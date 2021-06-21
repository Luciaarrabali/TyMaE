from readFasta import readFasta
import sys

path = sys.argv[1]
k = sys.argv[2]

def kmers(seq, k):
    kmer = {}
    length = len(seq)

    for i in range(length-k+1):
        numKmers = seq[i:i+k]
        if numKmers not in kmer:
            kmer[numKmers] = 1
        else:
            kmer[numKmers] += 1
    kmer = kmer_relative(kmer, length, k)

def kmer_relative(kmer, sequence_length, k):
    for count in kmer:
        n = kmer[count]
        kmer[count] = (n, round(n/(sequence_length-k+1), 6))
    return kmer

if __name__ == "__main__":
    main()