

import time

def log_time(function):
    def wrapper():
        start = time.time()
        result = function()
        end = time.time()
        runtime = round(end - start, 4)

        # Save result into file
        with open("execution_log.txt", "a") as f:
            f.write(f"{function.__name__} executed in {runtime} seconds\n")

        return result
    return wrapper
