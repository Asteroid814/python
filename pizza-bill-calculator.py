print("                welcome to pizza order code.")
a = input("which type of pizza size you wana order small , Medium , Large (S , M , L)::- ")
b = input("Wana Add Peperoni on it ? yes or no. (y / n )::- ")
c = input("wana add cheese on it yes or no ( y / n )::- ")

bill = 0
if a == "S":
    bill += 15
elif a == "M":
    bill += 20
else:
    bill += 25

if b == "y":
    if a == "S":
        bill += 2
    else:
        bill += 3

if c == "y":
    bill += 1

print(f"your total bill is ${bill}")
