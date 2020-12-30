from random import randint
R_N = randint(100,999)
game = True
code = str(R_N)
Ri_N = 0
Ri_P = 0
while game:
    U_N = int(input('введите трёхзначное число\t'))
    Ri_N = 0
    if len (U_N)!=3:
        print('незнаю как ты но я знаю что это не трёхзначное число')
    elif not U_N.isdigit():
        print("где ты там увидел цифры?")
    elif
    else:
        for d in U_N:
            if d in code:
                Ri_N == 1
    print("вот столько цифр ты угадал", Ri_N)

