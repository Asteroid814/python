a = int(input("Enter the year you wana check for leap year:: "))

b = a % 4 

if b == 0:
    if b % 100 == 0:
        if b % 4 == 0:
            print("leap year")
    else:
        print("not a leap year")
else:
    print("it's  not an leap year")
