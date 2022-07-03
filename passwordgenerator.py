import random

num = random.randint(8,15)
password = "Ac2"
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxwz@#$%&+?"
i = 0
while i < num:
    cho = random.randint(0,len(alp)-1)
    password += alp[cho]
    i+=1
print("Suggested Password is: \"",password,"\"")