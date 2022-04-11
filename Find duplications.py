# Find duplications in 2 lists

# 1st way

l1 = [1, 2, 3, 4, 5, 6]
l2 = [5, 6, 7, 8, 9, 10]
l3 = []

for x in l1:
    for y in l2:
        if x == y:
            l3.append(x)
if len(l3) > 0:
    print(f"The duplicates of the 2 lists are {l3}")
else:
    print("No duplicates found in the 2 ")

# 2nd Way


l1 = list(range(0, 100, 2))
l2 = list(range(0, 100, 3))
l3 = []

for x in l1:
    for y in l2:
        if x == y:
            l3.append(x)
if len(l3) > 0:
    print(f"The duplicates of the 2 lists are {l3}")
else:
    print("No duplicates found in the 2 ")
