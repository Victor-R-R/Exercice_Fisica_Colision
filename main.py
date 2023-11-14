""" /*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 */ """


def colision(posicion_a, velocidad_a, posicion_b, velocidad_b):

    xa, ya = posicion_a
    xb, yb = posicion_b
    vxa, vya = velocidad_a
    vxb, vyb = velocidad_b

    if vxa - vxb == 0:
        if xa == xb:
            tx = 0
        else:
            return "Los objetos no se encontraran"
    else:
        tx = (xb - xa) / (vxa - vxb)

    if vya - vyb == 0:
        if ya == yb:
            ty = 0
        else:
            return "Los objetos no se encontraran"
    else:
        ty = (yb - ya) / (vya - vyb)

    if tx == ty:
        t = tx
        x = xa + vxa * tx
        y = ya + vya * ty
        return f"Los objetos colisionan en el punto ({x}, {y}) en un tiempo {t}"
    else:
        return "Los objetos no se encontraran"


print(colision((2, 0), (0, 1), (0, 2), (1, 0)))

print(colision((0, 0), (10, 5), (100, 50), (-5, -2.5)))
