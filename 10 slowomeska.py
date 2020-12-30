from random import choice

words = ["aнтарктида","индустриализация","локомотив","амплитуда","процессор",]

word = choice (words)
print (word)

shuffle_word = list (word)
shuffle(shuffle_word)

game= True
while game:
    user_word = input("угадай слово:"+''.join(shuffle_word))

    if user_word == word:
        print ('угадал')
        word = choice(words).lower()
        shuffle_word = list(word)
        shuffle(shuffle_word)
    else:
        print ('не угадал')


