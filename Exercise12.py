def first_and_last(numbers):
    return [numbers[0], numbers[-1]]

a = [5, 10, 15, 20, 25]
new_list = first_and_last(a)

print("Original list:", a)
print("New list with only first and last elements:", new_list)