#1
for i in range(0,10):
    print(f"Iteration {i}")

#2
for i in range(10, 0, -1):
    print(f"Reverse Iteration {i}")

#3
for i in range(1, 8):
    print("#" * i)

#4
for i in range(1, 8):
    for j in range(1, 8):
        print("Waiting for more precision...")

#5
for i in range(1, 11):
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
        