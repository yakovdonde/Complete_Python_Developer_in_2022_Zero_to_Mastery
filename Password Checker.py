# Password checker

# The goals are:
# 1 - printing the username
# 2 - printing the hidden password in a form of astrix
# 3 - printing the password length


username = (input('Hi, please enter your username: \n'))
password = (input('Hi, please enter your password: \n'))
password_masked = "*" * len(password)
password_length = len(password)

print(f"Hey {username}, your password of {password_masked} is {password_length} characters long ")
