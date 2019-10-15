""" Manuela Garcia Monsalve - 593892
    Osmi Santiago Otalora Guerrero - 598970
    Andres Felipe Garcia Fiscal - 604962
    Paradigmas de programacion - 2206"""

def isNumber(input):
    try:
        int(input)
        if int(input) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def fib_recursive(num):
    result = []
    if num <= 1:
        return num;
    else:
        return(fib_recursive(num-1) + fib_recursive(num-2));

result = []
max_number = input("Ingresa un numero: ")
while not isNumber(max_number):
    print('No es un numero entero positivo')
    max_number = input("Ingresa un numero: ")
    pass

num = fib_recursive(0)
i = 0
while True:
    result.append(num)
    i=i+1
    num = fib_recursive(i)
    if num > int(max_number):
        break

print(result[-2:])
