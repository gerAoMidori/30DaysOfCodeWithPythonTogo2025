"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

"""

""""
2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
September, October or November, the season is Autumn. December, January
or February, the season is Winter. March, April or May, the season is Spring
June, July or August, the season is Summer
"""
def level2_1():
    reference = {
        "A": (80, 100),
        "B": (70, 89),
        "C": (60, 69),
        "D": (50, 59),
        "F": (0, 49)
    }
    try:
        grade = int(input("Enter your grade: "))
    except:
        print("Please enter a valid grade.")

    for j, i in reference.items():
        if i[0] <= grade <= i[1]:
            print(f"Your grade is {j}")
            break


def level2_2():
    seasons = {
        "Autumn": ["September", "October", "November"],
        "Winter": ["December", "January", "February"],
        "Spring": ["March", "April", "May"],
        "Summer": ["June", "July", "August"]
    }
    "Ctrl+C ----> Ctrl+V"
    try:
        month = input("Enter your the current month in english by capitalizing the first letter: ")
    except:
        print("Please enter a valid grade.")

    for j, i in seasons.items():
        if month in i:
            print(f"Current season : {j}")
            break

def level2_3():
    fruits = ["banana", "orange", "mango", "lemon"]
    try:
        fruit = input("Enter a fruit following the format 'raspberry' :")
        while fruit.strip() == "":
            fruit = input("Enter a fruit following the format 'raspberry' :") 
    except:
        print("Please enter a valid fruit.")
    if fruit.strip() not in fruits:
        fruits.append(fruit.strip())
    else:
        print('That fruit already exist in the list')
    print(fruits)


level2_3()
