import random
x=int(input("Enter the start of the range"))
y=int(input("Enter the end of the range"))
z=int(input("Enter the number of random number to be generated"))
#to generate random number 👇🏽
rand_num=[random.randint(x,y)
          for _ in range(z)]
print(rand_num)