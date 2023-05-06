personaje_a = input('ingrese nombre de personaje')
ataque_a = 10
defensa_a = 100
efectividad_a = 0.5
personaje_b = input('ingrese nombre de personaje')
ataque_b = 10
defensa_b = 100
efectividad_b = 0.5


def daño_combate_a(ataque_a, defensa_b,efectividad_a):
    daño_combate_a = int(ataque_a - defensa_b * efectividad_a)
    if daño_combate_a >= 1:
        print(f'{personaje_a} hace {daño_combate_a} puntos de daño a {personaje_b}.')
    return daño_combate_a
    