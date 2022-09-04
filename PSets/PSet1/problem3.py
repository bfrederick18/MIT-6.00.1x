"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""
s = 'abcbcd'

# Paste your code into this box 
def longest_sub(string):
    for i in range(len(string)):
        for j in range(i + 1):
            sub = string[j:j+len(string) - i]
            if sub == ''.join(sorted(sub)):  # If the substring is equal to its sorted version (meaning sub is sorted)
                return sub

print('Longest substring in alphabetical order is:', longest_sub(s))