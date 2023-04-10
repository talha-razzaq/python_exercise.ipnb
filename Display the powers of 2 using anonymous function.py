# Display the powers of 2 using anonymous function


# Uncomment code below to take input from the user

# use anonymous function

terms = int(input("How many terms : "))

print("The total terms are : ", terms)

result = list(map(lambda x: 2**x, range(terms)))

for i in range(terms):
    print("2 raise to power",i,"is",result[i])