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

#______________________

# fruit = "Apple"
# print(fruit[1:-1])

# prints: ppl starting with the first letter 1 => 'p' then ending with the -1 letter "e" 

# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# So 1, 2, 2 will be 1^2 + 2^2 + 2^2 = 9

def square_sum(numbers):
    return sum([num*num for num in numbers])

# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"
  
#______________________
  
#   While making a game, your partner, Greg, decided to create a function to check if the user is still alive called checkAlive/CheckAlive/check_alive. Unfortunately, Greg made some errors while creating the function.

# checkAlive/CheckAlive/check_alive should return true if the player's health is greater than 0 or false if it is 0 or below.

# The function receives one parameter health which will always be a whole number between -10 and 10.

def check_alive(health):
    if health <= 0:
        return False
    else:
        return True
    
#______________________

# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

#or

def positive_sum(arr):
    sum = 0
    for x in arr:
        if x > 0:
            sum = sum + x
    return sum

#______________________

# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

# For example:

# a = 1
# b = 4
# --> [1, 2, 3, 4]

def between(a,b):
    l = []
    for v in range(a,b + 1):
        l.append(v):
    return l

#______________________

# Complete the function which converts a binary number (given as a string) to a decimal number.

# You use the built-int() function, and pass it the base of the input number, i.e. 2 for a binary number:

def bin_to_decimal(inp):
    return int(inp, 2)

#______________________

# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0

def make_negative( number ):
    return -abs(number)


#OR

def make_negative( number ):
    if number < 0:
        return number
    else:
        return -number
    
#______________________

# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

def find_difference(a, b):
    nums = 1
    numss = 1
    for i in a:
        nums = nums * i
    for j in b:
        numss = numss * j
    return int(abs(nums - numss))

#______________________

# Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.

def merge_arrays(a, b): 
    return sorted(set(a + b))

# OR

def merge_arrays(first, second): 
    working = []
    for e in first:
        if e not in working:
            working.append(e)
    for i in second:
        if i not in working:
            working.append(i)

#______________________

# Write a function that accepts two numbers a and b and returns whether a is smaller than, bigger than, or equal to b, as a string.

# (5, 4)   ---> "5 is greater than 4"
# (-4, -7) ---> "-4 is greater than -7"
# (2, 2)   ---> "2 is equal to 2"
# There is only one problem...

# You cannot use if statements, and you cannot use the ternary operator ? :.

# In fact the word if and the character ? are not allowed in your code.

def no_ifs_no_buts(a, b):
    return {
        a == b: str(a) + " is equal to " + str(b),
        a < b: str(a) + " is smaller than " + str(b),
        a > b: str(a) + " is greater than " + str(b),
    }[True]

#______________________

# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.



def findSmallestInt(arr):
    return min(arr)

#______________________

# I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

# P.S. Each array includes only integer numbers. Output is a number too.

def array_plus_array(arr1,arr2):
    num = sum(arr1) + sum(arr2)
    return(num)

#______________________

# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?

# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

def function(num):
    return str(num)
#______________________

# Nickname Generator

# Write a function, nicknameGenerator that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.

# If the 3rd letter is a consonant, return the first 3 letters.

# nickname("Robert") //=> "Rob"
# nickname("Kimberly") //=> "Kim"
# nickname("Samantha") //=> "Sam"
# If the 3rd letter is a vowel, return the first 4 letters.

# nickname("Jeannie") //=> "Jean"
# nickname("Douglas") //=> "Doug"
# nickname("Gregory") //=> "Greg"
# If the string is less than 4 characters, return "Error: Name too short".


def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    elif name[2] not in 'aeiou': 
        return name[:3]
    elif name[2] in 'aeiou':
        return name[:4]
    
#______________________

# Colour plays an important role in our lifes. Most of us like this colour better then another. User experience specialists believe that certain colours have certain psychological meanings for us.

# You are given a 2D array, composed of a colour and its 'common' association in each array element. The function you will write needs to return the colour as 'key' and association as its 'value'.

# For example:

# var array = [["white", "goodness"], ...] returns [{'white': 'goodness'}, ...]

def colour_association(arr):
    return [{i[0] : i[1]} for i in arr]

#______________________

# You are the greatest chef on earth. No one boils eggs like you! Your restaurant is always full of guests, who love your boiled eggs. But when there is a greater order of boiled eggs, you need some time, because you have only one pot for your job. How much time do you need?

# Your Task
# Implement a function, which takes a non-negative integer, representing the number of eggs to boil. It must return the time in minutes (integer), which it takes to have all the eggs boiled.

# Rules
# you can put at most 8 eggs into the pot at once
# it takes 5 minutes to boil an egg
# we assume, that the water is boiling all the time (no time to heat up)
# for simplicity we also don't consider the time it takes to put eggs into the pot or get them out of it

import math

def cooking_time(eggs):
    time = 5
    eggz = 8
    return math.ceil(eggs/eggz)*time

#OR

def cooking_time(eggs):
    t = 0
    while( eggs > 0 ):
        t += 5
        eggs -= 8
    
    return t

#______________________

# Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language) of strictly positive integers, and the reduced fraction must be returned as an array/tuple:

# input:   [numerator, denominator]
# output:  [reduced numerator, reduced denominator]
# example: [45, 120] --> [3, 8]
# All numerators and denominators will be positive integers.

from fractions import Fraction
def reduce_fraction(fraction):
    t = Fraction(*fraction)
    return (t.numerator, t.denominator)

#______________

# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]

#______________

# The function is not returning the correct values. Can you figure out why?

# Example (Input --> Output ):

# 3 --> "Earth"

def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name

# Work out what number day of the year it is.

# toDayOfYear([1, 1, 2000]) => 1
# The argument passed into the function is an array with the format [D, M, YYYY], e.g. [1, 2, 2000] for February 1st, 2000 or [22, 12, 1999] for December 22nd, 1999.

# Don't forget to check for whether it's a leap year! Three criteria must be taken into account to identify leap years:

# The year can be evenly divided by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.

def to_day_of_year(date):
    # Define the number of days in each month, accounting for leap years
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day, month, year = date

    # Check if it's a leap year and update February's days
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        days_in_month[2] = 29

    # Calculate the day of the year
    day_of_year = sum(days_in_month[:month]) + day

    return day_of_year


# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]


def greet(name):
    return "Hello, " + name + " how are you doing today?"

# Two players - "black" and "white" are playing a game. The game consists of several rounds. If a player wins in a round, he is to move again during the next round. If a player loses a round, it's the other player who moves on the next round. Given whose turn it was on the previous round and whether he won, determine whose turn it is on the next round.

# Input/Output
# [input] string lastPlayer/$last_player

# "black" or "white" - whose move it was during the previous round.

# [input] boolean win/$win

# true if the player who made a move during the previous round won, false otherwise.

# [output] a string

# Return "white" if white is to move on the next round, and "black" otherwise.

# Example
# For lastPlayer = "black" and win = false, the output should be "white".

# For lastPlayer = "white" and win = true, the output should be "white".

def whose_move(last_player, win):
    ... # Your Move...
    if last_player == "black" and win == False:
        return "white"
    elif last_player == "black" and win == True:
        return "black"
    elif last_player == "white" and win == False:
        return "black"
    elif last_player == "white" and win == True:
        return "white"
    
# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

# Return true if yes, false otherwise :)   

def hero(bullets, dragons):
  bulletsNeeded = dragons * 2;
  if bullets >= bulletsNeeded:
    return True;
  else:
    return False;

# OR

def hero(bullets, dragons):
    return bullets >= dragons * 2

# OR

def hero(bullets, dragons):
    return dragons <= bullets / 2

# Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes

# Task
# Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return johns age is 34

class Person:
    def __init__(self, name,age):
        self.info = "{}s age is {}".format(name, age)

#OR

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f'{name}s age is {age}'

#OR

class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


# Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.

def merge_arrays(first, second): 
    return sorted(set(first + second))

# It checks the char in the given string from the front with an iteration, in the iteration it does these steps:

# There is a flag and it will be started from 1.
# Check the current char in the iteration index.
# If it is an alphabet character [a-zA-Z] and the flag value is equal to 1, then change this character to upper case.
# If it is an alphabet character [a-zA-Z] and the flag value is equal to 0, then change this character to lower case.
# Otherwise, if it is not an alphabet character, then set the flag value to 1.
# If the current char is an alphabet character, do a boolean not operation to the flag.
# After the iteration has done, return the fixed string that might have been changed in such iteration.

# Examples
# uglify_word("aaa") === "AaA"
# uglify_word("AAA") === "AaA"
# uglify_word("BbB") === "BbB"
# uglify_word("aaa-bbb-ccc") === "AaA-BbB-CcC"
# uglify_word("AaA-BbB-CcC") === "AaA-BbB-CcC"
# uglify_word("eeee-ffff-gggg") === "EeEe-FfFf-GgGg"
# uglify_word("EeEe-FfFf-GgGg") === "EeEe-FfFf-GgGg"
# uglify_word("qwe123asdf456zxc") === "QwE123AsDf456ZxC"
# uglify_word("Hello World") === "HeLlO WoRlD"

def uglify_word(s):
    flag = 1
    ugly = []
    for c in s:
        ugly.append(c.upper() if flag else c.lower())
        flag = not flag or not c.isalpha()
    return ''.join(ugly)

#OR

def uglify_word(s: str) -> str:
    flag = 1
    result = []
    for i in s:
        if flag == 1 and i.isalpha():
            result.append(i.upper())
            flag = 0
            continue
        elif flag == 0 and i.isalpha():
            result.append(i.lower())
            flag = 1
            continue
        elif not i.isalpha():
            flag = 1
            result.append(i)
            continue
    return (''.join(result))



# Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries. Marketing thinks it would be great to welcome visitors to the site in their own language. Luckily you already use an API that detects the user's location, so this is an easy win.

# The Task
# Think of a way to store the languages as a database. The languages are listed below so you can copy and paste!
# Write a 'welcome' function that takes a parameter 'language', with a type String, and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input.


