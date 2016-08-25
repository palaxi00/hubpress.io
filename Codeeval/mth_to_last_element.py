import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        stringe = test.strip().split()
        lista = stringe[:-1]
        contar = int(stringe[-1])
        if contar <= len(lista):
            print (lista[-contar])