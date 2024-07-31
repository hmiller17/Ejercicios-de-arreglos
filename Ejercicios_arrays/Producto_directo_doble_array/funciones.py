def producto_directo(v,w):
    if len(v) == len(w):
        producto = []
        for i in range(len(v)):
            m = v[i] * w[i]
            producto.append(m)
        print(f"El producto de cada item de v y w es: {producto}")
    else:
        print("Las listas no tienen la misma cantidad de elementos.")
            