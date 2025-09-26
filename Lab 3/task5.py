import os, shutil

def  filemanager_task():
    while True:
        path = input("Enter directory path: ").strip()
        if os.path.isdir(path):
            break
        print("invalid directory, try again")

    backup_dir = os.path.join(path, "backup")
    os.makedirs(backup_dir, exist_ok=True)

    count = 0
    for file in os.listdir(path):
        if file.endswith(".txt"):
            shutil.copy(os.path.join(path, file), backup_dir)
            count += 1

    print(f" {count} files copied")