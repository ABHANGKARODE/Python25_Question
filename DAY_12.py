# Day 12: Count the Dots
# Write a function called count_dots. This function takes a
# string separated by dots as a parameter and counts how many
# dots are in the string. For example, ‘h.e.l.p.’ should return 4
# dots, and ‘he.lp.’ should return 2 dots.

def count_dots(string):
    # Count the number of dots in the string
    dot_count = string.count('.')
    return dot_count

# Test the count_dots function
string1 = 'h.e.l.p.'
string2 = 'he.lp.'
print(count_dots(string1))  # Output: 4
print(count_dots(string2))  # Output: 2




# Extra Challenge: Your Age in Minutes
# Write a function called age_in_minutes that tells a user how
# old they are in minutes. Your code should ask the user to
# enter their year of birth, and it should return their age in
# minutes (by subtracting their year of birth to the current year).
# Here are things to look out for:
# a. The user can only input a 4-digit year of birth. For
# example, 1930 is a valid year. However, entering any
# number longer or less than 4 digits long should render
# input invalid. Notify the user to input a four digits
# number.
# b. If a user enters a year before 1900, your code should
# tell the user that input is invalid. If the user enters the
# year after the current year, the code should tell the user,
# to input a valid year.
# The code should run until the user inputs a valid year.
# Your function should return the user's age in minutes. For
# example, if someone enters 1930, as their year of birth your
# function should return:
# You are 48,355,200 minutes old.

from datetime import datetime

def age_in_minutes():
    # Get the current year
    current_year = datetime.now().year

    while True:
        # Ask the user to input their year of birth
        year_of_birth = input("Enter your year of birth (4 digits): ")

        # Check if the input is a valid 4-digit number
        if year_of_birth.isdigit() and len(year_of_birth) == 4:
            year_of_birth = int(year_of_birth)

            # Check if the year of birth is within the valid range
            if 1900 <= year_of_birth <= current_year:
                break
            else:
                if year_of_birth < 1900:
                    print("Input is invalid. Year of birth must be after 1900.")
                else:
                    print("Input is invalid. Year of birth must be before the current year.")
        else:
            print("Input is invalid. Please enter a valid 4-digit year of birth.")

    # Calculate age in minutes
    age_in_years = current_year - year_of_birth
    age_in_minutes = age_in_years * 365 * 24 * 60

    return f"You are {age_in_minutes:,} minutes old."

# Test the age_in_minutes function
print(age_in_minutes())
