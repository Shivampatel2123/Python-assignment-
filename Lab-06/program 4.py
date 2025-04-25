food_items = [("Burger", 150), ("Pizza", 300), ("Pasta", 200), ("Sandwich", 100)]

sorted_items = sorted(food_items, key=lambda x: x[1], reverse=True)

print("Sorted food items:", sorted_items)
