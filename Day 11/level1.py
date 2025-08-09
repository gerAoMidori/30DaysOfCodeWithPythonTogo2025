#1
def add_two_numbers(a, b):
    return a + b

#2
from math import pi
def area_of_circle(r):
    area = pi * (r ** 2)
    print(f"The area of the circle with radius {r} is: {area}")
#3
def add_all_numbers(*args):
    val = 0
    for i in args:
        if  isinstance(i, (int, float)) == True:
            val += i
        else:
            return "All arguments must be numbers."
        
    return f"The sum of the numbers is: {val}"
        
c = add_all_numbers(1, 2, 3, 4, 5)

#4
def convert_celsius_to_fahrenheit(temp_celsius):
    if isinstance(temp_celsius, (int, float)):
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        return f"{temp_celsius}°C is equal to {temp_fahrenheit}°F"
    else:
        return "Input must be a number."

#5
def check_season(month):
    season = {"Winter": ["December", "January", "February"],
              "Spring": ["March", "April", "May"],
              "Summer": ["June", "July", "August"],
              "Autumn": ["September", "October", "November"]
              }
    for i in season:
        if month in season[i]:
            return f"{month} is in {i}."
        

#6
def calculate_slope(x1, y1, x2, y2):   
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    slope = (y2 - y1) / (x2 - x1)
    return f"The slope between points ({x1}, {y1}) and ({x2}, {y2}) is: {slope}"

#7
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "Coefficient 'a' cannot be zero."
    
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No real solution."
    if discriminant == 0:
        return f"Whe have douuble solutions which is {-b / 2*a}."
    return f"The solutions of the equation are: {(-b + discriminant**0.5) / (2*a)} and {(-b - discriminant**0.5) / (2*a)}"


#8

def print_list(your_list):
    for i in your_list:
        print(i)

#9

def reverse_list(my_list):
    return my_list [::-1]


#10
def capitalize_list_items(my_list):
    return [i.upper() for i in my_list]

#11

def add_item(my_list, val_to_add):
    return my_list + [val_to_add]

#12

def remove_item(my_list, val):
    return [i for i in my_list if i != val]

#13

def sum_of_numbers(number):
    cursor = 0
    val = 0

    while cursor <= number:
        val += cursor
        cursor += 1
    return val 

#14

def sum_of_evens(number):
    cursor = 0
    val = 0

    while cursor <= number:
        if cursor % 2 == 0:
            val += cursor
        cursor += 1
    return val 

#15

def sum_of_odds(number):
    cursor = 0
    val = 0

    while cursor <= number:
        if cursor % 2 != 0:
            val += cursor
        cursor += 1
    return val 

