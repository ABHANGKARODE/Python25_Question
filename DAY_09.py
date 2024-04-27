# Day 9: Biggest Odd Number
# Create a function called biggest_odd that takes a string of
# numbers and returns the biggest odd number in the list. For
# example, if you pass ‘23569’ as an argument, your function
# should return 9. Use list comprehension.

def biggest_odd(numbers):
    # Use list comprehension to convert each character to an integer
    # Filter out even numbers and convert them back to string
    # Get the maximum odd number using max()
    return int(max([num for num in numbers if int(num) % 2 != 0]))

print("Biggest odd number:", biggest_odd('23569'))


# Extra Challenge: Zeros to the End
# Write a function called zeros_last. This function takes a list as
# argument. If a list has zeros (0), it will move them to the front of
# the list and maintain the order of the other numbers in the list.
# If there are no Zeros in the list, the function should return the
# original list sorted in ascending order. For example, if you pass
# [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1,
# 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
# your code should return [1, 2, 4, 6, 7].

def zeros_last(lst):
    # Separate zeros and non-zeros
    zeros = [num for num in lst if num == 0]
    non_zeros = [num for num in lst if num != 0]

    # Return sorted list with zeros moved to the end
    return sorted(non_zeros) + zeros

# Test cases
print("Result with zeros moved to the end:", zeros_last([1, 4, 6, 0, 7, 0, 9]))
print("Result with sorted list if no zeros:", zeros_last([2, 1, 4, 7, 6]))
