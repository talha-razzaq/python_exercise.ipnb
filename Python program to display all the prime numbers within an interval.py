# Python program to display all the prime numbers within an interval

# Take user input
lower = int(input("Enter the lower digit : "))
upper = int(input("Enter the upper digit : "))

print("Prime numbers between", lower, "and",upper,"are : ")

# for loop and lower && upper varible
for num in range(lower, upper +1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break

        else:
            print(num)
