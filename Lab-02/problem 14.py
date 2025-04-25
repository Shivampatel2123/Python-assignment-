def grade(marks):
    if marks == "Absent":
        return "NA"
    elif 0 <= marks <= 39:
        return "F"
    elif 40 <= marks <= 44:
        return "P"
    elif 45 <= marks <= 49:
        return "C"
    elif 50 <= marks <= 54:
        return "B"
    elif 55 <= marks <= 59:
        return "B+"
    elif 60 <= marks <= 69:
        return "A"
    elif 70 <= marks <= 79:
        return "A+"
    elif 80 <= marks <= 100:
        return "O"
s1=int(input("Enter marks of subject 1 "))
s2=int(input("Enter marks of subject 2 "))
s3=int(input("Enter marks of subject 3 "))
print("The total marks is",s1+s2+s3)
print("The average marks is",(s1+s2+s3)/3)
print("Grade for subject 1 is",grade(s1))
print("Grade for subject 2 is",grade(s2))
print("Grade for subject 3 is",grade(s3))
