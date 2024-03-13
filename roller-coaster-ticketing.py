height = int(input("Enter your height in cm:: "))
age = int(input("Enter your age:: "))
if height >= 120:
    if age <= 12:
        bill = 12
        print("child tickets are of $5")
    elif age <= 18:
        bill = 7
        print("youth tickets are of  $7")
    if age >= 45 and age <= 55:
        print("Everythong is gona be OK. and have a free ride with us .)
    else:
        bill = 12
        print("adult tickets are $12")
    
    want_pic = input("DO you want a pic (yes or no):: ")
    if want_pic == "yes":
        bill += 3
    print(f"your total bill is ${bill}")
    
else:
    print("you need to be grow taller to ride this roller coster")
