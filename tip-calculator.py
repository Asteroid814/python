print("welcome to a tip calculator.")
total_bill = float(input("full amount ? : $"))
tip = int(input("tip percentage? = $"))
split_into = int(input("how many peoples are splitting:? : = "))
a = tip / 100
b =  total_bill * a
c = total_bill + b
bill = round( c / split_into, 2) 
print(f"pay ${bill} each person")
