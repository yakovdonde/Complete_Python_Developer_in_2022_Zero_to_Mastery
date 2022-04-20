# Create a script that enumerates a list of numbers 1 to 100 and print the index of number 50

for _, num in enumerate(list(range(100))):
    if num == 50:
        print(f"The index of number 50 is {_}")
