import math


def calcula_espesor(D_1, d_1, mL_1):
    D_1 = D_1 * 10
    d_1 = d_1 * 10
    mL_1 = mL_1 * 1000
    espr = (math.pi * (D_1 ** 2 - d_1 ** 2)) / (4 * mL_1)
    return espr


def calcula_metros_lineales_nuevos(espr, D_2, d_2):
    D_2 = D_2 / 100
    d_2 = d_2 / 100
    espr = espr / 1000
    mL_2 = (math.pi * (D_2 ** 2 - d_2 ** 2)) / (4 * espr)
    return mL_2


def unidades_obtenidas_al_desembobinar(mL_1, mL_2):
    uod = mL_1 / mL_2
    return uod


def unidades_obtenidas_al_dividir_por_ancho(ach_1, ach_2):
    uoda = ach_1 / ach_2
    return uoda


def calcular_volumen(D_2, d_2, ach_2):
    rd = D_2 / 2
    gsr = D_2 - d_2
    vol = 2 * (math.pi) * rd * ach_2 * gsr
    return vol


def calcular_peso_nuevo_por_unidad(ms, mL_2, ach_2, clb, vol):
    mL_2 = mL_2 * 100
    clb = clb / 10
    gme = ms / (mL_2 * ach_2)
    dsad = gme / clb
    uw_2 = (dsad * vol) / 1000
    return uw_2, gme, dsad


def calcular_desperdicio(uw_2, uoda, uod, uw_1):
    smunid = int(uw_2) * int(uoda) * int(uod)
    desp = uw_1 - smunid
    return desp


def main():
    ms = float(input("Rollo principal - Ingresa la masa/peso base (g): "))
    D_1 = float(input("Rollo principal - Ingresa el diámetro exterior/diámetro (cm): "))
    d_1 = float(input("Rollo principal - Ingresa el diámetro interior (cm): "))
    uw_1 = float(input("Rollo principal - Ingresa el peso total del rollo (kg): "))
    clb = float(input("Rollo principal - Ingresa el calibre/puntos (mm): "))
    mL_1 = float(input("Rollo principal - Ingresa los metros lineales/longitud (m): "))
    ach_1 = float(input("Rollo principal - Ingresa el ancho (cm):"))
    D_2 = float(input("Rollos nuevos - Ingresa el diámetro exterior nuevo (cm): "))
    d_2 = float(input("Rollos nuevos - Ingresa el diámetro interior nuevo (cm): "))
    ach_2 = float(input("Rollos nuevos - Ingresa el ancho nuevo (cm): "))

    espr = calcula_espesor(D_1, d_1, mL_1)
    mL_2 = calcula_metros_lineales_nuevos(espr, D_2, d_2)
    uod = unidades_obtenidas_al_desembobinar(mL_1, mL_2)
    uoda = unidades_obtenidas_al_dividir_por_ancho(ach_1, ach_2)
    vol = calcular_volumen(D_2, d_2, ach_2)
    uw_2, gme, dsad = calcular_peso_nuevo_por_unidad(ms, mL_2, ach_2, clb, vol)
    desp = calcular_desperdicio(uw_2, uoda, uod, uw_1)

    print("El espesor que se usa en ambos procesos es: ", espr, "mm")
    print("Los metros lineales de cada nuevo rollo son: ", mL_2, "m")
    print("Unidades obtenidas al desembobinar: ", int(uod), "rollos")
    print("Unidades obtenidas al dividir por ancho: ", int(uoda), "rollos por corte")
    print("Volumen del rollo obtenido al final: ", vol, "cm3")
    print("Peso de cada rollo al final del proceso: ", uw_2, "kg")
    print("Gramaje por peso entre area nueva: ", gme, "g/cm2")
    print("Densidad de papel por gramaje entre calibre: ", dsad, "g/cm3")
    print("Desperdicio de papel por recortes: ", desp, "kg")


if __name__ == "__main__":
    main()

