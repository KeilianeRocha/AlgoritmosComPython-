"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido."""

import random

aluno1 = str(input('1° aluno: '))
aluno2 = str(input('2° aluno: '))
aluno3 = str(input('3° aluno: '))
aluno4 = str(input('4° aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sort = random.choice(lista)
print('O alno sorteado foi {}'.format(sort))

