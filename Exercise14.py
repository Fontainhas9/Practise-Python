# Using loops
def remove_duplicates_loop(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

# Using sets
def remove_duplicates_set(input_list):
    return list(set(input_list))

# Example usage
input_list = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 6]
print(remove_duplicates_loop(input_list))
print(remove_duplicates_set(input_list))
