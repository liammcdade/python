usdcon = float(input("What is the price of the usd?: "))
eurocon = float(input("What is the price of the euro?: "))
gbpcon = float(input("What is the price of the gbp?: "))

bors = input("Would you like to buy or sell today? (b/s): ")
if bors == "b":
    commission = 0.05
elif bors == "s":
    commission = 0.07

currency1 = input("What currency would you like to convert to? euro, gbp, usd?: ")
currency2 = input("What currency would you like to convert from? euro, gbp, usd?: ")

amount = float(input("How much would you like to convert?: "))

if currency1 == "euro" and currency2 == "usd":
    result = amount * eurocon / usdcon

elif currency1 == "usd" and currency2 == "gbp":
    result = amount * usdcon / gbpcon
    

elif currency1 == "gbp" and currency2 == "euro":
    result = amount * gbpcon / eurocon

elif currency1 == "euro" and currency2 == "gbp":
    result = amount * eurocon / gbpcon

elif currency1 == "gbp" and currency2 == "usd":
    result = amount * gbpcon / eurocon

else:
    print("Invalid currency conversion.")
    exit()

commission_amount = result * commission
result -= commission_amount

print("Result:", result)
print("Commission:", commission_amount)

