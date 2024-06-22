#1) Escreva um programa que lê uma frase e uma String antiga e uma String nova. O programa deve imprimir uma String contendo a frase original, mas com a última ocorrência da String antiga substituída pela String nova.
#Exemplo:
#Frase: "Quem parte e reparte fica com a maior parte"
#String antiga: "parte"
#String nova: "parcela"
#Resultado a ser impresso no programa principal: "Quem parte e reparte fica com a maior parcela"

ant = 'quem parte e reparte, fica com a maior parte'
me, io = ant.split(',')
nov = io.replace('parte','parcela')
print(me,nov)

#2) Faça um programa que lê uma String que representa uma cadeia de DNA e gera a cadeia complementar.
#Exemplo:
 #Entrada: AATCTGCAC
 #Saída: TTAGACGTG

entrada = 'AATCTGCAC' 
vazia = ''
for i in entrada:
    if i == 'A':
        vazia += 'T'
    elif i == 'T':
        vazia += 'A'
    elif i == 'C':
        vazia += 'G'
    elif i == 'G':
        vazia += 'C'
print(vazia)

#3) Faça um programa que lê uma frase e retorna o número de palavras que a frase contém. Considere que a palavra pode começar e/ou terminar por espaços.

frase = "eu sou o melhor"
frase1 = frase.replace(' ','')
cont = len(frase1)
print(cont)

#4) Faça um programa que lê uma frase e substitui todas as ocorrências de espaço por "#".

frase = "eu sou o melhor"
frase1 = frase.replace(' ','#')
print(frase1)

#5) Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma é igual à outra quando lida de traz para frente.
#Exemplo: amor e roma.
frase1 = input('digite a primeira palavra').upper()
frase2 = input('digite a segunda palavra').upper()
invert = frase2[::-1]
if frase1 ==invert:
     print('palíndromas mútuas')
else:
      print('não são palíndromas mútuas')

#6) Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. Por exemplo, "Iracema" é um anagrama para "America". Escreva um programa que decida se uma String é um anagrama de outra String, ignorando os espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, "a" = "A".

fra1 = input("digite a primeira frase")
fra2 = input("digite a segunda frase")
frase1 = fra1.replace(' ','').lower()
frase2 = fra2.replace(' ','').lower()
invert = frase2[::-1]
if frase1 == invert:
       print(fra1,'é um anagrama para', fra2)
else:
      print('não é um anagrama')
#7) Faça um programa que leia o nome do usuário e mostre o nome de traz para frente, utilizando somente letras maiúsculas.
#Exemplo:
#Nome = Swainstainger
#Resultado gerado pelo programa:
#REGNIATSNIAWS

frase1 = input('digite a primeira palavra').upper()
invert = frase1[::-1]
print(invert)

#8) Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas.
#Exemplo:
#Nome =Vanessa
#Resultado gerado pelo programa:
#V
#VA
#VAN
#VANE
#VANES
#VANESS
#VANESSA

frase1 = input('digite a primeira palavra').upper()
for i in range(1,len(frase1)+1):
        print(frase1[:i])

#9) Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada invertida, usando apenas letras maiúsculas.
#Exemplo:
#Nome =Vanessa
#Resultado gerado pelo programa:
#VANESSA
#VANESS
#VANES
#VANE
#VAN
#VA
#V

frase1 = input('digite a primeira palavra: ').upper()
while len(frase1) > 0:
       print(frase1)
       frase1 = frase1[:-1]

#10) Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e imprima a data como mês escrito por extenso.
#Exemplo:
#Data = 20/02/1995
#Resultado gerado pelo programa:
#Você nasceu em 20 de fevereiro de 1995

meses=['','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro' ,'novembro','dezembro']
dia,mes,ano = input('digite sua data').split('/')
num =int(mes)
atu = meses[num]
print('voçê nasceu em',dia,'de',atu,'de',ano)

#11) Faça um programa que leia 2 Strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas Strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#Exemplo:
#String 1: Brasil Hexa 2026
#String 2: Brasil! Hexa 2026!
#Tamanho de "Brasil Hexa 2026": 16 caracteres
#Tamanho de "Brasil! Hexa 2026!": 18 caracteres
#As duas strings são de tamanhos diferentes.
#As duas strings possuem conteúdo diferente.

