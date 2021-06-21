# Leer un archivo FASTA
def readFasta(FASTA):
    f = open(FASTA, "r")
    lines = f.readlines()
    seq = ""

    for i in lines:
        if ">>" in i:
            pass
        else:
            seq += i.strip()
    return(seq)