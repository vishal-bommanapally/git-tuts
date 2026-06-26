def merge_sort(arr):
    """
    Sorts the array using merge sort with slicing.
    Returns a new sorted list (does not modify the original).
    """
    if len(arr) <= 1:
        return arr
    
    # Divide: split into two halves using slicing
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])      # recursive on left slice
    right_half = merge_sort(arr[mid:])     # recursive on right slice
    
    # Conquer: merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two already-sorted lists into one sorted list.
    """
    result = []
    i = 0  # pointer for left
    j = 0  # pointer for right
    
    # Compare and take smaller element from left or right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements from left (if any)
    result.extend(left[i:])
    
    # Add any remaining elements from right (if any)
    result.extend(right[j:])
    
    return result


# Example usage
array = [4, 2, 4, 56, 523, 556, 80, 4, 3, 5, 2, 5, 3, 3, 6, 6]

sorted_array = merge_sort(array)
print("Original array:", array)
print("Sorted array:  ", sorted_array)