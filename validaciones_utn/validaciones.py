def validar_opcion(num_min: int, num_max: int) -> None:
    opcion = input(f"Ingrese una opcion [{num_min} - {num_max}]: ")

    # if not opcion or not opcion.isdigit() or int(opcion) > num_max or int(opcion) < num_min:
    if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max):
        return validar_opcion(num_min, num_max)
    else:
        return int(opcion)