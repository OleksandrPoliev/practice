# from codewars
#
# Descending
# Order
# import itertools
#
#
# def descending_order(num):
#     num1 = str(num)
#     num_map = map(int, num1)
#     num_list = list(num_map)
#     list1 = []
#     for i in itertools.permutations(str(n) for n in num_list):
#         list1.append("".join(i))
#     maxi = max(list1, key=int)
#     return (int(maxi))
#
#
# Sort
# array
# by
# string
# length
#
#
# def sort_by_length(arr):
#     arr.sort(key=lambda x: len(x))
#     return arr
#
#
# You
# only
# need
# one - Beginner
#
#
# def check(seq, elem):
#     if elem in seq:
#         return True
#     return False
#
#
# Convert
# a
# Boolean
# to
# a
# String
#
#
# def boolean_to_string(b):
#     return str(b)
#
#
# Convert
# boolean
# values
# to
# strings
# 'Yes' or 'No'.
#
#
# def bool_to_word(boolean):
#     if boolean is True:
#         return "Yes"
#     return "No"
#
#
# Small
# enough? - Beginner
#
#
# def small_enough(array, limit):
#     for i in array:
#         if i > limit:
#             return False
#     return True
#
#
# Regular
# Ball
# Super
# Ball
#
#
# class Ball(object):
#     def __init__(self, objekt="regular"):
#         self.objekt = objekt
#
#     def __str__(self):
#         return self.objekt
#
#     @property
#     def ball_type(self):
#         return self.objekt
#
#
# Object
# Oriented
# Piracy
#
#
# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#
#     def is_worth_it(self):
#         if (self.draft - (self.crew * 1.5)) >= 20:
#             return True
#         return False
#
#
# Refactored
# Greeting
#
#
# class Person:
#     def __init__(self, my_name):
#         self.name = my_name
#
#     def greet(self, your_name):
#         return f"Hello {your_name}, my name is {self.name}"
#
#
# Person
# Class
# Bug
#
#
# class Person:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = F"{first_name} {last_name}"
#
#
# Middle
# Me
#
#
# def middle_me(N, X, Y):
#     if N % 2 == 1:
#         return X
#     return f"{Y * (N // 2)}{X}{Y * (N // 2)}"
#
#
# Digitize
#
#
# def digitize(n):
#     list = []
#     for i in str(n):
#         for j in i:
#             list.append(int(j))
#     return list
#
#
# Sum
# of
# Digits / Digital
# Root
#
#
# def digital_root(n):
#     n = str(n)
#     list1 = []
#     while len(n) != 1:
#         for i in n:
#             j = int(i)
#             list1.append(int(j))
#         n = sum(list1)
#         n = str(n)
#         list1 = []
#
#
# return int(n)
# Who likes it?
# def likes(names):
#     if len(names) >= 4:
#         return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
#     if len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     if len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     if len(names) == 1:
#         return f"{names[0]} likes this"
#     if len(names) == 0:
#         return f"no one likes this"
#
#
# Array.diff
#
#
# def array_diff(a: list, b: list) -> list:
#     c = []
#     for i in a:
#         if i not in b:
#             c.append(i)
#     return c
#
#
# Create
# Phone
# Number
#
#
# def create_phone_number(n):
#     return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
#
#
# Unique
# In
# Order
#
#
# def unique_in_order(a):
#     a = list(a)
#     C = []
#     for i, x in zip(a, a[1:]):
#         if i != x:
#             C.append(i)
#     if len(a) > 0:
#         C.append(a[-1])
#     return C
#
#
# Persistent
# Bugger.
#
#
# def persistence(n):
#     k = 0
#     n = str(n)
#     while len(n) != 1:
#
#         n = list(n)
#         t = 1
#         for i in n:
#             i = int(i)
#             t *= i
#
#         n = t
#         n = str(n)
#         k += 1
#     return k
#
#
# Turn
# String
# Input
# into
# Hash
#
#
# def str_to_hash(st):
#     if len(st) < 2:
#         return {}
#     convertedDict = dict((x.strip(), int(y.strip()))
#                          for x, y in (element.split('=')
#                                       for element in st.split(', ')))
#     return convertedDict
#
#
# # Breaking search bad
# #
# # def search(titles, term):
# #     lists=[]
# #     listt=[]
# #     term=term.upper()
# #     for i in titles:
# #         i=i.upper()
# #         lists.append(i)
# #     for i in lists:
# #         if term in i :
# #             listt.append(i)
# #     lists=[]
# #     for i in listt :
# #          for j in titles:
# #             if len(i)==len(j) and i[0].upper()==j[0].upper():
# #                 lists.append(j)
# #                 break
# #     return lists
#
#
# Two
# Sum
#
#
# def two_sum(numbers, target):
#     number = numbers[1:]
#     for i, t in enumerate(numbers):
#         for j, q in enumerate(number):
#             k = t + q
#             if k == target:
#                 return i, j + 1
#
#
# Simple
# Pig
# Latin
#
#
# def pig_it(text):
#     text = text.split()
#     ready_text = []
#     for str_element in text:
#         if str_element in ["!", "?"]:
#             ready_text.append(str_element)
#             continue
#         else:
#             new_str = str_element[1:] + str_element[0] + "ay"
#             ready_text.append(new_str)
#     sentens = " ".join(ready_text)
#     return sentens
#
#
# Regex
# Password
# Validation
#
# regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
# Pete, the
# baker
#
#
# def cakes(recipe, available):
#     result_return = []
#     for key in recipe:
#         if key not in available:
#             return 0
#         else:
#             recipe_var = recipe.get(key)
#             available_var = available.get(key)
#             result_return.append(available_var // recipe_var)
#     return min(result_return)
#
#
# Square
# Every
# Digit
#
#
# def square_digits(num):
#     num = str(num)
#     return_var = ""
#     for i in num:
#         k = int(i) * int(i)
#         return_var += str(k)
#     return int(return_var)
#
#
# Find
# The
# Parity
# Outlier
#
#
# def find_outlier(integers):
#     list = [x for x in integers if x % 2 == 1]
#     list2 = [x for x in integers if x % 2 == 0]
#     return list[0] if len(list) < len(list2) else list2[0]
#
#
# List
# Filtering
#
#
# def filter_list(l):
#     result_list = [x for x in l if isinstance(x, int) and x > -1]
#     return result_list
#
#
# Moving
# Zeros
# To
# The
# End
#
#
# def move_zeros(array: list):
#     listOFZERO = [x for x in array if x > 0]
#     l = [x for x in array if x == 0]
#
#     return listOFZERO + l
#
#
# Calculate
# average
#
#
# def find_average(numbers):
#     return sum(numbers) / len(numbers)
#
#
# Multiply
#
#
# def multiply(a, b):
#     return a * b

