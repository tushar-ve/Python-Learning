import os

files = os.listdir("data")

i =0
for file in files:
    if file.endswith(".txt"):
        print(file)
        os.rename(f"data/{file}", f"data/new{i}.txt")
        i = i+1