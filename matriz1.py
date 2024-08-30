matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None


valor_a_buscar = 50

resultado = buscar_valor(matriz, valor_a_buscar)

if resultado:
    print(f"Valor {valor_a_buscar} encontrado en la posición {resultado}.")
else:
    print(f"Valor {valor_a_buscar} no encontrado en la matriz.")