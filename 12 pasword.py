from random import choice
sec = "!@#$%^&*(){}[]:;'\|?/.,_-qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM234567890"
long = int(input("какой длинны нужен код?"))
pas = " "
for a in range(long):
    pas += choice(sec)
print(pas)
