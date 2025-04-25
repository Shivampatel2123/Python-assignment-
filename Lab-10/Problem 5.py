with open("Q5.txt", "r") as source_file:
    content = source_file.read()
    upper_content = content.upper()
    with open("Q5_copy.txt", "w") as destination_file:
        destination_file.write(upper_content)
    print("File copied and converted to uppercase.")
