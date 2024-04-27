# Day 7: A String Range
# Write a function called string_range that takes a single
# number and returns a string of its range. The string characters
# should be separated by dots(.) For example, if you pass 6 as
# an argument, your function should return ‘0.1.2.3.4.5’.
def string_range(num):
    # Generate a string range from 0 to num-1 separated by dots
    return '.'.join(map(str, range(num)))
print("String range:", string_range(6))






# Extra Challenge: Dictionary of names
# You are given a list of names, and you are asked to write a code
# that returns all the names that start with ‘S’. Your code should
# return a dictionary of all the names that start with S and how
# many times they appear in the dictionary. Here is a list below:
# names = ["Joseph","Nathan", "Sasha", "Kelly",
#  "Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
# Your code should return: {“Sasha”: 1, “Sera”: 2}
print("Dictionary of names")


# Function to return names starting with 'S' and their frequency
def names_starting_with_s(names):
    # Initialize an empty dictionary to store names starting with 'S' and their frequency
    s_names = {}
    # Iterate through the list of names
    for name in names:
        # Check if the name starts with 'S'
        if name.startswith('S'):
            # Increment the frequency count if name already exists, otherwise add the name to the dictionary
            s_names[name] = s_names.get(name, 0) + 1
    # Return the dictionary of names starting with 'S' and their frequency
    return s_names
names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
print("Names starting with 'S':", names_starting_with_s(names))