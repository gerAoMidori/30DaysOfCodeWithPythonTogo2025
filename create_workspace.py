import os 

for i in range(1, 31):
    name = f"Day {i}"
    os.makedirs(name, exist_ok=True)