string1 = input('digite uma frase: ')
string2 = input('digite outra frase: ')
print('O tamanho de "',string1,'"é de', len(string1),'caracteres')
print('O tamanho de "',string2,'" é de', len(string2),'caracteres' )
if len(string1) == len(string2):
        print('As duas strings são do mesmo tamanho')
        if string1 == string2:
            print('As duas strings são iguais')
        else:
            print('As duas strings possuem conteúdo diferente')
else:
    print('As duas strings são de tamanhos diferentes')
    print('As duas strings possuem conteúdo diferente')

#12) Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#Exemplo:
#F
#U
#L
#A
#N
#O
string1 = input('digite seu nome: ')
for i in range (len(string1)):
       print(string1[i])

#13) Dado uma String com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#a. quantos espaços em branco existem na frase.
#b. quantas vezes aparecem as vogais a, e, i, o, u.

string1 = input('digite uma frase: ')
str1 = string1.lower()
branco = 0
vogais = [0,0,0,0,0]
for i in str1:
      if i == ' ':
            branco += 1
      if i == 'a':
            vogais[0] += 1
      if i == 'e':
            vogais[1] += 1
      if i == 'i':
            vogais[2] += 1
      if i == 'o':
            vogais[3] += 1
      if i == 'u':
            vogais[4] += 1
print('existe', branco, 'espeços em branco')
print('contagem de vogais')
print('a',vogais[0])
print('e',vogais[1])
print('i',vogais[2])
print('o',vogais[3])
print('u',vogais[4])

#14) Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
#Exemplo:
#Telefone: 461-0133
#Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
#Telefone corrigido sem formatação: 34610133
#Telefone corrigido com formatação: 3461-0133

string = input('digite seu telefone: ')
remov = string.replace('-','')
if len(remov) == 7:
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente')
    tel = '3'+ remov
    print(tel)
    telefone = tel[:4] + '-' + tel[4:]
    print('numero formatado',telefone)
elif len(remov) == 8:
    telefone = remov[:4] + '-' + remov[4:]
    print('numero formatado',telefone)
else:
    print('vpçê digitou mais de 8 digitos ou menos de 7')

#15) Escreva uma função que receba um texto e retorne um dicionário com a frequência de cada palavra, desconsiderando a pontuação e diferenças entre maiúsculas e minúsculas.

import string
def contar(texto):
    texto1 = texto.translate(str.maketrans('', '', string.punctuation))
    min = texto1.lower()
    palavras = min.split()
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1   
    return frequencia
texto = "Olá, mundo! Olá a todos. Este é um texto de exemplo. Texto de exemplo!"
frequencia = contar(texto)
print(frequencia)

#16) Escreva uma função que substitua palavras censuradas em um texto por asteriscos (*), mantendo o comprimento das palavras censuradas. Pergunte ao usuário quais são as palavras censuradas.
def censurar(texto, palavras):
    for palavra in palavras:
        texto = texto.replace(palavra, '*' * len(palavra))
    return texto
def pri():
    texto = input("Digite o texto: ")
    palavras = input("Digite as palavras a serem censuradas, separadas por vírgula: ").split(',')
    texto_censurado = censurar(texto, palavras)
    print("Texto censurado:", texto_censurado)
pri()

#17) Crie uma função que expanda abreviações em um texto baseado em um dicionário de abreviações. Crie uma Matriz de abreviações, contendo a abreviação e a palavra completa (sem abreviações). Quando o texto for inserido, apresente o texto sem as abreviações originais.

def exp(texto, abreviacao):
    for x , y in abreviacao.items():
        texto = texto.replace(x,y)
    return texto
def abr():
    abreviacao = {
        "vc": "você",
        "tb": "também",
        "pq": "porque",
        "q": "que",
        "td": "tudo",
        "obg": "obrigado",
    }
    texto = input("Digite o texto com abreviações: ")
    texto_expandido = exp(texto, abreviacao)
    print("Texto expandido:", texto_expandido)
abr()

#18) Implemente um algoritmo de compressão de string que utilize a contagem de caracteres repetidos (por exemplo, "aaabbc" se torna "a3b2c1").

def comp_string(s):
    comp = []
    count = 1
    prev = s[0]
    for char in s[1:]:
        if char == prev:
            count += 1
        else:
            comp.append(prev + str(count))
            prev = char
            count = 1
    comp.append(prev + str(count))
    comp_string = ''.join(comp)
    return comp_string if len(comp_string) < len(s) else s
