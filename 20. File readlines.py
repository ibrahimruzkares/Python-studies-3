with open("sample.py", "r") as folder:
    content = folder.readlines()
    for line in content:
        print(line, end = "")