
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i

        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


a = [6,3,2,7]

print(selection_sort(a))


# Time Complexity
# Always: O(n²)
            