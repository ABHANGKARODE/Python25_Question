# Day 11: Are They Equal?
# Write a function called equal_strings. The function takes two
# strings as arguments and compares them. If the strings are equal
# (if they have the same characters and have equal length), it
# should return True, if they are not, it should return False. For
# example, ‘love’ and ‘evol’ should return True.

def equal_strings(str1, str2):
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort the characters of both strings and compare them
    return sorted(str1) == sorted(str2)

# Test the equal_strings function
string1 = 'love'
string2 = 'evol'
print(equal_strings(string1, string2))  # Output: True


# Extra Challenge: Swap Values
# Write a function called swap_values. This function takes a list
# of numbers and swaps the first element with the last element.
# For example, if you pass [2, 4,67, 7] as a parameter, your
# function should return
# [7, 4, 67, 2].

def swap_values(lst):
    # Check if the list has at least two elements
    if len(lst) < 2:
        return lst

    # Swap the first and last elements
    lst[0], lst[-1] = lst[-1], lst[0]

    return lst

# Test the swap_values function
numbers = [2, 4, 67, 7,8,10]
print(swap_values(numbers))  # Output: [10,4,67,7,8,2]
