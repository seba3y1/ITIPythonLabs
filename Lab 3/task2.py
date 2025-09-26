import re
from task7 import log_time

@log_time
def  regex_task():
    # create fake log file
    with open("access.log", "w") as file:
        logs = [
            "user1@example.com - login success",
            "invalid-email - failed attempt",
            "hello@test.org - access",
            "another@domain.com",
            "notanemail@@something",
            "fake@site",
            "contact@company.com",
            "random text",
            "me@you.net",
            "foo@bar.com"
        ]
        file.write("\n".join(logs))

    # extract valid emails
    with open("access.log", "r") as file:
        data = file.read()

    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", data))

    with open("valid_emails.txt", "w") as file:
        file.write("\n".join(emails))

    print(f"{len(emails)} valid emails ,saved to valid_emails.txt")