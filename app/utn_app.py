from funciones_utn import (
    mostrar_menu
)

from validaciones_utn import (
    validar_opcion
)

from UTN_Heroes_Dataset.utn_funciones import play_sound, clear_console

from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

def utn_heroes_app():

    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 13)
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                print("Saliendo...")
                break
        play_sound()
        clear_console()

if __name__  == "__main__": 
    utn_heroes_app(matriz_data_heroes)