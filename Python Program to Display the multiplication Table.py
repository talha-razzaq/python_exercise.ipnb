
# Multiplication table (from 1 to so on.....) in Python

# To take input from the user

num = int(input("Display multiplication table of? "))

# Use for loop for this purpose

for i in range(1, 10+1):   # We can do here (1, 11)
    print(num,"*",i,"=", num *i)