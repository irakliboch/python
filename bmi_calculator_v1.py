# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_transformed = float(height)
weight_transformed = int(weight)


bmi = weight_transformed / (height_transformed * height_transformed)
print(round(bmi))

