#1
a = 0
for i in range(1, 101):
    a += i

print("Sum of numbers from 1 to 100 :", a)

#2
b = 0
for i in range(1, 101):
    if i % 2 == 0:
        b += i
print("Sum of even numbers from 1 to 100 :", b)

#3
c = 0  
for i in range(1, 101):
    if i % 2 != 0:
        c += i
print("Sum of odd numbers from 1 to 100 :", c)