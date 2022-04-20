picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


for ind, lists in enumerate(picture):
    for idx, ele in enumerate(picture[ind]):
        if ele == 0:
            picture[ind][idx] = " "
        elif ele == 1:
            picture[ind][idx] = "*"

for i in picture:
    print(i)
