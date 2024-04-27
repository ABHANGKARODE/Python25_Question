# Day 10: Hide my Password
# Write a function called hide_password that takes no
# parameters. The function takes an input (a password) from a
# user and returns a hidden password. For example, if the user
# enters ‘hello’ as a password the function should return ‘****’ as
# a password and tell the user that the password is 4 characters
# long.

def hide_password():
    # Take input from the user
    password = input("Enter your password: ")

    # Get the length of the password
    password_length = len(password)

    # Hide the password by replacing characters with asterisks
    hidden_password = '*' * password_length

    # Return the hidden password along with its length
    return hidden_password, password_length

# Test the hide_password function
hidden_pass, length = hide_password()
print("Hidden password:", hidden_pass)
print("Password length:", length, "characters")




# Extra Challenge: A Thousand Separator
# Your new company has a list of figures saved in a list. The issue
# is that these numbers have no separator. The numbers are
# saved in the following format:
# [1000000, 2356989, 2354672, 9878098].
# You have been asked to write a code that will convert each of the
# numbers in the list into a string. Your code should then add a
# comma on each number as a thousand separator for
# readability. When you run your code on the above list, your
# output should be:
# [ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]
# Write a function called convert_numbers that will take one
# argument, a list of numbers above.

def convert_numbers(numbers):
    # Convert each number to a string and add a comma as a thousand separator
    formatted_numbers = [format(num, ',') for num in numbers]
    return formatted_numbers

# Test the convert_numbers function
numbers = [1000000, 2356989, 2354672, 9878098]
formatted_numbers = convert_numbers(numbers)
print(formatted_numbers)
