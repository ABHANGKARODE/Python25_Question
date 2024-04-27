# Day 5: My Discount
# Create a function called my_discount. The function takes no
# arguments but asks the user to input the price and the
# discount (percentage) of the product. Once the user inputs the
# price and discount, it calculates the price after the discount.
# The function should return the price after the discount. For
# example, if the user enters 150 as price and 15% as the discount,
# your function should return 127.5.

def my_discount():
    # Ask the user to input price and discount percentage
    price = float(input("Enter the price of the product: $"))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the price after the discount
    discount_amount = price * (discount_percentage / 100)
    price_after_discount = price - discount_amount

    # Return the price after the discount
    return price_after_discount

# Test the function
discounted_price = my_discount()
print("Price after discount:", discounted_price)




# Extra Challenge: Tuple of Student Sex
# You work for a school and your boss wants to know how many
# female and male students are enrolled in the school. The school
# has saved the students in a list. Your task is to write a code that
# will count how many males and females are in the list. Here is a
# list below:
# students = ['Male', 'Female', 'female', 'male', 'male', 'male',
#  'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
# Your code should return a list of tuples. The list above should
# return:
# [(‘Male’,7), (‘female’,6)]

print("Number of Male and Female")
def count_gender(students):
    # Initialize counters for male and female
    male_count = 0
    female_count = 0

    # Iterate through the list of students
    for student in students:
        # Convert the gender to lowercase for case-insensitive comparison
        gender = student.lower()
        # Increment the respective counter based on the gender
        if gender == 'male':
            male_count += 1
        elif gender == 'female':
            female_count += 1

    # Return a list of tuples containing counts for each gender
    return [('Male', male_count), ('female', female_count)]

# List of students
students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

# Count the genders
gender_counts = count_gender(students)

# Print the result
print(gender_counts)
