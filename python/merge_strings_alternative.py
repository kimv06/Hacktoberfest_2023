# Title: 1768. Merge Strings Alternately
# Difficulty: Easy
# Problem: https://leetcode.com/problems/merge-strings-alternately/
# Description: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.


def mergeAlternately( word1: str, word2: str) -> str:
    #testcase for this function
    """
    >>> mergeAlternately("abc","pqr")
    'apbqcr'
    >>> mergeAlternately("ab","pqrs")
    'apbqrs'
    >>> mergeAlternately("abcd","pq")
    'apbqcd'
    """

    # Find the maximum length of two words.
    maxLen=max(len(word1),len(word2))
    output=""

    # Iterate through the loop a maximum of 'maxLen' times.
    for i in range(maxLen):
        # Check if the current index is within the length of word1.
        if i < len(word1): 
            output += word1[i] # Append the 'i'th character from word1.
        # Check if the current index is within the length of word2.
        if i < len(word2):  
            output += word2[i] # Append the character from word2.
    return output

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    result = mergeAlternately("abcd","pqrs")
    print(result)