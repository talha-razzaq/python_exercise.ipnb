# Sum of natural numbers up to num
"""What is Sum of natural numbers?
It means that all numbers which is smaller than num which takes from user.
For example: We take '5' than
1+2+3+4+5 = 15 natural number is 15"""

# Take user input
num = int(input("Enter the number : "))

# user if ... else statement

if num < 0:
    print("Please enter the positive number")

else:
    sum = 0

    # Use while loop for iterate until zero
    while (num > 0):
        sum += num
        num -= 1
    
    print("The sum is : ", sum)