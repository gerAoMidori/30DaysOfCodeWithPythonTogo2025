import random
import string

#1

def random_user_id(length = 6):
    all_character = string.ascii_letters + string.digits
    id = ""
    for i in range(length):
        id += random.choice(all_character)
    return id

#2 

def user_id_gen_by_user():
    length = int(input("Enter the number of characters you want"))
    number = int(input("Enter the number of IDs you want"))

    for i in range(number):
        print(random_user_id(length))

#3

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f"rgb({red}, {green}, {blue})"

print(rgb_color_gen())