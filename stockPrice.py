from fractions import Fraction

def Get_Total_Dollars():
    while True:
        try:
            share_price_int = input("Enter price (dollars, numerator, denominator): ")
            value_array = share_price_int.split(" ")
            dollars = int(value_array[0])
            numerator = int(value_array[1])
            denominator = int(value_array[2])
            total = float(Fraction(numerator/denominator))
            return dollars, numerator, denominator, total
        except Exception:
            print("Invalid price!")

def Get_Shares():
    try:
        number_of_shares_int = int(input("Enter number of shares: "))
        return number_of_shares_int
    except Exception:
        print("Invalid number!")

while True:
    number_of_shares_int = Get_Shares()
    dollars, numerator, denominator, total = Get_Total_Dollars()
    calc = number_of_shares_int * (dollars + total)
    print("{} shares with market price {} {}/{} have the value {:.2f}".format(number_of_shares_int, dollars,numerator,denominator,calc))
    cont_str = input("Continue: ")
    if cont_str in 'yY':
        continue
    elif cont_str in 'nN':
        break
