def level1_1():
    try:
        my_age = int(input("Enter your age: "))
        if my_age >= 18:
            print("You are old enough to learn to drive.")
        else:
            print(f"You need {18 - my_age} more years to learn to drive.")
    except:
        print("Please enter a valid age.")

def level1_2():
    try:
        my_age = int(input("Enter my age: "))
        your_age = int(input("Enter your age: "))
        if my_age == your_age:
            print("We are the same age.")
        else:
            if my_age > your_age:
                print(f"I am  {my_age - your_age} years older than you ." if my_age - your_age != 1 else "I am a year older than you.")
            else:
                print(f"You are {your_age - my_age} years older than me." if your_age - my_age != 1 else "You are a year older than me.")

    except:
        print("Please enter valid ages.")

def level1_3():

    try:
        num1 = int(input("Enter number one: "))
        num2 = int(input("Enter number two: "))
        if num1 == num2:
            print(f"{num1} is equal to {num2}")
        else:
            print(f"{num1} is greater than {num2}" if num1 > num2 else f"{num2} is greater than {num1}")
    except:
        print("Please enter valid numbers")