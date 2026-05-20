

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr



a = [2,5,1,6,7]

print(bubble_sort(a))


# Time Complexity
# Worst: O(n²)
# Best: O(n) (if already sorted with optimization)