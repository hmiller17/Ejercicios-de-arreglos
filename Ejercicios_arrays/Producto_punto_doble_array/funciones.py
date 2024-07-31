def producto_arrays(v,w):
    if (len(v) == len(w)):
        producto = []
        x = 0
        for i in range(len(v)):
            m = 0
            m = v[i] * w[i]
            producto.append(m)
        for j in producto:
            x += j
        print(f"El producto de los arreglos v y w es: {x}")
    else:
        print("La cantidad de items en los arreglos, no son iguales")

