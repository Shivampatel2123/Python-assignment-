import os

current_path = os.getcwd()
subdirectory = os.path.join(current_path, 'Q4')
if not os.path.exists(subdirectory):
    os.makedirs(subdirectory)
    print(f"Directory {subdirectory} created.")
else:
    print(f"Directory {subdirectory} already exists.")

source_file = os.path.join(current_path, 'Q3', 'Q3.py')
destination_file = os.path.join(subdirectory, 'Q3.py')
if os.path.exists(source_file):
    with open(source_file, 'r') as src:
        content = src.read()

    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"File copied from {source_file} to {destination_file}.")
else:
    print(f"Source file {source_file} does not exist.")

