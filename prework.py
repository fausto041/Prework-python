#Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.

def print_hello_name(user_name):
    print("hello," + user_name + "!")
    
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for i in range(1, 101, 2):
        print(i)
#Please write a Python function, max_num_in_list to return the max number of a given list. 
def max_num_in_list(num_list):
    max_num = num_list[0, 30, 20, 8, 40] 
    for num in num_list:
        if num > max_num:
            max_num = num # initialize max_num to the first element of the list
    return max_num

#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 == 0: # divisible by 4
        if a_year % 100 == 0 and a_year % 400 != 0: # divisible by 100 but not 400
            return False
        else:
            return True
    else:
        return False

#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.




def is_consecutive(numbers):
    """
    Check if all the numbers in the given list are consecutive numbers.
    Returns True if the list contains consecutive numbers, False otherwise.
    """
    if len(numbers) == 0:
        return False
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i-1] + 1:
            return False
    return True