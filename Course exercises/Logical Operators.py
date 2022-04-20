# Check is magician AND expert, print "you are a master magician"

# Check if  magician but not an expert, print "at least you are getting there"

# If not magician, print "You need magic powers"

is_magician = False
is_expert = True

# First way:

if is_magician == True and is_expert == True:
    print("You are a master magician")
elif is_magician == True and is_expert == False:
    print("At least you are getting there")
elif is_magician == False:
    print("You need magic powers")

# Second way

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you are getting there")
elif not is_magician:
    print("You need magic powers")
