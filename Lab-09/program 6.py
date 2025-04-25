def create_list(n):
    return [(x, x**2, x**3) for x in range(1, n+1)]
end_point=int(input("Enter a end point"))

print(create_list(end_point))
