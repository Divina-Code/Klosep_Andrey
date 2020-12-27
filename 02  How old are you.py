print("Hellow")
U_N = input ("what id your name  ?")
print("Hellow",U_N,"inyour name",len(U_N),'letters')
U_Y = int(input ("when you was born?"))
if len(str(U_N)) == 4:
    print(U_Y,"was a good year")
    a = 2020 - U_Y
    if a >= 100:

        print ("you're",a,"years old. how are you still alive?")
    else:
         print ("you're",a,"years old.")
else:
    print ("You make a little mistake")
