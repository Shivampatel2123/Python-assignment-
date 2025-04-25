def create_list(list1, list2):
    return list(set(list1) & set(list2))

print(create_list([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
