matriz = [
    [34, 23, 12],
    [45, 67, 89],
    [23, 56, 78]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

def ordenar_fila(matriz, fila_index):
    if 0 <= fila_index < len(matriz):
        fila = matriz[fila_index]
        bubble_sort(fila)
    else:
        print("indice de fila fuera de rango.")

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 0

ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
