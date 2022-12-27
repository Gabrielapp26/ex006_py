#Desafio 05
#Faça um programa que leia um número inteiro qualquer e mostre a sua tabuaba
print("Escreva um número e veja a sua tabuaba")
n = int(input("Número: "))
n0 = n*0
n1 = n*1
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n*10
print("Tabuada do {}".format(n))
print(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

#Outra forma de fazer o Desafio 05
num = int(input("Digite um número para ver a sua tabuada: "))
print('-'*15)
print('Tabuada do {}'.format(num))
print("{} x {:2} = {}".format(num, 1, num*1))
print("{} x {:2} = {}".format(num, 2, num*2))
print("{} x {:2} = {}".format(num, 3, num*3))
print("{} x {:2} = {}".format(num, 4, num*4))
print("{} x {:2} = {}".format(num, 5, num*5))
print("{} x {:2} = {}".format(num, 6, num*6))
print("{} x {:2} = {}".format(num, 7, num*7))
print("{} x {:2} = {}".format(num, 8, num*8))
print("{} x {:2} = {}".format(num, 9, num*9))
print("{} x {:2} = {}".format(num, 10, num*10))
print('-'*15)