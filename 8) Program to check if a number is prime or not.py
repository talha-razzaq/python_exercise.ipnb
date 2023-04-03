# Program to check if a number is prime or not

"""What is prime number?

A prime number is a natural number that is greater than one and connot exactly 
divided on whole numbers likes 2,3,5,7,11,13,17,19,2,23,29 so on and so forth."""

# take user input 

num = int(input("Enter the number : "))

# define a varible

prime_number = False    # false means it value is zero

#use if else condition

if num == 1:
    print(num, "is not a prime number")

elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            prime_number = True     # prime_number varilbe assume it's value is 1
            break

if prime_number:        # prime_number varilbe assume it's value is 1
    print(num, "is not prime number")

else:
    print(num, "is a prime number")
