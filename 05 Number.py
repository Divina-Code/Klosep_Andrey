import random
i = False
num = random.randint(1, 100)
while i != True :
    op = int(input("я загодал число от одного до ста, угадай его"))
    if num == op :
        print ("хе-хе, неплохо")
        i = True
    elif num < op <= 100:
        print ("перебор")
    elif op == 0:
        print ("жаль что ты не смог угадать. я загадывал число", num)
        i = True

    elif num > op >=1 :
        print ("маловато")
    else:
        print ("Что в фразе 'от 1 до 100' было непонятно?")


print ("ну вот и конец")
