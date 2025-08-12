#1
def evens_and_odds(number):
    evens = 0
    odds = 0
    count = 0
    
    if number < 0:
        return "Your argument must be a positive number"
    while count <= number:
        if count % 2 == 0:
            evens += 1
        else:
            odds += 1
        count += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

#1
def factorial(number):
    val = 1
    for i in range(1, number + 1):
        val *= i
    return val

#2
def is_empty(variable):
    if isinstance(variable, (int, float)):
        return "Enter a string or a list"
    if isinstance(variable, str):
        return True if len(variable.strip()) == 0 else False
    return True if len(variable) == 0 else False
    
#3
def calculate_mean(my_list):
    return sum(my_list)/len(my_list)

def calculate_median(my_list):
    if len(my_list) % 2 != 0:
        return my_list[len(my_list)//2]
    else:
        return (my_list[len(my_list)/2] + my_list[(len(my_list)/2) - 1]) /2

def calculate_mode(my_list):
    """I'll use a dictionnary because the is taking too much time"""
    chart = {}
    for i in my_list:
        chart[str(i)] = chart.get(str(i), 0) + 1
    converted_chart = list(chart.items())
    sorted_chart = sorted(converted_chart, key = lambda x:x[1], reverse=True)
    final_list = [i for i in sorted_chart if i[1] == sorted_chart[0][1]]
    return final_list


def calculate_range(my_list):
    return my_list[-1] - my_list[0]

def calculate_variance(my_list):
    t = len(my_list)
    mean_ = calculate_mean(my_list)
    new_list = [(i - mean_)**2 for i in my_list]
    v = 1/t * sum(new_list)
    return v

def calculate_std(my_list):
    return calculate_variance(my_list)**0.5
