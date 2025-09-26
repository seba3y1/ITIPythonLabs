from task1 import  math_task
from task2 import  regex_task
from task3 import  datetime_task
from task4 import  products_task
from task5 import  filemanager_task
from task6 import  random_task

def menu():
    tasks = {
        1: ("Math Automation",  math_task),
        2: ("Regex Log Cleaner",  regex_task),
        3: ("Datetime Reminder",  datetime_task),
        4: ("Product Data Transformer",  products_task),
        5: ("OS File Manager",  filemanager_task),
        6: ("Random Data Generator",  random_task),
    }

    print("\n===== TASK MENU =====")
    for k, v in tasks.items():
        print(f"{k}) {v[0]}")

    while True:
        try:
            choice = int(input("Select a task number: "))
            if choice in tasks:
                tasks[choice][1]()
                break
            else:
                print("invalid choice, try again")
        except ValueError:
            print("enter a valid number")

if __name__ == "__main__":
    menu()