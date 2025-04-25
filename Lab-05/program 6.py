temperatures_f = [32, 68, 77, 104, 212]
print("Temperatures in Fahrenheit:", temperatures_f)
temperatures_c = [(f - 32) * 5 / 9 for f in temperatures_f]
print("Temperatures in Celsius:", temperatures_c)
