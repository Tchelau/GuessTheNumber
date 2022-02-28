from random import randint
from time import sleep

print("\033[1;34m""VOU PENSAR EM UM NÚMERO DE 0 A 5...""\033[0;0m")
sleep(2)
z = 0
y = 6
x = randint(0, 5)


sleep(2)

while y != x and z != 2:
    y = int(input("Em qual número eu pensei? "))
    print("\033[1;31m""PROCESSANDO...""\033[0;0m")
    sleep(2)
    z = z + 1
    if y == x:
        print("\033[0;32m""VOCÊ ME VENCEU!""\033[0;0m")
    else:
        print("\033[1;31m""NÃO FOI DESSA VEZ! ""\033[0;0m")

print("\033[1;34m""OBRIGADO POR JOGAR!""\033[0;0m")
