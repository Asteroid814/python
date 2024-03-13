height = int(input("Enter your height in cm:: "))
age = int(input("Enter your age:: "))
if height >= 120:
    if age >= 18:
        print("pay $12")
    else:
        print("pay $7")
else:
    print("you need to be grow taller to ride this roller coster")
