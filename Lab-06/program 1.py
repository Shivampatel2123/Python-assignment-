names = [("John",), ("Mike",), "Sarah", "Emma", ("David",), "Olivia", "Sophia"]
boys_count = sum(1 for name in names if isinstance(name, tuple))
girls_count = len(names) - boys_count
print(f"Number of boys: {boys_count}")
print(f"Number of girls: {girls_count}")

