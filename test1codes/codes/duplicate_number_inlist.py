def find_duplicates(nums):
  
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

num_ls = [1, 2, 3, 4, 5, 1, 2, 6, 7, 2]
print(find_duplicates(num_ls))
