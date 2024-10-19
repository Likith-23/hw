def power_of8(number):
    # Check if the number is greater than 0
    if number <= 0:
        return False
    # Continuously divide the number by 8
    while number % 8 == 0:
        number //= 8
    # If the final result is 1, it is a power of 8
    return number == 1

number = int(input("ENTER A NUMBER: "))
if power_of8(number):
    print("The number is a power of 8 :)")
else:
    print("The number is not a power of 8 :(")