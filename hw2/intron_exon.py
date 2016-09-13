from __future__ import division
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


def read_file(file_name):
    """
    Reads a file containing a collection of DNA strings in FASTA format having total length at most 10 kbp
    and returns DNA strings and their corresponding name in two separate lists
    :param file_name
    :return: a tuple of name list and DNA list
    """
    with open(file_name) as f:
        content = f.readlines()
    names = []
    dnas = []
    dna = ""
    name = ""
    for line in content:
        line = line.strip()
        if line[0] == ">":
            names.append(name)
            dnas.append(dna)
            name = line[1:]
            dna = ""
        else:
            dna += line
    names.append(name)
    dnas.append(dna)
    return (names[1:], dnas[1:])

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

def transcribe_dna2rna(dna, introns):
    exon = ""
    i = 0
    skip = 0
    while i < len(dna):
        skip = 0
        for intron in introns:
            j = 0
            while j < len(intron) and i+j < len(dna) and dna[i+j] == intron[j]:
                j+=1
            if j == len(intron):
                skip = max(skip, len(intron))
        if skip:
            i+=(skip)
        else:
            exon += dna[i].replace('T', 'U')
            i+=1
    return exon


"""Main"""
names, dnas = read_file('rosalind_intron_exon.txt')
rna = transcribe_dna2rna(dnas[0], dnas[1:])
#print(rna)
protein = translate_rna2protein(rna)
