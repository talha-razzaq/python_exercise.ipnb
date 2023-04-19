# Python program to display the Fibonacci sequence

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
    
nterm = int(input("Enter the number : "))

if nterm <= 0:
    print("Please type the positive number!!!")

else:
    print("Fibonacci sequence: ")
    for i in range(nterm):
        print(recur_fibo(i))