# Day 1: Division and Square-root  
# Write  a  function  called  divide_or_square  that  takes  one 
# argument (a number), and returns the square root of the number 
# if it is divisible by 5, returns its remainder if it is not divisible by 
# 5. For example, if you pass 10 as an argument, then your function 
# should return 3.16 as the square root. 

import math

def divide_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)
    else:
        return number % 5


print(divide_or_square(10))  







 
# Extra Challenge: Longest Value  
# Write a function called longest_value that takes a dictionary 
# as  an  argument  and  returns  the  first  longest  value  of  the 
# dictionary. For example, the following dictionary should return 
#  apple as the longest value. 
# fruits = {'fruit': 'apple', 'color': 'green'} 


def longest_value(dictionary):
    max_length = 0
    longest_value = None
    
    for value in dictionary.values():
        if len(value) > max_length:
            max_length = len(value)
            longest_value = value
            
    return longest_value

#example_01
fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))  

#example_02
fruits = {'fruit': 'apple', 'color': 'green','quality':"verysweet"}
print(longest_value(fruits))  


   
