#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    return len(string) == len(set(string.lower()))

#__________
#Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.


# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square



import math


def find_next_square(sq):
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1
#__________

# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    return s.lower().count('x') == s.lower().count('o')

# Other good solutions:
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

def xo(s):
    return True if s.lower().count('x') == s.lower().count('o') else False

#__________
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]


def remove_smallest(numbers):
    a = numbers[:] #<--- taking a copy of the array; see note below :)
    if a:
        a.remove(min(a))
    return a

# !!!!!!! The [:] makes a shallow copy of the array, hence allowing you to modify your copy without damaging the original.

# The reason this also works for strings is that in Python, Strings are arrays of bytes representing Unicode characters. !!!!!!!!!!!

#_______________
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    return string.endswith(ending)

#__________
# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

def stray(arr):
    return [num for num in arr if arr.count(num) == 1][0]
#__________
# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# Examples (input --> output):
# "4556364607935616" --> "############5616"
#      "64607935616" -->      "#######5616"
#                "1" -->                "1"
#                 "" -->                 ""


def maskify(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]

#Or

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
#__________
#Given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.

def find_short(s):
    l = map(len, s.split())
    return min(l)

#other solutions that would've worked:

def find_short(s):
    return min(len(x) for x in s.split())

#or

def find_short(s):
    return min(map(len, s.split(' ')))
#__________
# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]

def friend(x):
    return[n for n in x if len(n) == 4]

#__________
# DropCaps means that the first letter of the starting word of the paragraph should be in caps and the remaining lowercase, just like you see in the newspaper.

# But for a change, let"s do that for each and every word of the given String. Your task is to capitalize every word that has length greater than 2, leaving smaller words as they are.

# *should work also on Leading and Trailing Spaces and caps.

# "apple"            => "Apple"
# "apple of banana"  => "Apple of Banana"
# "one   space"      => "One   Space"
# "   space WALK   " => "   Space Walk   " 


def drop_cap(str_):
    return ' '.join( w.capitalize() if len(w) > 2 else w for w in str_.split(' ') )


#__________
# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"


def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

#__________
# In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)

#or

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))


#-----------------------


# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]


def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]

#or

def number(lines):
    return [f"{i}: {j}" for i,j in enumerate(lines,1)] 

#-----------------

# The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age,  oldest age].

# The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

# For example (Input --> Output):

# [1, 2, 10, 8] --> [8, 10]
# [1, 5, 87, 45, 8, 8] --> [45, 87]
# [1, 3, 10, 0]) --> [3, 10]

def two_oldest_ages(ages):
    return sorted(ages)[-2:]

#or

def two_oldest_ages(ages):
    max_number = max(ages)
    ages.remove(max_number)
    return [max(ages), max_number]

#-----------------

# Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

# For example, if this array were passed as an argument:

# ["Telescopes", "Glasses", "Eyes", "Monocles"]

# Your function would return the following array:

# ["Eyes", "Glasses", "Monocles", "Telescopes"]

# All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the same length.

def sort_by_length(arr):
    arr.sort(key = len)
    return arr 

#:)

#-----------------

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    a = "".join(map(str, n[0:3]) )
    b = "".join(map(str, n[3:6]) )
    c = "".join(map(str, n[6:10]) )
    return "("+a+") "+ b +"-"+c 

#OR

def create_phone_number(n):
    a = "".join(map(str, n[0:3]) )
    b = "".join(map(str, n[3:6]) )
    c = "".join(map(str, n[6:10]) )
    return "("+a+") "+ b +"-"+c 

#-----------------

# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

# The string has the following conditions to be alphanumeric:

# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore.

def alphanumeric(string):
    return string.isalnum()

#______________

# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    # The function code should be here
    return {c:s.count(c) for c in s}

#_____________________
# Your task, is to create N×N multiplication table, of size provided in parameter.

# For example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:

# [[1,2,3],[2,4,6],[3,6,9]]
def multiplication_table(size):

    result = []
    for i in range (1,size+1):
        result.append([(j * i) for j in range(1, size+1)])
    return result

#or

def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]

#_____________________

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

def alphabet_position(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())

#_____________________

# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

def encrypt_this(text):
    result = []
    
    for word in text.split():
        # turn word into a list
        word = list(word)
        
        # replace first letter with ascii code
        word[0] = str(ord(word[0]))
        
        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        
        # add to results
        result.append(''.join(word))
    
    return ' '.join(result)

#_____________________