def main():
    texto = input("Digite a string a ser comprimida: ")
    texto = comp_string(texto)
    print("String comprimida:", texto)
main()

#19) Escreva uma função que inverta a ordem das palavras em uma frase, mantendo a ordem dos caracteres dentro de cada palavra.

def invert(frase):
    pala = frase.split()
    invert = pala[::-1]
    frasei = ' '.join(invert)
    return frasei
frase = input('digite a frase')
inverte = invert(frase)
print(inverte)

#20) Escreva um algoritmo que verifique se um e-mail é válido quanto a sua forma. Exemplo: jean@zahn.com é um e-mail válido, mas jean@zahn e jeanzahn.com não são e-mails válidos.

import re
def veri (email1, email2):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email1) and re.match(padrao, email2):
        return True
    return False
email1 = input('digite um email')
email2 = "usuario@dominio.com"
if veri(email1, email2):
    print(email1, 'é um email válido')
else:
    print(email1, 'é um email inválido')

#21) Crie uma função que normalize um texto, removendo acentos, convertendo para minúsculas e removendo caracteres especiais.

import string
import unicodedata
def remover(texto):
    texto1 = unicodedata.normalize('NFD', texto)
    sem_acentos = ''.join(c for c in texto1 if unicodedata.category(c) != 'Mn')
    return sem_acentos
def normalizar(texto):
    novo ={}
    texto1 = texto.translate(str.maketrans('', '', string.punctuation))
    min = texto1.lower() 
    textosem = remover(min)
    novo = textosem
    return novo
texto = "Olá, mundo! Olá a todos. Este é um texto de exemplo. Texto de exemplo!"
novo = normalizar(texto)
print(novo)

#22) Escreva uma função que verifique se os parênteses em uma string estão equilibrados (considerando também colchetes e chaves).

def verificar(s):
    pares = {')': '(', ']': '[', '}': '{'}
    pilha = []
    for i in s:
        if i in pares.values():
            pilha.append(i)
        elif i in pares.keys():
            if not pilha or pilha[-1] != pares[i]:
                return False
            pilha.pop()
    return not pilha
s = input('digite o texto')
print(verificar(s))

#23) Faça um programa que contém uma função que recebe um número inteiro que corresponde a um mês do ano e retorna o nome desse mês. Por exemplo, se o mês informado como parâmetro for 1 a função deverá retornar "janeiro", se o mês enviado como parâmetro for 2 a função deverá retornar "fevereiro" e assim por diante.

def mes(data):
    meses = ['','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','setembro','outubro','Novembro','Dezembro']
    if 1 <= data <= 12:
        return meses[data]
    else:
        return "Número do mês inválido. Deve ser entre 1 e 12."
data = int(input('Digite seu mes com numero inteiro'))
print(mes(data))

#24) Faça uma função que informe o status do aluno a partir da sua média de acordo com a tabela a seguir:
#Nota acima de 6 → “Aprovado”
#Nota entre 4 e 6 → “Verificação Suplementar”
#Nota abaixo de 4 → “Reprovado”

def media(med):
    if med >= 6:
        return 'Aluno Aprovado'
    elif med < 6 and med >= 4:
        return 'Verificação Suplementar'
    else:
        return 'Aluno Reprovado'
med = float(input('Qual a mdedia do aluno'))
print(media(med))

#25) Faça uma função para verificar se um ano é bissexto ou não. Utilize a seguinte regra: Um ano bissexto é divisível por 4, mas não por 100, ou então se é divisível por 400. Exemplo: 1988 é bissexto pois é divisível por 4 e não é por 100; 2000 é bissexto porque é divisível por 400.
#A função deve retornar True caso o ano seja bissexto, e False caso contrário.

def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
ano = int(input('Digite o ano'))

print(bissexto(ano))
#26) Faça um programa que, dado uma figura geométrica que pode ser uma circunferência, triângulo ou retângulo, calcule a área e o perímetro da figura O programa deve primeiro perguntar qual o tipo da figura:
#(1) circunferência
#(2) triângulo
#(3) retângulo
#Dependendo do tipo de figura, ler o (1) tamanho do raio da circunferência; (2) tamanho de cada um dos lados do triângulo; (3) tamanho dos dois lados retângulos.
import math
def circunferencia(raio):
    area = math.pi * raio ** 2
    perimetro = 2 * math.pi * raio
    return area, perimetro
