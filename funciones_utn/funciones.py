from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

def recorrer_matriz(matriz_data_heroes) -> None:

    for fila in range(len(matriz_data_heroes)):
        for columna in range(len(matriz_data_heroes[fila])):
            print(matriz_data_heroes[fila][columna], end=' ')
        print(' ')


def mostrar_heroes_femeninos(matriz_data_heroes) -> None:

    heroes_femeninos = []
    for heroe in matriz_data_heroes:
        if heroe[3] == "Femenino":
            heroes_femeninos.append(heroe)
    
    recorrer_matriz(heroes_femeninos)

    # for fila in range(len(matriz_data_heroes)):
    #     for columna in range(len(matriz_data_heroes[fila])):
    #         dato = matriz_data_heroes[fila][columna]
    #         print(f'Fila: {fila} | Columna: {columna} | Dato: {dato}')



if __name__ == "__main__":
    print("Heroes femeninos: ")
    mostrar_heroes_femeninos(matriz_data_heroes)

