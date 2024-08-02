def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    char_count1 = {}
    char_count2 = {}
    for char in str1:  
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1
    
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    
   
    return char_count1 == char_count2


print(are_anagrams("Listen", "Silent"))
print(are_anagrams("Hello", "World")) 
