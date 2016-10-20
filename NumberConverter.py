#############################################
#	COMPSCI 105 S2 C, 2016              #
#	Assignment 2 Question 1             #
#                                           #
#	@Luke Canes  	lcan812             #
#	@16/10/16                           #
#############################################

def display_intro():
    UPI = "lcan812"
    message = "*"*2 + " "*8 + "A Number Converter Program" + " "*8+ "*"*2 +"\n"+\
              "*"*2 + " Decimal --> Binary, Octal or Hexadecimal " + "*"*2 +"\n"+\
              "*"*2 + " "*16 + "by " + UPI + " "*16+ "*"*2
    print(message)

def converter(number, base):
    if base != 16:
        add = number % base
        if number <= 1:
            return str(number)
        else:
            return str(converter(number // base, base)) + str(add)
    else:
        digit_to_hex = "0123456689ABCDEF"
        if number < 16:
            return digit_to_hex[int(number)]
        mod = number % 16
        number /= 16
        return converter(number, base) + str(digit_to_hex(mod))
        
                    
def display_separator():
    lines = "*" * 46
    print(lines)

def display_menu():
    print("1. Convert to binary value")
    print("2. Convert to octal value")
    print("3. Convert to hexadecimal value")
    print("4. Quit the program")

def get_option(start,end):
    user_option = input("Please make a selection: ")
    while not user_option.isnumeric() or int(user_option) < start or int(user_option) > end:
        user_option = input("Invalid selection. Try again: ")
    return int(user_option)

def get_num():
    user_option = input("Please enter a positive integer: ")
    while not user_option.isnumeric() or int(user_option) <= 0:
        user_option = input("Invalid entry. Try again: ")
    return int(user_option)

def main():
    display_separator()
    display_intro()
    display_separator()
    display_menu()
    display_separator()
    option = get_option(1,4)
    while option != 4:
        dec_num = get_num()
        if option == 1:
            bin_number = converter(dec_num,2)
            print(dec_num,"is",bin_number,"in binary")
        if option == 2:
            oct_number = converter(dec_num,8)
            print(dec_num,"is",oct_number,"in octal")
        if option == 3:
            hexa_number = converter(dec_num,16)
            print(dec_num,"is",hexa_number,"in hexadecimal")
        display_separator()
        display_menu()
        display_separator()
        option = get_option(1,4)
        
main()
