x=int(input())
factorial=lambda x:x and x*factorial(x-1) or 1


print("Factorial of the",x ,"is",factorial(x))