# Day 2: Strings to Integers  
# Write a function called convert_add that takes a list of strings 
# as an argument and converts it to integers and sums the list. For 
# example    should  be  converted  to  [1,  3,  5]  and 
# summed to 9.  

def convert_add(string_list):
    # Convert each string element to an integer and sum them up
    return sum(map(int, string_list))


string_list = ['1', '3', '5']
print(convert_add(string_list))  # Output should be 9




# Extra Challenge: Duplicate Names  
# Write a function called check_duplicates that takes a list of 
# strings as an argument. The function should check if the list has 
# any duplicates. If there are duplicates, the function should return 
# the  duplicates.  If  there  are  no  duplicates,  the  function  should 
# return "No duplicates". For example, the list of fruits below 
# should  return  apple  as  a  duplicate  and list  of  names  should 
# return "no duplicates". 
# fruits = ['apple', 'orange', 'banana', 'apple'] 
# names = ['Yoda', 'Moses', 'Joshua', 'Mark'] 
 
def check_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    if duplicates:
        return duplicates
    else:
        return "No duplicates"


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates(fruits))  # Output should be {'apple'}
print(check_duplicates(names))   # Output should be "No duplicates"

   
