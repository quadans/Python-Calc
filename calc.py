num1 = float(input("Gebe Nummer 1 ein: "))
num2 = float(input("Gebe Nummer 2 ein: "))

print("Welche Operation soll verwendet werden? ")
operation = input("(1)+  (2)-  (3)*  (4)/ \n")

if operation == "1":
    result = (num1) + (num2)

if operation == "2":
    result = (num1) - (num2)

if operation == "3":
    result = (num1) * (num2)

if operation == "4":
    result = (num1) * (num2)

print(result)