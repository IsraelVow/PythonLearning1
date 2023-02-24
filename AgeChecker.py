name = input('What is your name')
age = int(input("What is your age?"))

yearsto50 = 50 - age

if yearsto50 > 0:
    print ("Hello " + name.title() + " You have " + str(yearsto50) + " years, before you get to 50 years")
else:
    print ("Hello " + name.title() + " You were already 50, " + str(-yearsto50) + " years ago")
print ("bye")