weight = float(input("Enter your weight in Kg's :: "))
height = float(input("Enter your height in meter :: "))

BMI = round(weight / height * 2 , 2)
if BMI <= 18.5:
    print(f"you bmi is {BMI} and you are under weight")
elif BMI <= 25:
    print(f"you bmi is {BMI} and you are normal weight")
elif BMI <= 30:
    print(f"you bmi is {BMI} and you are over weight")
elif BMI <= 35:
    print(f"you bmi is {BMI} and you are  obese")
else:
    print(f"you bmi is {BMI} and you are clinically obese")
