def promedio_array(lista_reales):
    j = 0
    for i in lista_reales:
        j += i

    promedio = j / len(lista_reales)
    print(f"El promedio de {lista_reales} es: {promedio}")