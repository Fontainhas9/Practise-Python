# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# common_elements = []

# for num in a:
#     if num in b and num not in common_elements:
#         common_elements.append(num)

# print("Common elements between", a, "and", b, "are:", common_elements)

import random

list1 = random.sample(range(1, 30), 12)
list2 = random.sample(range(1, 30), 8)

common_elements = []

common_elements = [num for num in list1 if num in list2 and num not in common_elements]

print("List 1:", list1)
print("List 2:", list2)
print("Common elements between the two lists are:", common_elements)