import os

os.chdir("/Users/sample/OneDrive/Masaüstü/new")

with open("sample.txt") as doc1:
    with open("sample2.txt", "w") as doc2:
        for line in doc1:
            doc2.write(line)

