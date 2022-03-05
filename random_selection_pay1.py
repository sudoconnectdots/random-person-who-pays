import random

names_string = input("Give me  names, seperated by a comma , ")
names = names_string.split(",")

#num_items = len(names)
#random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today! god bless this is your day  :)")








