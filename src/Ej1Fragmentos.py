from src.readFasta import readFasta
from src.Ej2Secuencias import reverse_complement

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

sec = readFasta("../sources/Seq.fasta")
sec_rc = reverse_complement(sec)

for n in [0,1,2]:
    print(f"Distancias para +{n+1}F:\n{distancia(marcoLectura(sec, n))}")
    print(f"Distancias para -{n+1}R:\n{distancia(marcoLectura(sec_rc, n))}")
