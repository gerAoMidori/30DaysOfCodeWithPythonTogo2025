#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [x for x in numbers if x <= 0]

#2

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [j for i in list_of_lists for j in i[0]]

#3
first_tuple = [tuple([i] + [i**j for j in range(6)]) for i in range(11)]


#4
countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [[j[0].upper(), j[0][:3].upper(),j[1].upper()] for i in countries for j in i]

#5

dico_countries = [{"country" : j[0].upper(), "city" : j[1].upper()} for i in countries for j in i]

#6

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],[('Donald', 'Trump')], [('Bill', 'Gates')]]

concatenate_names = [j[0]+" "+j[1] for i in names for j in i]

#7
# y = mx + b
def solver(_x1, _y1, _x2, _y2):

    m = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

    b = lambda m, x, y: y - m * x

    slope_val = m(_x1, _y1, _x2, _y2)    

    val = b(slope_val, _x2, _y2)  

    return slope_val, val

