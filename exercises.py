lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['emy','gui','gustavo','alberto']
lista_de_anos = [2003,2024]

#for numero in lista_de_numeros:
    #print(numero)

#soma_impares = 0
#for i in range(1, 11, 2):
    #soma_impares += i
#print(soma_impares)

#for i in range(10, 0, -1):
#    print(i)

#numero = int(input('Digite um numero para a tabuada: '))
#for i in range(1,11):
#    print(numero * i)

soma_da_lista = 0
try:
    for numero in lista_de_numeros:
        soma_da_lista += numero
    print(f"A soma da lista é: {soma_da_lista}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Exception é uma classe base para todas as exceções em Python. Capturar Exception 
# permite lidar com qualquer tipo de exceção que possa ocorrer no bloco try. O "as e" é opcional, mas é 
# frequentemente usado para acessar informações detalhadas sobre a exceção, como mensagens de erro.

lista_de_valores = [10,20,30]
soma_de_valores = 0    
try:
    for valores in lista_de_valores:
        soma_de_valores += valores
    media = soma_de_valores / len(lista_de_valores) #Len retorna o numero de itens da variavel
    print(f"Media dos valores é: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")