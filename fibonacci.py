x=int(input()) #taking the input
fib = lambda x: x if x<=1 else fib(x-1)+fib(x-2) 
print([fib(i) for i in range(x)]) #to print the serires