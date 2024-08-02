linked_list = [1, 2, 3, 4]

print("Original List:")
print(" -> ".join(map(str, linked_list)) + " -> None")

def reverse_linked_list(lst):
    return lst[::-1]
    
reversed_list = reverse_linked_list(linked_list)

print("Reversed List:")
print(" -> ".join(map(str, reversed_list)) + " -> None")
