# Day 6: User Name Generator
# Write a function called user_name that generates a username
# from the user’s email. The code should ask the user to input an
# email and the code should return everything before the @ sign
# as their user name. For example, if someone enters
# ben@gmail.com, the code should return ben as their user
# name.

def user_name():
    # Input email from user
    email = input("Enter your email: ")
    # Find the position of '@' sign
    at_position = email.find('@')
    # Extract the username from email
    username = email[:at_position]
    # Return the username
    return username
print("Username:", user_name())



# Extra Challenge: Zero Both ends
# Write a function called zeroed code that takes a list of numbers
# as an argument. The code should zero (0) the first and the last
# number in the list. For example, if the input is [2, 5, 7, 8, 9],
# your code should return [0, 5, 7, 8, 0].
print("Zero Both ends")
def zero_both_ends(numbers):
    # Check if the list is not empty
    if numbers:
        # Zero the first and last elements
        numbers[0] = 0
        numbers[-1] = 0
    # Return the modified list
    return numbers
numbers = [2, 5, 7, 8, 9]
print("Zeroed list:", zero_both_ends(numbers))