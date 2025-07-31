dico = {
    "Alice": 125,
    "Bob": 30, 
    "Charlie": 35,
    "David": 40
}

sorted_items = sorted(dico.items(), key=lambda x: x[1], reverse=True)
print(sorted_items)