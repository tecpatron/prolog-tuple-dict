# USO DE TUPLAS

hechos = {
    ("juan", "padre", "carlos"),
    ("juan", "padre", "ana"),
    ("carlos", "padre", "luis"),
    ("carlos", "padre", "sofia"),
    ("luis", "padre", "mateo"),
}

def consultar(s=None, p=None, o=None):
    return sorted(
        (sujeto, predicado, objeto)
        for sujeto, predicado, objeto in hechos
        if (s is None or sujeto == s)
        and (p is None or predicado == p)
        and (o is None or objeto == o)
    )


def inferir():
    padres = {(x, y) for x, r, y in hechos if r == "padre"}
    hijos = {(y, x) for x, y in padres}

    abuelos = {
        (x, z)
        for x, y in padres
        for y2, z in padres
        if y == y2
    }

    hermanos = {
        (x, y)
        for p1, x in padres
        for p2, y in padres
        if p1 == p2 and x != y
    }

    return {
        "hijo": hijos,
        "abuelo": abuelos,
        "hermano": hermanos,
    }

def mostrar_relacion(nombre, pares):
    print(f"\n{nombre.upper()}:")
    for x, y in sorted(pares):
        print(f"  {nombre}({x}, {y})")

if __name__ == "__main__":
    print("HECHOS:")
    for sujeto, predicado, objeto in consultar(p="padre"):
        print(f"  {predicado}({sujeto}, {objeto})")

    print("\nCONSULTAS POR PATRÓN:")
    print("Hijos de Carlos:", consultar(s="carlos", p="padre"))
    print("Hecho padre de Ana:", consultar(p="padre", o="ana"))

    resultados = inferir()
    for relacion, pares in resultados.items():
        mostrar_relacion(relacion, pares)

    print("\nPREGUNTAS:")
    print("¿Juan es abuelo de Luis?", ("juan", "luis") in resultados["abuelo"])
    print("¿Luis y Sofía son hermanos?", ("luis", "sofia") in resultados["hermano"])