# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi_calc = weight / (height * height)

if bmi_calc < 18.5:
    print(f'Your BMI is {bmi_calc}, you are underweight.')
elif bmi_calc < 25:
    print(f'Your BMI is {bmi_calc}, you have a normal weight.')
elif bmi_calc < 30:
    print(f'Your BMI is {bmi_calc}, you are slightly overweight.')
elif bmi_calc < 35:
    print(f'Your BMI is {bmi_calc}, you are obese.')
else:
    print(f'Your BMI is {bmi_calc}, you are clinically obese.')
