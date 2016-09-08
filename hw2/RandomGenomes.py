from __future__ import division
from __future__ import print_function
import math
import numpy as np


def read_file(file_name):
    """Read a simple file containing two lines. The first line is DNA string. The second line is list of probabilites"""
    with open(file_name) as f:
        content = f.readlines()
    dna = content[0]
    prob_array = np.array(content[1].split())
    prob_array = prob_array.astype(np.float)
    return (dna, prob_array)

def calc_prob(dna, prob_array):
    """Given: A DNA string ss of length at most 100 bp and an array AA containing at most 20 numbers between 0 and 1.
       Return: An array BB having the same length as AA in which B[k]B[k]
       represents the common logarithm of the probability that a random string
       constructed with the GC-content found in A[k]A[k] will match ss exactly."""
    dna_prob= []
    for i in range(len(prob_array)):
        # Each value in the list shows the 2*probability of a character to be A or T in the string
        a_or_t = math.log(prob_array[i]/2, 10)
        c_or_g = math.log((1-prob_array[i])/2, 10)
        dna_prob.append(0)
        for char in dna:
            if char == 'G' or char == 'C':
                dna_prob[i] += a_or_t
            else:
                dna_prob[i] += c_or_g
    return [round(elem, 3) for elem in dna_prob]


"""Main"""
dna, prob_array = read_file('rosalind_prob.txt')
dna_prob = calc_prob(dna, prob_array)
for prob in dna_prob:
    print(prob, end=" ", flush=True)
print()