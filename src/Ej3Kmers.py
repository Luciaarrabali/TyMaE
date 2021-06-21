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
    kmer = compute_relative()

if __name__ == "__main__":
    main()