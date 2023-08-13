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


# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

def stray(arr):
    return [num for num in arr if arr.count(num) == 1][0]

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