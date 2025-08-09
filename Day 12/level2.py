import random
import string

#1

def list_of_hexa_colors(number):
    our_list = []
    possible_values = string.digits + string.ascii_lowercase[:6]
    while len(our_list) != number:
        color = "#"
        for i in range(6):
            color +=  random.choice(possible_values)
        if color not in our_list:
            our_list.append(color)
    return our_list

#2
def list_of_rgb_colors(number):
    our_list = []
    while len(our_list) != number:
        color = ""
        for i in range(6):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            color = f"rgb({red}, {green}, {blue})"
        if color not in our_list:
            our_list.append(f"rgb({red}, {green}, {blue})")
    return our_list
       

#3
def generate_colors(option, number):
    if option == "hexa":
        return list_of_hexa_colors(number)
    elif option == "rgb":
        return list_of_rgb_colors(number)

print(generate_colors("rgb", 3))