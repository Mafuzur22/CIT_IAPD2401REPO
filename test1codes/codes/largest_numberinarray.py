def find_largest_number(arr):
    if not arr:
        raise ValueError("The array is empty")
    
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    
    return largest
    
    
inparr = [6, 8, 5, 5, 3, 8, 3, 2, 6]
print(find_largest_number(inparr))
