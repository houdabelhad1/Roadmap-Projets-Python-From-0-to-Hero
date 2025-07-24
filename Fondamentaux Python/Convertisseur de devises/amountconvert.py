amount = float(input("Enter the amount in DH: \n"))
rate = float(input("Enter the conversion rate to Euro : \n"))
print(f"the amount is,{amount}!")
print(f"the the conversion rate is,{rate}!")
def convert(amount,rate):
    euroamount= amount * rate
    return euroamount
print(f"the amount converted is: {convert(amount,rate)}")