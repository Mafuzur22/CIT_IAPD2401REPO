def find_median(numbers):
    if not numbers:
        raise ValueError("The list is empty. Cannot compute median.")
    
    sorted_numbers = sorted(numbers)
    
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        
        mid2 = sorted_numbers[n // 2]
        
        median = (mid1 + mid2) / 2
    
    return median
    
# n = odd
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(sorted(numbers))
print("Median:", find_median(numbers))

# n = even
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(sorted(numbers))
print("Median:", find_median(numbers))

