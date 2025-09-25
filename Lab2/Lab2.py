"""
    Python Practice Tasks
    =====================

    Rules:
        - Everything must be written inside functions.
        - The file should run as a script.
        - When the script starts, the user must see a menu of numbered scenarios  (1: List order, 2: Pepole with favorite color , .....).
        - The user chooses a number, and the program runs the corresponding function.
        - Each task should only run when chosen from the menu.
        - At ANY stage: if the user enters invalid input, the program must:
              * Show an error message
              * Display what valid input looks like
              * Let the user try again (do not crash or exit)

    Tasks:
    ------

    1 - Ask the user to enter 5 numbers.
        Store them, then display them in ascending order and descending order.

    2 - Write a function that takes two numbers: (length, start).
        Generate a sequence of numbers with the given length,
        starting from the given start number and increasing by one each time.
        Print the result.

    3 - Keep asking the user for numbers until they type "done".
        When finished, print:
            * The total of all numbers entered
            * The count of valid entries
            * The average
        If the user enters something invalid, show an error and continue.
        

    4 - Ask the user to enter a list of numbers.
        Remove any duplicates, sort the result, and display it.


    6 - Ask the user to enter a sentence.
        Count how many times each word appears in the sentence
        and display the result.


    7 - Create a small gradebook system:
        - The user enters 5 students names and their scores.
        - At the end, show:
            * The highest score
            * The lowest score
            * The average score.

    8 - Write a program that simulates a shopping cart:
        - The user can add items with a name and a price.
        - The user can remove items by name.
        - The user can view all items with their prices.
        - At the end, display the total cost.

    9 - Create a number guessing game:
        - The program randomly selects a number between 1 and 20.
        - The user keeps guessing until they get it right.
        - After each guess, show if the guess was too high or too low.
        - When correct, display the number of attempts.
"""

def get_int(prompt, valid=None):
    while True:
        val = input(prompt)
        
        num = int(val)
        if valid and not valid(num):
            print("enter a valid number.")
            continue
        return num
        

def get_float(prompt):
    while True:
        val = input(prompt)
        try:
            return float(val)
        except ValueError:
            print("enter a number")

def task1():
    print("enter 5 numbers:")
    numbers = []
    while len(numbers) < 5:
        num = input(f"enter number {len(numbers)+1}/5: ")
        try:
            numbers.append(float(num))
        except ValueError:
            print("enter a number.")
    print("Asc:", sorted(numbers))
    print("Desc:", sorted(numbers, reverse=True))

def task2():
    print("task 2")
    while True:
        length = input("Enter the length : ")
        try:
            length = int(length)
            if length <= 0:
                print("length must be a positive")
                continue
        except ValueError:
            print("invalid input enter a positive integer")
            continue
        break
    start = get_float("enter the start number: ")
    seq = [start + i for i in range(length)]
    print("sequence:", seq)

def task3():
    print("task 3")
    numbers = []
    while True:
        val = input("enter a number or 'done' to finish : ")
        if val.lower() == 'done':
            break
        try:
            numbers.append(float(val))
        except ValueError:
            print("enter a number or 'done'")
    if numbers:
        total = sum(numbers)
        count = len(numbers)
        avg = total / count
        print(f"total: {total}")
        print(f"count: {count}")
        print(f"average: {avg}")
    else:
        print("no valid numbers entered")

def task4():
    print("task 4")
    while True:
        val = input("enter numbers separated by commas: ")
        try:
            nums = [float(x.strip()) for x in val.split(',') if x.strip() != '']
            break
        except ValueError:
            print("enter numbers separated by commas")
    unique_sorted = sorted(set(nums))
    print("result:", unique_sorted)

def task5():
    print("task 5")
    while True:
        sentence = input("Enter a sentence: ").strip()
        if not sentence:
            print(" enter a non-empty sentence")
            continue
        words = sentence.split()
        word_count = {}
        for word in words:
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1
        print("Word counts:")
        for word, count in word_count.items():
            print(f"'{word}': {count}")
        break

def task6():
    print("Task 6")
    students = []
    scores = []
    count = 5
    for i in range(1, count + 1):
        while True:
            name = input(f"enter name for student {i}: ").strip()
            if not name:
                print("name cannot be empty, enter a valid name")
                continue
            break
        while True:
            score = input(f"enter score for {name}: ")
            try:
                score = float(score)
                break
            except ValueError:
                print("score must be a number, enter a valid score")
        students.append(name)
        scores.append(score)
    print("\nGradebook Results:")
    print("Highest score:", max(scores))
    print("Lowest score:", min(scores))
    print("Average score:", sum(scores) / len(scores))




def task8():
    import random
    print("Task 8")
    number = random.randint(1, 20)
    attempts = 0
    while True:
        guess = get_int("Guess a number between 1 and 20: ")
        attempts += 1
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Correct! The number was {number}. Attempts: {attempts}")
            break

def main():
    menu = [
        "1: List order (enter 5 numbers)",
        "2: Generate sequence (length, start)",
        "3: Numbers until 'done' (sum, count, avg)",
        "4: Remove duplicates from list of numbers",
        "5: Word count in a sentence",
        "6: Gradebook system",
        "8: Guessing game",
        "0: Exit"
    ]
    actions = {
        '1': task1,
        '2': task2,
        '3': task3,
        '4': task4,
        '5': task5,
        '6': task6,
        '8': task8
    }
    while True:
        print("\nMenu:")
        for item in menu:
            print(item)
        choice = input("Choose a number: ").strip()
        if choice == '0':
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please enter one of:", ', '.join(actions.keys()) + ", 0")

if __name__ == "__main__":
    main()
