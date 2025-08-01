#1
for i in range(0,10):
    print(f"For Loop Iteration {i}")
a = 0
while a < 10:
    print(f"While Loop Iteration {a}")
    a += 1

#2
for i in range(10, 0, -1):
    print(f"Reverse For Loop Iteration {i}")
a = 10
while a > 0:
    print(f"Reverse While Loop Iteration {a}")
    a -= 1


#3
for i in range(1, 8):
    print("#" * i)

#4
b = 9
for i in range(1, b):
    for j in range(1, b):
        print("#", end="")
    print()
#5
for i in range(0, 11):
    print(i, "x", i, "=", i **2)

#6
my_list = ["python", "numpy", "pandas", "django", "flask"]
for i in my_list:
    print(i) 
    
#7 & #8
print("Even Numbers:")
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

print("Odd Numbers:")
for i in range(0, 101):
    if i % 2 != 0:
        print(i)
        