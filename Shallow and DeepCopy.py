import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99
print("Original:", original)  # Output: [[99, 2], [3, 4]]
print("Shallow:", shallow)   # Output: [[99, 2], [3, 4]
original1 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original1)
deep[0][0] = 99
print("Original:", original1)  # Output: [[1, 2], [3, 4]]
print("Deep:", deep)       # Output: [[99, 2], [3, 4]]