import random
from string import digits
#1
def shuffle_list(my_list : list):
    new_list = my_list.copy()
    random.shuffle(new_list)
    return new_list

""" For testing
my = [1, 2, 3, 4]
print(shuffle_list(my))
print(my)

"""

#2
def seven_random():
    val = ""
    while len(val) != 7:
        a = random.choice(digits)
        if a not in val:
            val += a
    return val

print(seven_random())