user_dta = {
    "admin" : "ytrewq321",
    "user" : "000,"
}

while True:
    answer = input("ты тут впервые?").upper()
    if answer == "N":
        data = input("введи пароль").split()
        if len (data) == 2:
            login = data[0]
            password = data[1]
            if user_dta.get(login) == None:
                user_dta[login] = password
            else:
                print ('такой логин уже занят')
        else:
            print ("что-то нетак")

