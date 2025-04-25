def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

def average(lst):
    if not lst:
        return 0
    return sum_list(lst) / len(lst)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Average:", average(nums))