# def prime_generator(n):
#     # Generator pozwalający na iterowanie po n liczbach pierwszych
#     number = 2
#     generated_numbers = 0
#     while generated_numbers != n:
#         if number:
#             yield number
#             generated_numbers += 1
#         number += 1
#
#
# gen = prime_generator(1000000)
# for elem in gen:
#     print(elem)


# class PrimeIterator:
#
#     def __init__(self, n):
#         self.n = n
#         self.generated_numbers = 0
#         self.number = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number += 1
#         if self.generated_numbers >= self.n:
#             raise StopIteration
#         elif self.number:
#             self.generated_numbers += 1
#             return self.number
#         return self.__next__()
#
#
# iter = PrimeIterator(1000)
# for elem in iter:
#     print(elem)


# class Loopse:
#
#     def __init__(self,n):
#         self.n=n
#
#     def loos(self):# тобі не потрібно передавати дату яка уже вказана
#         datalist=[]
#         for i in self.n :
#             if i%5==0:
#                 datalist.append(i)
#         return datalist
#
# data=Loopse([x for x in range(10)])
#
# data2=Loopse([10,4,'str'])

class NumberChenge:
    def __init__(self,n):
        self.n=n
    def cheng_n(self):
        self.n=self.n+1
        return self.n

    def g(self):
        return self.n


data =NumberChenge(2)
for i in range(10):
    data.cheng_n()
print(data.g())