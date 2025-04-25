with open("Q6_file1.txt", "r") as file1, open("Q6_file2.txt", "r") as file2, open("Q6_merged.txt", "w") as merged_file:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        if i < len(lines1):
            merged_file.write(lines1[i])
        if i < len(lines2):
            merged_file.write(lines2[i])

print("Files merged successfully into Q6_merged.txt.")
