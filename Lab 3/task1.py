import math
from task7 import log_time

@log_time
def  math_task():
    while True:
        nums = input("enter numbers and seprate by commas: ").strip()
        try:
            numbers = [float(x) for x in nums.split(",") if x.strip()]
            break
        except ValueError:
            print("enter valid numbers")

    with open("math_report.txt", "w") as f:
        for n in numbers:
            f.write(f"Floor: {math.floor(n)}\n")
            f.write(f"Ceil: {math.ceil(n)}\n")
            f.write(f"Square root: {math.sqrt(n) if n >= 0 else 'N/A'}\n")
            f.write(f"Circle area: {math.pi * n**2}\n\n")

    print(" math_report.txt created.")
    with open("math_report.txt", "r") as file:
        data = file.read()
        print(data)