import numpy as np

def merge(arr, start_a, start_b, end_b):
    idx_a, idx_b = start_a, start_b
    arr_final = []
    
    # Merge both subarrays while both have elements
    while idx_a < start_b and idx_b <= end_b:
        if arr[idx_a] <= arr[idx_b]:
            arr_final.append(arr[idx_a])
            idx_a += 1
        else:
            arr_final.append(arr[idx_b])
            idx_b += 1

    # Append remaining elements from the first subarray
    while idx_a < start_b:
        arr_final.append(arr[idx_a])
        idx_a += 1

    # Append remaining elements from the second subarray
    while idx_b <= end_b:
        arr_final.append(arr[idx_b])
        idx_b += 1

    # Colocano elementos de volta no array inical.
    for i, val in enumerate(arr_final):
        arr[start_a + i] = val
    
    return arr


def mergeSort(arr, start, end):
    mid = (end + start) // 2
    
    if start < end:

        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)
	
    return merge(arr, 0, mid + 1, end)

# Array de números aleatórios.
arr = np.random.randint(100, size=20)
arr = list(arr.tolist())
print(arr)

print(mergeSort(arr, 0, len(arr) - 1))