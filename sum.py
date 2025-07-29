
num1 = (input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
total = num1 + num2
print(f"The sum of num1 and num2 is total.")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 + num2
    print("The sum is:", total)

except ValueError:
    print("Error: Please enter valid numbers only.")