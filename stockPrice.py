# Enter number of shares: 100
# Enter price (dollars, numerator, denominator): 29 a b
# Invalid price!
# Enter price (dollars, numerator, denominator): 29 7 8
# 100 shares with market price 29 7/8 have value $2987.50
# Continue: y
# Enter number of shares: 1a
# Invalid number!
# Enter number of shares: 30
# Enter price (dollars, numerator, denominator): x 1 2
# Invalid price!
# Enter price (dollars, numerator, denominator): 89 1 2
# 30 shares with market price 89 1/2 have value $2685.00
# Continue: n

def Stock_Price():
    while True:
        number_of_shares_int = int(input("Enter number of shares: "))

        while True:
            try:
                share_price_int = input("Enter price (dollars, numerator, denominator): ")
                value_array = share_price_int.split(" ")
                dollars = int(value_array[0])
                numerator = int(value_array[1])
                denominator = int(value_array[2])
                break
            except ValueError:
                print("Invalid price!")
        #100 shares with market price 29 7/8 have value $2987.50
        calc = number_of_shares_int * dollars * float(numerator/denominator)
        print("{} shares with market price {} {}/{} have the value {}".format(number_of_shares_int, dollars,numerator,denominator,calc))
        cont_str = input("Continue: ")
        if cont_str in 'yY':
            continue
        elif cont_str in 'nN':
            break


Stock_Price()