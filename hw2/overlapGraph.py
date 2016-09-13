from __future__ import division
from __future__ import print_function

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

def create_overlapGraph(names, dnas):
    """
    :param names: a collection of names assigned to DNA strings in the same order
    :param dnas: a collection of DNA strings
    :return: The adjacency list corresponding to O3 (3 matches of suffix and prefix).
    """
    overlap_graph = []
    for i in range(len(dnas)):
        for j in range(i+1, len(dnas)):
            if dnas[i][0] == dnas[j][len(dnas[j])-3] and \
                dnas[i][1] == dnas[j][len(dnas[j]) - 2] and \
                    dnas[i][2] == dnas[j][len(dnas[j]) - 1]:
                overlap_graph.append((names[j], names[i]))
            if dnas[i][len(dnas[i]) - 3] == dnas[j][0] and \
                dnas[i][len(dnas[i]) - 2] == dnas[j][1] and \
                    dnas[i][len(dnas[i]) - 1] == dnas[j][2]:
                overlap_graph.append((names[i], names[j]))
    return overlap_graph



"""Main"""
names, dnas = read_file('rosalind_graph.txt')
graph = create_overlapGraph(names, dnas)
for edge in graph:
    print(edge[0], end=" ")
    print(edge[1])
print()