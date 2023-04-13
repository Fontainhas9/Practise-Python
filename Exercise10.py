# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# common_elements = [num for num in a if num in b]

# print("Original lists:", a, "and", b)
# print("New list with only common elements:", common_elements)

import random
 
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in a if i in b]
print(result)