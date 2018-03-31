import random
import math

def solucao1():
    print("Solução 1:")
    #Considerei que a lista contém números aleatórios.
    #Se for lista de números sequenciais e únicos,
    #poderia otimizar mais usando índices.
    lista = sorted([random.randint(0,1000) for x in range(300)])
    print("Lista gerada: \n{}".format(lista))
    """
    A melhor maneira de saber se o número está na lista é esta:
    if numero_usuario in lista:
        print('Encontrou!')
    """
    numero_usuario = int(input("Número a procurar: "))
    
    for numero_atual in lista:
        if numero_usuario == numero_atual:
            print('Encontrou!')
            break
        else:
            if numero_usuario < numero_atual: #se eu passei do número, não preciso continuar
                print('Não encontrou!')
                break

def solucao2():
    input("Solução 2: pressione 'enter'")
    lista_1 = sorted([random.randint(0, 5000000) for x in range(500)])
    lista_2 = sorted([random.randint(0, 5000000) for x in range(50000)])

    print("Comparando listas:")
    for item_2 in lista_2:
        if item_2 in lista_1: #A Python faz o trabalho para mim.
            print('- {}'.format(item_2))

def solucao3():
    input("Solução 3: pressione 'enter'")
    numero_alvo = int(input('Número limite: '))
    
    for numero in range(3,numero_alvo,2):
        if all(numero%divisor!=0 for divisor in range(3,int(math.sqrt(numero))+1)):
            print(numero)
    """
    * 2 é um numero primo, mas vou desconsiderar na solução!
    
    Um número primo é aquele que todo número que divido por um outro número
    entre 1 e ele mesmo resultará em uma divisão com resto.
    Adicionalmente, números primos não têm raiz quadrada inteira,
    pois este seria um divisor inteiro se houvesse.
    
    Então, eu testo cada número entre 3 (o primeiro número primo impar) e ele mesmo.
    Se este número em teste satisfaz esta condição:
        - Divido por todo número entre 1 e ele mesmo, dará resto.
    este número é primo.
    Testo da segunite forma:
        para cada divisor entre 2 e este número:
            se número divido pelo divisor dá resto
                adiciono o resultado na lista
        se todos os resultados da lista são verdadeiros,
            então o número é primo.
            
    Otimização: Como os números primos nunca têm raiz quadrada inteira,
    posso interromper o loop quando chegar na sua raiz quadrada.
    Se o número não é primo, seu menor divisor já terá sido encontrado
    antes de chegar na raiz quadrada. Exemplo: 16 não é primo,
    pois até sua raiz (4), já encontraos o 2 e o próprio 4.
    17 é primo, pois até chegar em sua raiz (4.12310), não encontramos divisor
    inteiro, e portando, nenhum outro seguinte irá dividi-lo.
    Adiciono o +1 para garantir arredondamento para cima.

    Se eu puder parar assim que encontrar o primeiro divisor, melhor.

    Como números pares nunca são primos, posso iterar a lista de 2 e 2 com range(x,x,2)
        
    O for inline após a condiçao, alimenta uma lista implícita
    destes resultados para a função all().

    Referências: Stack Overflow e documentação da Python.
    """
def solucao4():
    input("Solução 4: pressione 'enter'")
    lista = []
    for x in range (65,91+1):
        lista.append(chr(x))
    for x in range (97,122+1):
        lista.append(chr(x))
    #tupla = tuple(lista)   #Se eu quiser converter
    palavra = input('Informe a palavra: ')

    #print("Lista gerada: {}".format(lista))

    valor_palavra = 0
    for letra in palavra:
        valor_palavra += (lista.index(letra) + 1)

    print("Valor palavra: {}".format(valor_palavra))

    
    if all(valor_palavra%divisor!=0 for divisor in range(2,int(math.sqrt(valor_palavra))+1)):
        print("Palavra de valor {} é prima!".format(valor_palavra))
    else: 
        print("Palavra de valor {} não é prima!".format(valor_palavra))
        
def main():
    solucao1()
    solucao2()
    solucao3()
    solucao4()

if __name__ == "__main__":
    main()
