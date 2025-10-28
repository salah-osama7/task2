def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# Example Usage:
data = [40, 39, 94, 33, 25]
sorted_data = selection_sort(data)
print(sorted_data)