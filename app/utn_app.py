from funciones_utn import (

)

from validaciones_utn import (

)



def utn_heroes_app(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas, debug):

    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 13)
        play_sound()
        match opcion:
            case 1:
                utn_mostrar_nombres_heroes(lista_nombres)
            case 2:
                utn_mostrar_identidades_heroes(lista_identidades)
            case 3:
                utn_mostrar_heroe_mayor_altura(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas, debug)
            case 4:
                utn_mostrar_heroes_mas_fuertes(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas)
            case 5:
                utn_filtrar_heroes_genero(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas, "Femenino")
            case 6:
                utn_filtrar_heroes_genero(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas, "Masculino")
            case 7:
                utn_filtrar_heroes_genero(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas, "No-Binario")
            case 8:
                utn_mostrar_heroes_poder_superior_promedio(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas)
            case 9:
                utn_mostrar_heroes_mas_debiles(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas)
            case 10:
                utn_ordenar_heroes_poder_ascendente(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas)
            case 11:
                pass
            case 12:
                pass
            case 13:
                print("Saliendo...")
                break
            case _:
                print('Opcion no valida')

        limpiar_pantalla()