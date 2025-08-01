#1
a = 0
for i in range(1, 101):
    a += i

print(f"The sum of all numbers is {a}.")

#2
b = 0
for i in range(1, 101):
    if i % 2 == 0:
        b += i
print(f"The sum of all evens is {b}.")

c = 0  
for i in range(1, 101):
    if i % 2 != 0:
        c += i
print(f"The sum of all odds is {c}.")