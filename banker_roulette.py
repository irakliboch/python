# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)


who_pays = random.randint(0, num_items - 1)
person_name = names[who_pays]

print(person_name)
