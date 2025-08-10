
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark','Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
#Explain the difference between map, filter, and reduce.
""" With map we take each element of a list, apply a funtion to that element and add that output into our list
    With filter we do the same thing but the best practice is to have a funtion that returns true or false and if 
    the answer is true we add the element we've processed into the list
    With reduce what I understood is that we parse a funtion with ideally 2 variables and reduce takes items in groups 
    of two, first and second, after result of the previous operation and the following item until the list ends and return the final result 
    as a single value either and integer or a string
"""

#2
#Explain the difference between higher order function, closure and decorator
""" Higher order funtion that return a funtion
    Closure is a funtion that remembers varaibles even after it's execution
    Decorator is a funtion that takes a funtion runs it and return a new funtions

"""
#3
#Call funtion

def HelloWorld(message):

    if "land" in message:
        return True
    else:
        return False

countries_= filter(HelloWorld, countries)
countries_land = list(countries_)

#4
for i in countries:
    print(i)

#5
for i in names:
    print(i)

#6
for i in numbers:
    print(i)