def sanitize(lst):
    if not lst:
        return []
    head = 0 if lst[0] < 0 else lst[0]
    return [head] + sanitize(lst[1:])

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sanitized list:", sanitize(nums))
