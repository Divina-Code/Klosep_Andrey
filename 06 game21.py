import random
a = 0
b = 0
c = 0
a1 = False
c1 = False
a1 = False
print ("вместо да вводите 1 вместо нет вводите 2")
while a1 == False and c1 == False or b1 == False and c1 == False or b1 == False and a1 == False:
    if a < 21:
            a2 = int(input("желает ли игрок a взять карту"))
            if a2 == 1:
                 a = a + random.randint(2, 11)
                 print (a2)
                 print ("ок, теперь ход игрока b")
            elif a > 21:
                 print ("игрок выбывает")
            elif a2 ==2:
                 print ("ок, теперь ход игрока b")
                 a1 = True
            else:

                print ('повторюсь-"вместо да вводите 1 вместо нет вводите 2"')
    else:
        print ("игрок a неможет учавствовать в этом ходе")

    if b < 21:
        b2 = int(input("желает ли игрок b взять карту"))
        if b2 == 1:

             b = b + random.randint(2, 11)
             print (a2)
             print ("ок, теперь ход игрока с")
        elif a > 21:
                 print ("игрок выбывает")
        elif b2 ==2:
                print ("ок, теперь ход игрока с")
                b1 = True
        else:
                 print ('повторюсь-"вместо да вводите 1 вместо нет вводите 2"')
    else:
        print ("игрок b неможет учавствовать в этом ходе")
    if b < 21:
        c2 = int(input("желает ли игрок c взять карту"))
        if c2 == 1:

             c = c + random.randint(2, 11)
             print (a2)
             print ("подсчёт очков")
        elif c2 == 2:
                print ("подсчёт очков")
                с1 = True
        else:
                 print ('повторюсь-"вместо да вводите 1 вместо нет вводите 2"')
    else:
                print ("подсчёт очков")
    if a == 21:
        print ("игрок а выйграл")
        a1 = False
    elif a < 21:
        print ("количество очков у игрока а равно",a)
    else :
        print (" игрок а выбыл")
        a1 = False
    if c == 21:
        print ("игрок а выйграл")
        c1 = False
    elif c < 21:
        print ("количество очков у игрока c равно",c)
    else :
        print (" игрок c выбыл")
        c1 = False
    if b == 21:
        print ("игрок а выйграл")
        b1 = False

    elif a < 21:
        print ("количество очков у игрока b равно",b)
    else:
        print (" игрок а выбыл")

if c<a>b and a<=21:
    print ("выиграл а")
elif a<c>b and c<=21:
    print ("выиграл c")
elif c<b>c and b<=21:
    print ("выиграл b")
else:
    print ("опять что-то невразумительное")








