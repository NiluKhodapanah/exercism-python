def distance(strand_a, strand_b):
    diff = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        for nt_a, nt_b in zip(strand_a, strand_b):
            if nt_a != nt_b:
                diff += 1
        return diff