def triangulo(lado1, lado2, lado3):
    s = (lado1 + lado2 + lado3) / 2
    area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
    perimetro = lado1 + lado2 + lado3
    return area, perimetro
def retangulo(lado1, lado2):
    area = lado1 * lado2
    perimetro = 2 * (lado1 + lado2)
    return area, perimetro
def main():
    print("Escolha o tipo da figura geométrica:")
    print("(1) Circunferência")
    print("(2) Triângulo")
    print("(3) Retângulo")
    tipo = int(input("Digite o número correspondente ao tipo da figura: ")) 
    if tipo == 1:
        raio = float(input("Digite o tamanho do raio da circunferência: "))
        area, perimetro = circunferencia(raio)
        print(f"Área da circunferência: {area:.2f}")
        print(f"Perímetro da circunferência: {perimetro:.2f}")
    elif tipo == 2:
        lado1 = float(input("Digite o tamanho do primeiro lado do triângulo: "))
        lado2 = float(input("Digite o tamanho do segundo lado do triângulo: "))
        lado3 = float(input("Digite o tamanho do terceiro lado do triângulo: "))
        area, perimetro = triangulo(lado1, lado2, lado3)
        print(f"Área do triângulo: {area:.2f}")
        print(f"Perímetro do triângulo: {perimetro:.2f}")
    elif tipo == 3:
        lado1 = float(input("Digite o tamanho do primeiro lado do retângulo: "))
        lado2 = float(input("Digite o tamanho do segundo lado do retângulo: "))
        area, perimetro = retangulo(lado1, lado2)
        print(f"Área do retângulo: {area:.2f}")
        print(f"Perímetro do retângulo: {perimetro:.2f}")
    else:
        print("Tipo de figura inválido. Por favor, escolha 1, 2 ou 3.")
main()

#27) O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos. Faça o programa que lê o valor de N e M e informa o número de combinações possíveis.
#a. Número de combinações é igual a 𝑁!/(𝑀! ∗ (𝑁 − 𝑀)!)

def combinacoes(N, M):
    resultado = 1
    k = min(M, N - M)
    for i in range(k):
        resultado = resultado * (N - i) // (i + 1)
    return resultado
def main():
    N = int(input("Digite o número total de alunos (N): "))
    M = int(input(f"Digite o número de alunos em um dos grupos (M menor ou igual a {N}): "))
    if M < 0 or M > N:
        print("Número inválido para M. M deve ser maior ou igual a 0 e menor ou igual a N.")
    else:
        num_combinacoes = combinacoes(N, M)
        print(f"O número de combinações possíveis é: {num_combinacoes}")
main()

#28) Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a conclusão da soma, o novo estado da memória passa a ser 8.
#Estado da memória: 0
#Opções:
#(1) Somar
#(2) Subtrair
#(3) Multiplicar
#(4) Dividir
#(5) Limpar memória
#(6) Sair do programa
#Qual opção você deseja?

def somar(memoria, numero):
    return memoria + numero
def sub(memoria, numero):
    return memoria - numero
def mul(memoria, numero):
    return memoria * numero
def div(memoria, numero):
    if numero != 0:
        return memoria / numero
    else:
        print("Erro: Divisão por zero!")
        return memoria
def limpar():
    return 0
def main():
    memoria = 0
    while True:
        print(f"Estado da memória: {memoria}")
        print("Opções:")
        print("(1) Somar")
        print("(2) Subtrair")
        print("(3) Multiplicar")
        print("(4) Dividir")
        print("(5) Limpar memória")
        print("(6) Sair do programa")
        opcao = input("Qual opção você deseja? ")
        if opcao == '1':
            numero = float(input("Digite o número para somar: "))
            memoria = somar(memoria, numero)
        elif opcao == '2':
            numero = float(input("Digite o número para subtrair: "))
            memoria = sub(memoria, numero)
        elif opcao == '3':
            numero = float(input("Digite o número para multiplicar: "))
            memoria = mul(memoria, numero)
        elif opcao == '4':
            numero = float(input("Digite o número para dividir: "))
            memoria = div(memoria, numero)
        elif opcao == '5':
            memoria = limpar()
        elif opcao == '6':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")
        print(f"Novo estado da memória: {memoria}")
        print()
main()

#29) Escreva uma função que receba dois números como parâmetros e retorne a soma deles.

def somar(n1, n2):
    return n1+n2
n1 = float(input('digite um numero'))
n2 = float(input('digite um numero'))
print(somar(n1,n2))

