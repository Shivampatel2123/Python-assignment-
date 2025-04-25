def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Reversed list:", reverse_list(nums))
