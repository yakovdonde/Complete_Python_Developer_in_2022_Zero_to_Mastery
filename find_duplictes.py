# Find duplicates in list_1 without using sets

list_1 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for element in list_1:
    if list_1.count(element) > 1:
        if element not in duplicates:
            duplicates.append(element)
print(f"The following elements are not unique in list_1 and appear more than once: {duplicates}")
