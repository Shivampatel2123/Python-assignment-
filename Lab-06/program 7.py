tup = (10, 20, 30, 40)
tup_list = list(tup)  
tup_list.remove(30)  
tup = tuple(tup_list)

print("Tuple after deletion:", tup)