#30) Escreva uma função que calcule o fatorial de um número inteiro.

def fato(n):
    if n < 0:
        return "Fatorial não definido para números negativos"
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial
n = int(input('digite um numero'))
print(fato(n))

#31) Escreva uma função que gere o n-ésimo número da sequência de Fibonacci.

def fibo(seq):
    n1 =0
    n2 =1
    print(n1)
    print(n2)
    cont = 3
    while cont <= seq:
        n3 = n2 + n1
        print(n3)
        n1 = n2
        n2 = n3
        cont +=1
seq = int(input("Digite quantas sequencias"))
print(fibo(seq))    

#32) Escreva uma função que verifique se um número é primo.

def primo(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n= int(input('Digite um numero'))
print(primo(n))

#33) Escreva uma função que conte o número de vogais em uma string.

def vogais(s):
    vogais = "aeiouAEIOU"
    contador = 0
    for i in s:
        if i in vogais:
            contador += 1
    return contador
texto = input('digite uma palavra')
numero = vogais(texto)
print(f"O número de vogais em '{texto}' é: {numero}")

#34) Escreva uma função que ordene uma lista de números em ordem crescente sem usar métodos embutidos de ordenação.

def lista(lista1):
    for i in range(len(lista1)):
        min = i
        for j in range(i + 1, len(lista1)):
            if lista1[j] < lista1[min]:
                min = j
        lista1[i], lista1[min] = lista1[min], lista1[i]  
    return lista1
numeros = [64, 34, 25, 12, 22, 11, 90]
ord = lista(numeros)
print("Lista ordenada:", ord)

#35) Escreva uma função que calcule a média de uma lista de números.

def lista(nu):
    res = sum(nu)/len(nu)
    return res
nu = [6, 10, 20, 30]
print(lista(nu))

#36) Escreva uma função que conte o número de palavras em uma string.

def conta(texto):
    pala = texto.split()
    cont = len(pala)
    return cont
texto = input('digite um texto')
print(conta(texto))

#37) Escreva uma função que converta um número de uma base para outra (por exemplo, binário para decimal).

def trans(binario):
    decimal = 0
    potencia = 0
    for i in reversed(binario):
        if i == '1':
            decimal += 2 ** potencia
        potencia += 1
    return decimal
binario = input('digite um valor binario')
decimal =trans(binario)
print(f"O número binário {binario} convertido para decimal é: {decimal}")

#38) Escreva uma função que calcule a distância euclidiana entre dois pontos em um espaço n-dimensional.

import math
def dis(ponto1, ponto2):
    if len(ponto1) != len(ponto2):
        raise ValueError("Os pontos devem ter o mesmo número de dimensões")
    soma = sum((p1 - p2) ** 2 for p1, p2 in zip(ponto1, ponto2))
    return math.sqrt(soma)
pontoA = [1, 2, 3]
pontoB = [4, 5, 6]
distancia = dis(pontoA, pontoB)
print(f"A distância euclidiana entre {pontoA} e {pontoB} é {distancia}")

#39) Implemente o algoritmo de ordenação Mergesort como uma função. Pesquisar o funcionamento do Mergesort.

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = mergesort(lista[:meio])
    direita = mergesort(lista[meio:])
    return merge(esquerda, direita)
def merge(esquerda, direita):
    resultado = []
    i, j = 0, 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado
lista = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = mergesort(lista)
print(f"Lista original: {lista}")
print(f"Lista ordenada: {lista_ordenada}")

#40) Escreva uma função que gere uma lista dos primeiros n números primos.

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime(n):
    primos = []
    num = 2 
    while len(primos) < n:
        if primo(num):
            primos.append(num)
        num += 1
    return primos
n = int(input('Digite a quantidade de numeros primos'))
lista = prime(n)
print(f"Os primeiros {n} números primos são: {lista}")

#41) Escreva uma função que remova elementos duplicados de uma lista enquanto mantém a ordem original dos elementos.

def remo(lista):
    dupli = []
    vistos = set()
    for item in lista:
        if item not in vistos:
            dupli.append(item)
            vistos.add(item)
    return dupli
lista = [1, 2, 2, 3, 4, 4, 5, 1, 6]
dupli = remo(lista)
print(f"Lista original: {lista}")
print(f"Lista sem duplicados: {dupli}")

#42) Escreva uma função que verifique se uma string é uma subsequência de outra string.

def sub(s1, s2):
    itera = iter(s2)
    return all(i in itera for i in s1)
s1 = "abc"
s2 = "aebdc"
print(f"'{s1}' é uma subsequência de '{s2}': {sub(s1, s2)}")
s1 = "axc"
s2 = "aebdc"
print(f"'{s1}' é uma subsequência de '{s2}': {sub(s1, s2)}")

#43) Escreva uma função que encontre a interseção de duas listas (elementos comuns a ambas as listas).

def inte(lista1, lista2):
    conj1 = set(lista1)
    conj2 = set(lista2)
    intersecao = conj1.intersection(conj2)
    return list(intersecao)
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = inte(lista1, lista2)
print(f"A interseção das listas {lista1} e {lista2} é: {resultado}")

#44) Escreva uma função que calcule a potência de um número dado uma base e um expoente (sem usar operadores de potência embutidos).

def pot(base, expoente):
    if expoente == 0:
        return 1
    elif expoente < 0:
        base = 1 / base
        expoente = -expoente
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado
base = int(input('Digite o valor da base'))
expoente = int(input('Digite o valor do expoente'))
print(f"{base} elevado a {expoente} é {pot(base, expoente)}")

#45) Escreva uma função que verifique se uma matriz é um quadrado mágico (todas as linhas, colunas e diagonais têm a mesma soma).

def quadrado(matriz):
    n = len(matriz)
    if n == 0 or any(len(linha) != n for linha in matriz):
        return False
    soma = sum(matriz[0])  
    for i in range(n):
        if sum(matriz[i][j] for j in range(n)) != soma:
            return False
        if sum(matriz[j][i] for j in range(n)) != soma:
            return False
    if sum(matriz[i][i] for i in range(n)) != soma:
        return False
    if sum(matriz[i][n - 1 - i] for i in range(n)) != soma:
        return False
    return True
matriz = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]]
print(f"A matriz é um quadrado mágico: {quadrado(matriz)}")

