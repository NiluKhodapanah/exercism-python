def to_rna(dna_strand):
    rna = ""
    for nuc in dna_strand:
        if nuc == "G":
            rna += "C"
        elif nuc == "C":
            rna += "G"
        elif nuc == "A":
            rna += "U"
        else:
            rna += "A"
    return rna

print(to_rna("ACGTGGTCTTAA"))