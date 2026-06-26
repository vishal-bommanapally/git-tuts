def insertion_sort(arr):
    """
    Insertion Sort: Builds sorted array one element at a time
    Time: O(n²) average/worst, O(n) best
    Space: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    """
    Selection Sort: Repeatedly finds minimum and places it at beginning
    Time: O(n²) all cases
    Space: O(1)
    """
    for i in range(len(arr)):
        # Find minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap found minimum with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly swaps adjacent elements if in wrong order
    Time: O(n²) average/worst, O(n) best
    Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps, array is sorted
        if not swapped:
            break
    return arr


# Example usage
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", test_array)
    print("Insertion sort:", insertion_sort(test_array.copy()))
    print("Selection sort:", selection_sort(test_array.copy()))
    print("Bubble sort:", bubble_sort(test_array.copy()))
    
    
    
    
    
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j] # shift right
            j -=1

        arr[j+1] = key  # idhi  last lo manam select chesina element 
        #ni it's place lo position pettali 

array = [14,9,15,12,6,8,13]

insertion_sort(array)
print(array)