def greet(language):
    return {
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'english': 'Welcome',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }.get(language, 'Welcome')

#OR

def greet(language):
    greets = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }
    return greets[language] if language in greets else "Welcome"

#OR

# def greet(language):
#   if language=='english':
#     return('Welcome')
#   elif language=='czech':
#     return('Vitejte')
#   elif language=='danish':
#     return('Velkomst')
#   elif language=='dutch':
#     return ('Welkom')
#   elif language=='estonian':
#     return('Tere tulemast')
#   elif language=='finnish':
#     return('Tervetuloa')
#   elif language=='flemish':
#     return('Welgekomen')
#   elif language=='french':
#     return('Bienvenue')
#   elif language=='german':
#     return('Willkommen')
#   elif language=='irish':
#     return('Failte')
#   elif language=='italian':
#     return('Benvenuto')
#   elif language=='latvian':
#     return ('Gaidits')
#   elif language=='lithuanian':
#     return ('Laukiamas')
#   elif language=='polish':
#     return ('Witamy')
#   elif language=='spanish':
#     return('Bienvenido')
#   elif language=='swedish':
#     return('Valkommen')
#   elif language=='welsh':
#     return('Croeso')
#   else:
#     return('Welcome')
  
  #__________________-

#   Imagine you start on the 5th floor of a building, then travel down to the 2nd floor, then back up to the 8th floor. You have travelled a total of 3 + 6 = 9 floors of distance.

# Given an array representing a series of floors you must reach by elevator, return an integer representing the total distance travelled for visiting each floor in the array in order.

# // simple examples
# elevatorDistance([5,2,8]) = 9
# elevatorDistance([1,2,3]) = 2
# elevatorDistance([7,1,7,1]) = 18

# // if two consecutive floors are the same,
# //distance travelled between them is 0
# elevatorDistance([3,3]) = 0
# Array will always contain at least 2 floors. Random tests will contain 2-20 elements in array, and floor values between 0 and 30.


# return sum([abs(array[i] - array[i+1]) for i in range(len(array)-1)])


# Given any number of boolean flags function should return true if and only if one of them is true while others are false. If function is called without arguments it should return false.

#   only_one() == False
#   only_one(True, False, False) == True
#   only_one(True, False, False, True) == False
#   only_one(False, False, False, False) == False  

def only_one(*args):
    return args.count(True)==1

# What is Python *args?
# The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list. 

# The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
# What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
# For example, we want to make a multiply function that takes any number of arguments and is able to multiply them all together. It can be done using *args.
# Using the *, the variable that we associate with the * becomes iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.

#__________________

# You will get a list with several scattered numbers

# You must check that the sum of the two values on both sides equals the sum of the rest of the list elements

# And if not, delete the two elements on the sides and check repeatedly,

# until you reach the condition checklist:

# The sum of the list without the sides = the sum of the sides

# If it never equals return an empty list []

def plastic_balance(L):
    if L and L[0]+L[-1]!=sum(L[1:-1]): return plastic_balance(L[1:-1])
    return L

#____________________

# Write a simple regex to validate a username. Allowed characters are:

# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

def validate_usr(username):
    numeric="0123456789"
    if len(username)>=4 and len(username)<=16:
        for letter in username:
            status = 0
            if letter.islower() or letter == "_":
                status = 1
            for num in numeric:
                if letter == num:
                    status = 1
            if status == 0:
                return False
        return True
    else:
        return False
    

    #OR

def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False 
    allowed = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    for i in username:
        if i not in allowed:
            return False
    return True

# Write a function that takes a list of at least four elements as an argument and returns a list of the middle two or three elements in reverse order.

def reverse_middle(lst):
    l = len(lst)//2 - 1
    return lst[l:-l][::-1]

# Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:

# multiply(3)==15 # 3 * 5¹
# multiply(10)==250 # 10 * 5²
# multiply(200)==25000 # 200 * 5³
# multiply(0)==0 # 0 * 5¹
# multiply(-3)==-15 # -3 * 5¹


def multiply(n):
    x = n * (5**len(str(abs(n))))
    return x

# HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

def sorter(textbooks):
    return sorted(textbooks,key=str.lower)

#or

def sorter(textbooks):
    return sorted(textbooks, key=str.casefold)
#**** .casefold will sort while being case insensitive. 

# Write a function that will check if two given characters are the same case.

# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0
# Examples
# 'a' and 'g' returns 1

# 'A' and 'C' returns 1

# 'b' and 'G' returns 0

# 'B' and 'g' returns 0

# '0' and '?' returns -1

def same_case(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1

#OR

def same_case(a, b): 
    if a.isalpha() and b.isalpha():
        if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
            return 1
        else:
            return 0
    else:
        return -1
    

# Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

# Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

# Examples:

# * With `name` = "john"  => return "Hello, John!"
# * With `name` = "aliCE" => return "Hello, Alice!"
# * With `name` not given 
#   or `name` = ""        => return "Hello, World!"


def hello(name=""):
    return "Hello, " + name.title()+"!" if len(name)>1  else "Hello, World!"