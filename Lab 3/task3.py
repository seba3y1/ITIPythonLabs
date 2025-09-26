from datetime import datetime

def  datetime_task():
    while True:
        date_str = input("enter a date (YYYY-MM-DD): ").strip()
        try:
            user_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("invalid format, try again")

    today = datetime.today().date()
    diff = (user_date - today).days

    if diff < 0:
        print("this date passed")
    else:
        with open("reminders.txt", "a") as file:
            file.write(f"{user_date} -> {diff} days left\n")
        print(f" reminder saved")