tuples_list = [(), (1, 2, 3), ("a", "b"), (), (5, 6)]

filtered_list = [tup for tup in tuples_list if tup]

print("List after removing empty tuples:", filtered_list)
