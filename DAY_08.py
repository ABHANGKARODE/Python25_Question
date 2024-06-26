# User
# Day 8: Odd and Even
# Write a function called odd_even that has one parameter and
# takes a list of numbers as an argument. The function returns the
# difference between the largest even number in the list and the
# smallest odd number in the list. For example, if you pass
# [1,2,4,6] as an argument the function should return 6 -1= 5.

def odd_even(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    return max(evens) - min(odds)
print("Difference between largest even and smallest odd:", odd_even([1, 2, 4, 6]))

# Extra Challenge: List of Prime Numbers
# Write a function called prime_numbers. This function asks a
# user to enter a number (integer) as an argument and returns a
# list of all the prime numbers within its range. For example, if user
# enters 10, your code should return [2, 3, 5, 7] as prime numbers.
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
print("Prime numbers within the range:", is_prime(number))
