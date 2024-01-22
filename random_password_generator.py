import random
print("Welcome to my Program")

print("Welcome Random Password Generator")
randomchars="ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnopqstuvxyz1234567890!@#$%^&*()"

#Get user input
number_of_password=int(input("Please Enter the number of password to be generated:"))
pwslen=int(input("Please Enter the lenght of the password needed:"))

#Generate password
print("Here are your randome password:")
for x in range(number_of_password):
    pwd=""
    for chars in range(pwslen):
        pwd=pwd+random.choice(randomchars)
    print(pwd)
