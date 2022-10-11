import random


a=1
b = 2

print(random.randint(1,99))

taille_tab = 10
tab = list()

for i in range(taille_tab):
    print(random.randint(1,99))

tab = list(range(taille_tab)) # list of integers from 1 to 99
                              # adjust this boundaries to fit your needs
random.shuffle(tab)
print(tab)