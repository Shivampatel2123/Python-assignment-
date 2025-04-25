import csv

with open("Q1.csv", "wb") as f:
    f.write(b"Name,Age,City\n")
    f.write(b"Alice,30,New York\n")
    f.write(b"Bob,25,Los Angeles\n")
with open("Q1.csv", "rb") as f:
    for line in f:
        print(line.decode().strip())
