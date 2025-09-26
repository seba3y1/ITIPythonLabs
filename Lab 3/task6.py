import random, csv

def  random_task():
    while True:
        try:
            n = int(input("how many random numbers? "))
            if n > 0:
                break
        except ValueError:
            print("invalid number, try again.")

    nums = [random.randint(1, 100) for _ in range(n)]

    with open("random_numbers.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["index", "value"])
        for i, val in enumerate(nums, 1):
            writer.writerow([i, val])

    avg = sum(nums) / len(nums)
    print(f"generated {n} numbers. average = {avg:.2f}")