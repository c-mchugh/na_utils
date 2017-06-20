"""
Convert DNA sequences to RNA sequences
"""

def rna(seq):
    """ convert DNA to RNA """

    # determine if original sequence is upper case

    seq_upper = seq.isupper()

    # convert to lower case

    seq = seq.lower()

    # swap out T for U

    seq = seq.replace("t","u")

    # return upper or lower, depending on input
    if seq_upper:
        return seq.upper()
    else:
        return seq


def reverse_rna_complement(seq):
    """ convert a DNA sequence to its RNA reverse complement sequence """

    # determine if original sequence was uppercase
    seq_upper = seq.isupper()

    # reverse sequence
    seq = seq[::-1]

    # convert to uppercase
    seq = seq.upper()

    # compute complement
    seq = seq.replace("A", "u")
    seq = seq.replace("T", "a")
    seq = seq.replace("G", "c")
    seq = seq.replace("C", "g")

    # return in appropriate case
    if seq_upper:
        return seq.upper()

    else:
        return seq
