def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero -1) + fibonacci(numero -2)

num = int(input('Digite um número para calcular seu fibonacci: '))
resultado = fibonacci(num-1)
print(f'O Resultado fibonacci do número {num} é {resultado}')