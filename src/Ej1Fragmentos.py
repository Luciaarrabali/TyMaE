from readFasta import readFasta
from Ej2Secuencias import reverse_complement
import sys

# Marco de lectura
def marcoLectura(seq, n):
    codonParada = ["TAA", "TAG", "TGA"]
    pos = [n]
    # Marcos de lectura n, válido para cualquier marco de lectura
    for i in range(n, len(seq)-3+1, 3):
        if seq[i:i+3] in codonParada:
            pos.append(i)
    pos.append(len(seq))
    return(pos)

def distancia(pos):
    distancias = []
    for i in range(len(pos)-1):
        long = pos[i+1] - pos[i]
        distancias.append(long)
    return distancias

if __name__ == "__main__":
    sec = readFasta(sys.argv[1])
    sec_rc = reverse_complement(sec)

    for n in [0,1,2]:
        print(f"Distancias para +{n+1}F:\n{distancia(marcoLectura(sec, n))}")
        print(f"Distancias para -{n+1}R:\n{distancia(marcoLectura(sec_rc, n))}")
