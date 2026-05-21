

def quick_sort(arr):


	if len(arr) <= 1:
		return arr

	pivot = arr[-1]
	left = []
	right = []

	for i in range(len(arr)-1):
		if arr[i] <= pivot:
			left.append(arr[i])
		else:
			right.append(arr[i])

	return quick_sort(left) + [pivot] + quick_sort(right)



a = [3,6,1,7]
print(quick_sort(a))


# Average: O(n log n) ⚡
# Worst: O(n²) 😬 (rare but possible)
