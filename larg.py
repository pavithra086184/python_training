try:
    num = float(input("Enter a number: "))

    if num > 0:
        print("The number is positive.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")

except ValueError:
    print("Error: Please enter a valid number, not a string.")