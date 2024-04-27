# Day 4: Only Floats
# Write a function called only_floats, which takes two
# parameters a and b, and returns 2 if both arguments are floats,
# returns 1 if only one argument is a float, and returns 0 if neither
# argument is a float. If you pass (12.1, 23) as an argument, your
# function should return a 1.

def only_floats(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0
print("only float")
#Example_01
result = only_floats(12.1, 23)
print(result)  
#Example_02
result =only_floats(1.1,2.1)
print(result)





# Extra Challenge: Index of the Longest Word
# Write a function called word_index that takes one argument,
# a list of strings and returns the index of the longest word in the
# list. If there is no longest word (if all the strings are of the same
# length), the function should return zero (0). For example, the list
# below should return 2.
# words1 = ["Hate", "remorse", "vengeance"]
#  And this list below, shoul return zero (0)
# words2 = ["Love", "Hate"]

def word_index(words):
    if not words:
        return 0
    
    max_length = len(words[0])
    max_index = 0
    
    for i in range(1, len(words)):
        if len(words[i]) > max_length:
            max_length = len(words[i])
            max_index = i
    
    return max_index

# Test cases
print("longest word")
words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

print(word_index(words1))  # Output should be 2
print(word_index(words2))  # Output should be 0