#46) Escreva uma função que combine duas strings intercalando seus caracteres. Se uma string for mais longa que a outra, anexe o restante ao final.

def comb(str1, str2):
    resultado = []
    tam = max(len(str1), len(str2))
    for i in range(tam):
        if i < len(str1):
            resultado.append(str1[i])
        if i < len(str2):
            resultado.append(str2[i])
    return ''.join(resultado)
str1 = input('digite a sequencia')
str2 = input('digite a sequencia')
resultado = comb(str1, str2)
print(f"A combinação de '{str1}' e '{str2}' é '{resultado}'")

#47) Escreva uma função que calcule o determinante de uma matriz 2x2.

def matr(matriz):
    if len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
        raise ValueError("A matriz não é uma matriz 2x2 válida.")
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]
    determinante = a*d - b*c
    return determinante
matriz = [
    [1, 2],
    [3, 4]]
det = matr(matriz)
print(f"O determinante da matriz {matriz} é {det}")

#48) Escreva uma função que verifique se uma string é um pangrama (contém todas as letras do alfabeto pelo menos uma vez).

import string
def pang(frase):
    frase = frase.lower()
    let = set()
    for i in frase:
        if i in string.ascii_lowercase:
            let.add(i)
        if len(let) == 26:
            return True
    return False
frase1 = input('digite uma frase')
print(f"A frase '{frase1}' é um pangrama? {pang(frase1)}")

#49) Escreva uma função que receba uma string representando intervalos de números (por exemplo, "1-3,5,7-9") e retorne uma lista expandida com todos os números nesses intervalos.

def inter(intervalo):
    partes = intervalo.split(',')
    numeros = []
    for parte in partes:
        if '-' in parte:
            inicio, fim = parte.split('-')
            numeros.extend(range(int(inicio), int(fim) + 1))
        else:
            numeros.append(int(parte))
    return numeros
num = "1-3,5,7-9"
resultado = inter(num)
print(f"Intervalos expandidos de '{num}': {resultado}")

#50) Escreva uma função que converta um número romano para um número inteiro

def romano_para_inteiro(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    anterior = 0
    for numeral in reversed(romano):
        valor = valores[numeral]
        if valor < anterior:
            total -= valor
        else:
            total += valor
        anterior = valor
    return total
numero_romano = "IX"
print(f"O número romano '{numero_romano}' é: {romano_para_inteiro(numero_romano)}")
