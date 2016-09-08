## Inspired by "https://www.biostars.org/p/2903/"
from __future__ import print_function
import numpy as np

map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}


def translate_rna2protein(rna):
    """
    :param rna: An RNA string ss corresponding to a strand of mRNA (of length at most 10 kbp).
        read from a mRNA.txt file in the same directory as this code
        Print: The protein string encoded by ss.
    :return: None
    """
    rng = np.arange(0, len(rna), 3)
    for i in rng:
        protein_base = map[rna[i: i+3]]
        if protein_base == "STOP":
            break
        print(protein_base, end="")


"""Main"""
with open("mRNA.txt") as file:
    rna = file.readlines()
    translate_rna2protein(rna[0].strip())