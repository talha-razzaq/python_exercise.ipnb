# Python program to find the factorial of a number provided by the user.

#----------- Factorial ----------
#the product of all positive integers less than or equal to a given positive integer
# and denoted by that integer and an exclamation point. Thus, factorial seven is
# written 7!, meaning 1 × 2 × 3 × 4 × 5 × 6 × 7.


# To take input from the user

num = int(input("Enter the number here : "))

factorial = 1

# check if the number is negative, positive or zero

if num < 0:
    print("Sorry, factorial does not exist for negative number")

elif num == 0:
    print("The factorial of 0 is 1")

else:
    for i in range(1,num + 1):
        print(i)
        factorial = factorial * i
    print("The factorial  of ", num,"is ",factorial)

