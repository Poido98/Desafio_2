from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

def recorrer_matriz(matriz_data_heroes) -> None:

    for fila in range(len(matriz_data_heroes)):
        for columna in range(len(matriz_data_heroes[fila])):
            print(matriz_data_heroes[fila][columna], end=' ')
        print(' ')


def mostrar_heroes_femeninos(matriz_data_heroes) -> None:

    for columna in range(len(matriz_data_heroes[0])):
        mujeres = matriz_data_heroes[3][columna]
        if mujeres == 'Femenino':
            for fila in range(len(matriz_data_heroes)):
                print(matriz_data_heroes[fila][columna])
                print('////////////////')





if __name__ == "__main__":
    print("Heroes femeninos: ")
    mostrar_heroes_femeninos(matriz_data_heroes)

