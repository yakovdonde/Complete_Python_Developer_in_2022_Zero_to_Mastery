# Create a function that is going to take a list of integers and print the element that is both highest and even

l = [11, 10, 2, 3, 4, 8, 23, 24, 29]


def find_highest_even(x):
    '''
    accepts a list of integers and return the highest even number
    '''
    ll = []
    for i in x:
        if i % 2 == 0:
            ll.append(i)
    return f"the maximum even number in {x} is {max(ll)}"


print(find_highest_even(l))
print(find_highest_even([99, 100]))

