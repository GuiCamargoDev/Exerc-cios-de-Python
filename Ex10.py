a = input('Informe um valor para a variavel A: ')
b = input('Informe um valor para a variavel B: ')

if (a>b):
    aux=a
    a=b
    b=aux
print('O valor da variavel A agora é: ', a)
print('O valor da variavel B agora é: ', b)