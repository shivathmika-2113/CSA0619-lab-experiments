
def max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        return max(arr[low], arr[high]), min(arr[low], arr[high])

    mid = (low + high) // 2

    max1, min1 = max_min(arr, low, mid)
    max2, min2 = max_min(arr, mid + 1, high)

    return max(max1, max2), min(min1, min2)


arr = [10, 5, 20, 8, 15]

maximum, minimum = max_min(arr, 0, len(arr)-1)

print("Maximum element:", maximum)
print("Minimum element:", minimum)
