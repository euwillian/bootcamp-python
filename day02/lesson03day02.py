age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# divisão inteira, para não vir números float
weeks_in_a_year = 365 // 7

weeks_left = (90 - int(age)) * weeks_in_a_year
print(f"You have {weeks_left} weeks left.")