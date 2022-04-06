# The simple way


birth_year = input("What year were you born?")
current_year = 2022

age = current_year - int(birth_year)
print(age)

# The nicer Way
from datetime import date

current_year = date.today().year

while True:
    birth_year = input("What year were you born?")
    if birth_year.isdigit() == False or len(birth_year) != 4:
        print(f"Sorry, your answer of {birth_year} is incorrect, it should contain only 4 digits")
    elif current_year - int(birth_year) < 0:
        print(f"Looks like you still weren't born!, as we are  in year {current_year}")
    else:
        birth_year = int(birth_year)
        print(f"You are {current_year - birth_year} years old")
        break
