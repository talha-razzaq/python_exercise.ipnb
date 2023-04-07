# Program to display the Fibonacci sequence up to n-th term

#### Fibonacci sequence ####
"""
The 9th number in the Fibonacci sequence is 21.
The Fibonacci sequence is a series of numbers in
which every number is the sum of the two previous
numbers. The first ten numbers of the Fibonacci 
sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34.
"""


# take user input
nterm = int(input("How many terms show : "))

#first two terms
n1, n2 = 0, 1

#count varible where "while loop" will be start 
count = 0


# if elif statement
if nterm <= 0:
    print("Please enter positive digits")

elif nterm == 1:
    print("Fibonacci sequence upto",nterm,":")
    print(n1)

else:
    print("Fibonacci sequence :")
    while count < nterm:  #In this loop start "count ...to... nterm" 
        print(n1)
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count += 1
