
def subset_sums(arr):
    sums = [0]
    for x in arr:
        sums += [s + x for s in sums]
    return sums

arr = [3, 4, 5, 2]
target = 9

mid = len(arr) // 2

left = subset_sums(arr[:mid])
right = subset_sums(arr[mid:])

found = False

for x in left:
    if target - x in right:
        found = True
        break

if found:
    print("Subset with given sum exists")
else:
    print("Subset with given sum does not exist")
