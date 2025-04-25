names_set = set()

names_set.add("Alice")
names_set.add("Bob")
names_set.add("Charlie")
names_set.add("David")
names_set.add("Eve")

print("Set after adding names:", names_set)

names_set.remove("Charlie") 
names_set.add("CharlieUpdated")  

names_set.remove("Alice")
names_set.remove("Bob")

print("Updated names set:", names_set)
