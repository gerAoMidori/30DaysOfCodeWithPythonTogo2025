import re


def is_valid_variable(var : str):
    if re.match('\\d', var) != None:
        return False 
    check = re.findall("[^A-Za-z0-9]_", var)
    if len(check) == 0:
        return True
    else:
        return False

print(is_valid_variable("Hel__l_o"))

