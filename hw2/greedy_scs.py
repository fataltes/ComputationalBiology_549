from __future__ import division
from __future__ import print_function

"""
Question:
Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
"""

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

def merge_strs(str1, str2, l):
    """
    :param str1: the first string
    :param str2: the second string
    :param l: length of overlap
    :return: merged string if exists
    """
    if len(str1) < l or len(str2) < l:
        return ""
    if str1[0:l] == str2[len(str2)-l:len(str2)]:
        return str2[0:len(str2)-l] + str1
    if str2[0:l] == str1[len(str1)-l:len(str1)]:
        return str1[0:len(str1)-l] + str2
    return ""

def find_and_merge_strs(dnas, l):
    for i in range(len(dnas)-1):
        for j in range(i+1, len(dnas)):
            merged_str = merge_strs(dnas[i], dnas[j], l)
            if merged_str != "":
                return (merged_str, i, j)
    return ("", 0, 0)


"""Main"""
names, dnas = read_file('rosalind_greedy_scs.txt')
max_len = 0
for dna in dnas:
    if len(dna) > max_len:
        max_len = len(dna)

l = max_len - 1
while len(dnas) > 1 and l > 0:
    # in each round find two strings that have a common substring of size l and return the merged superstring of them
    merged_str, i, j = find_and_merge_strs(dnas, l)
    # if couldn't find any two strings to merge, decrease l by one
    if merged_str == "":
        l -= 1
    # replace the merged string instead of its two substrings
    else:
        first_to_be_removed = dnas[i]
        second_to_be_removed = dnas[j]
        dnas.remove(first_to_be_removed)
        dnas.remove(second_to_be_removed)
        dnas.append(merged_str)


# if we just have 1 final superstring in our list everything is fine, other than that there is either an error,
# or the condition is not satisfied.
if len(dnas) == 1:
    print(dnas[0])
else:
    print("ERROR")
