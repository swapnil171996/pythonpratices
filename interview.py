
'''d="sadhana"
duplicate={}

for char in d:
    if char in duplicate:
        duplicate[char]+=1
    else:
        duplicate[char]=1
for char,count in duplicate.items():
    if count>1:
        print(f"'{char}' appers {count} times'")'''

srt = "hackerearth"
duplicates = []

for char in srt:
    if srt.count(char) > 1 and char not in duplicates:
        duplicates.append(char)

for char in duplicates:
    print(char, end=" ")

'''1. Find duplicate char from string. Write a program to find duplicate characters in a given String.

Input: hackerearth
Output: h a e r'''

srt="hackerearth"
duplicatee={}

for char in srt:
    if char in duplicatee:
        duplicatee[char]+=1
    else:
        duplicatee[char]=1
for char,count in duplicatee.items():
    if count>1:
        print(char,end=" ")
'''2. Remove duplicate char from string: Write a program to remove duplicate characters in a given String.

Input: hackerearth
Output: hackert'''

def remove_duplicate(input_str):
    result=''
    seen=set()
    for char in input_str:
        if char not in seen:
            seen.add(char)
            result+=char
    return result
input_str = "hackerearth"
output=remove_duplicate(input_str)
print(output)

'''3. Revere string: Write a program to reverse a given string.

Input: This is a string
Output: gnirts a si sihT'''
'''
def reverse_string(input_str):
    return input_str[::-1]

input_str='This is a string'
output1=reverse_string(input_str)
print(output1)'''

def reverse_strings(input_st):
    reverse_st=''
    for char in input_st:
        reverse_st=char+reverse_st
    return reverse_st

input_str='This is a string'
output1=reverse_strings(input_str)
print(output1)

#
def reverse_each_word(input_str):
    words = input_str.split()         # Split the string into words
    reversed_words = []

    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word  # Reverse the word without slicing
        reversed_words.append(reversed_word)

    return " ".join(reversed_words)   # Join the reversed words back into a sentence

# Example usage
input_string = "This is a string"
output = reverse_each_word(input_string)
print(output)

'''String count of non-space chracter: Write a program to calculate the count of non-space characters in a string.

Input: This is a string
Output: 13'''

def count_non_space_character(input_st):
    count=0
    for char in input_st:
        if char!=" ":
            count+=1

    return count
input_st="This is a string"
output2=count_non_space_character(input_st)
print(output2) #13

#5. Swap two string using Substring: Write a program to swap the two strings using substring.
'''Input: Hello world
Output: World Hello'''

def swap_two_numbers(input_strr):
    space_index=input_strr.find(" ")
    first_word=input_strr[:space_index]
    second_word=input_strr[space_index+1:]
    return second_word+ " "+first_word
input_strr="Hello world"
output3=swap_two_numbers(input_strr)
print(output3)

#Swap two string using temp variable

def swap_number_temp_variable(input_s):
    word1,word2=input_s.split(input_s)
    temp=word1
    word1=word2
    word2=temp
    return word1+" "+word2

input_s="hello world"
output4=swap_number_temp_variable(input_s)
print(output4)

a = "10"
b = "20"
combined=a+b
a, b = combined[len(a):], combined[:len(a)]
print("Swapped values:", a, b)
'''
year = int(input("Enter a year: "))
if (year%4==0 and year%100 != 0) or(year%400==0):
    print(f"{year} is a leap year.")
'''

import random
x=-500
y=-100
z=50
print(random.randrange(x,y,z))

import math
num1=2.516
num2=-8
num3=7
print(math.ceil(num1))#3
print(math.floor(num1))#2
print(math.fabs(num2))#8.0
print(math.factorial(num3))#5040

import time
import datetime

print(time.gmtime())
print(time.localtime())
print(time.strftime("%S:%H:%M"))
print(datetime.date.today())
print(datetime.date.today().strftime("%d/%m/%y"))


def largest_word_string(in_sre):
    word_list=in_sre.split()
    max_word=word_list[0]
    for word in word_list:
        if len(word) > len(max_word):
            max_word=word
        else:
            continue



    print("Max_word:",max_word)
in_sre="Swapnil  Patil"

largest_word_string(in_sre)


def lon_word_string(i_st):
    word_l=i_st.split()
    max_len=word_l[0]
    for word in word_l:
        if len(word)>len(word_l):
            max_len=word
        else:
            continue
    print("Max length word",max_len)

i_st="I am living in india"
lon_word_string(i_st)











