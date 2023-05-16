
#import the random module of python
import random

#taking user input for the lenght of the password
pass_len = int(input("enter the length of password"))

# inserting the possibilities of the character to be generated as passowrd
possibilities="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

#generating the password
password =  "".join(random.sample(possibilities,pass_len ))

#printing the generated password
print (password)