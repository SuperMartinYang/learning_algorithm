# usage: sol_8.py doc1 doc2


# word-frequency vector is computed as follows:
# 1. the specified file is read in
# 2. it is converted into a list of alphanumeric "words"
#    Here a "word" is a sequence of consecutive alphanumeric characters.
#    Non-alphanumeric characters are treated as blanks. Case is not significant.
# 3. for each word, its frequency of occurrence is determined
# 4. the word/frequency lists are sorted into order alphabetically

# the "distance" between two vectors is the angle between them
# if x = (x1, x2, ..., xn) is the first vector (xi = freq of word i)
# and y = (y1, y2, ..., yn) is the second vector
# then the angle between them is defined as:
#    d(x,y) = arccos(inner_product(x,y) / (norm(x)*norm(y)))
# where:
#    inner_product(x,y) = x1*y1 + x2*y2 + ... xn*yn
#    norm(x) = sqrt(inner_product(x,x))

import math
# math.acos(x) is the arccosine of x
# math.sqrt(x) is the square root of x

import string
import sys

##############################
# Op 1: read a text file #####
##############################
def read_file(filename):
    """
    Read the text file with the given filename;
    return a list of the lines of text in the file.
    :param filename:
    :return:
    """
    try:
        f = open(filename, "r")
        return f.read()
    except IOError:
        print("Error opening or reading input file:", filename)
        sys.exit()

##########################################
# Op 2: split the text lines into words ##
##########################################

# global variables needed for fast parsing
# translation table maps upper case to lower case and punctuation to spaces
translation_table = string.maketrans(string.punctuation + string.ascii_uppercase, " " * len(string.punctuation) + string.ascii_lowercase)

def get_words_from_text(text):
    """
    Parse the given list L of text lines into words
    Return list of all words found.
    :param L:
    :return:
    """
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list


##############################################
# Op 3: count frequency of each word #########
##############################################
def count_frequency(word_list):
    """
    Return a list giving pairs of form (word, frequency)
    :param word_list:
    :return:
    """
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D

###########################################################
# Op 4: sort words into alphabetic order ##################
###########################################################
def insertion_sort(A):
    """
    Sort list A into order, in place.
    :param A:
    :return:
    """
    for j in range(len(A)):
        key = A[j]
        # insert A[j] into sorted sequence A[0..j - 1]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

def merge_sort(A):
    """
    Sort list A into order, and return list
    :param A:
    :return:
    """
    n = len(A)
    if n == 1:
        return A
    mid = n // 2
    L = merge_sort(A[:mid])     # sort
    R = merge_sort(A[mid:])
    return merge(L, R)          # merge

def merge(L, R):
    """
    Given two sorted sequences L and R, return their merge.
    :param L:
    :param R:
    :return:
    """
    i = 0
    j = 0
    answer = []
    while i < len(L) and j < len(R):
        if L(i) < R(j):
            answer.append(L(i))
            i += 1
        else:
            answer.append(R(j))
            j += 1
    if i < len(L):
        answer.extend(L[i:])
    if j < len(R):
        answer.extend(R[j:])

    return answer

#################################################
# compute word frequencies for input file #######
#################################################
def word_frequencies_for_file(filename):
    """
    Return alphabetically sorted list of (word, frequency) pairs
    for the given file
    :param filename:
    :return:
    """
    text = read_file(filename)
    word_list = get_words_from_text(text)
    freq_mapping = count_frequency(word_list)

    print("File", filename, " : ")
    print(len(word_list), " words, ")
    print(len(freq_mapping), " distinct words.")

    return freq_mapping

def inner_product(D1, D2):
    """
    Inner product between two vectors, where vectors are
    represented as lists of (word, frequency) pairs.

    Example:
        inner_product([["and",3],["of",2],["the",5]],
                        [["and",4],["in",1],["of",1],["this",2]]) = 14.0
    :param L1:
    :param L2:
    :return:
    """
    product_sum = 0
    for key in D1:
        if key in D2:
            product_sum += D1[key] * D2[key]
    return product_sum

def vector_angle(D1, D2):
    """
    The input is a list of (word, freq) pairs, sorted alphabetically.

    Return the angle between these two vector
    :param L1:
    :param L2:
    :return:
    """
    numerator = inner_product(D1, D2)
    denominator = math.sqrt(inner_product(D1, D1) * inner_product(D2, D2))
    return math.acos(numerator / denominator)

def main():
    if len(sys.argv) != 3:
        print("Usage: sol_1.py filename_1 filename_2")
    else:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        sorted_word_dict1 = word_frequencies_for_file(filename1)
        sorted_word_dict2 = word_frequencies_for_file(filename2)

        distance = vector_angle(sorted_word_dict1, sorted_word_dict2)
        print("The distance between the documents is: %0.6f (radians)" % distance)

if __name__ == '__main__':
    import profile
    profile.run("main()")
