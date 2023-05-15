cash = input("Input the cash used: ")
price = input("Input the price: ")

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

quarters_return = 0
dimes_return = 0
nickles_return = 0
pennies_return = 0

left = float(cash) - float(price)

while left >= 0:
    if left > quarters:
        left = left - quarters
        quarters_return += 1
    elif left > dimes:
        left = left - dimes
        dimes_return += 1
    elif left > nickles:
        left = left - nickles
        nickles_return += 1
    else:
        left = left - pennies
        pennies_return += 1

print("The left overs count is:")
print("Quarters: " + str(quarters_return))
print("Dimes: " + str(dimes_return))
print("Nickles: " + str(nickles_return))
print("Pennies: " + str(pennies_return))
