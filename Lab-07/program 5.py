prices = {
    'apple': 30,
    'banana': 20,
    'carrot': 15,
    'orange': 25
}
quantity = {
    'apple': 3,
    'banana': 2,
    'carrot': 4,
    'orange': 5
}
total_bill = 0
for item in prices:
    if item in quantity:  
        total_bill += prices[item] * quantity[item]
print("Total bill:", total_bill)
