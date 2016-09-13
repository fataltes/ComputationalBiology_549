from __future__ import print_function


def read_file(file_name):
    """
    Read a simple file containing two lines.
    The first line is the string length.
    The second line is list of integer numbers
    :param file_name:
    :return: list of integer numbers and its length
    """
    with open(file_name) as f:
        content = f.readlines()
    length = int(content[0])
    seq = [int(s) for s in content[1].split(" ")]
    return (length, seq)


def longest_inc_dec_subseq(length, seq, increasing=True):
    """
    :param length: length of the sequence
    :param seq: sequence of integers
    :param increasing: weather we want the maximum increasing subsequence or maximum decreasing subsequence
    :return: maximum increasing/decreasing subsequence of the input sequence
    """
    subseqs = []
    for i in range(length):
        # assume the longest subseq that supports our condition is the current integer itself
        max_subseq = [seq[i]]
        for subseq in subseqs:
            # Compare last integer in each subsequence with the current integer
            last_idx = len(subseq) - 1
            if (increasing and seq[i] >= subseq[last_idx]) or (not increasing and seq[i] <= subseq[last_idx]):
                new_subseq = subseq + [seq[i]]
                # In each iteration find the maximum subsequence generated with any of the current subsequences
                # plus the current integer in sequence
                if len(max_subseq) < len(new_subseq):
                    max_subseq = new_subseq
        subseqs += [max_subseq]

    # find the maximum subseq out of all subsequences that were generated in previous section
    max_subseq = []
    max_len = 0
    for subseq in subseqs:
        if max_len < len(subseq):
            max_len = len(subseq)
            max_subseq = subseq
    return max_subseq


"""Main"""
length, seq = read_file("rosalind_max_inc_dec_subseq.txt")
max_subseq = longest_inc_dec_subseq(length, seq, True)
print("Longest increasing subsequence:")
for char in max_subseq:
    print(char, end=" ")
print("\n")
print("Longest decreasing subsequence:")
max_subseq = longest_inc_dec_subseq(length, seq, False)
for char in max_subseq:
    print(char, end=" ")
