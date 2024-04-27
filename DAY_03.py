# Day 3: Register Check
# Write a function called register_check that checks how many
# students are in school. The function takes a dictionary as a
# parameter. If the student is in school, the dictionary says ‘yes’. If
# the student is not in school, the dictionary says ‘no’. Your
# function should return the number of students in school. Use the
# dictionary below. Your function should return 3.
# register = {'Michael':'yes','John': 'no',
#  'Peter':'yes', 'Mary': 'yes'}
# register = {'Michael':'yes','John': 'no','peter':'yes','Marry':'yes'}


def register_check(register):
    students_in_school = 0
    for status in register.values():
        if status == 'yes':
            students_in_school += 1
    return students_in_school
register1 = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
print(register_check(register1))  





# Extra Challenge: Lowercase Names
# names = ["kerry", "dickson", "John", "Mary",
#  "carol", "Rose", "adam"]
# You are given a list of names above. This list is made up of names
# of lowercase and uppercase letters. Your task is to write a code
# that will return a tuple of all the names in the list that have only
# lowercase letters. Your tuple should have names sorted
# alphabetically in descending order. Using the list above, your
# code should return:
# ('kerry', 'dickson', 'carol', 'adam')

def lowercase_names(names):
    lowercase_only = [name for name in names if name.islower()]
    lowercase_only_sorted = sorted(lowercase_only, reverse=True)
    return tuple(lowercase_only_sorted)

# Test case
names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
result = lowercase_names(names)
print(result)  # Output should be ('kerry', 'dickson', 'carol', 'adam')
