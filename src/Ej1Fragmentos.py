from src.readFasta import readFasta
from src.Ej2Secuencias import reverse_complement

# Marco de lectura
def marcoLectura(seq, n):
    codonParada = ["TAA", "TAG", "TGA"]
    pos = []
    # Marcos de lectura n, válido para cualquier marco de lectura
    for i in range(n, len(seq)-3+1, 3):
        if seq[i:i+3] in codonParada:
            pos.append(i)
    return(pos)

sec = readFasta("../sources/Seq.fasta")
sec_rc = reverse_complement(sec)
print(marcoLectura(sec, 2))
print(marcoLectura(sec_rc, 1))
