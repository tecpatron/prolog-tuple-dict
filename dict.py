# USO DE DICCIONARIOS

familia = {
    "juan": {"hijos": ["carlos", "ana"]},
    "carlos": {"padre": "juan", "hijos": ["luis", "sofia"]},
    "ana": {"padre": "juan"},
    "luis": {"padre": "carlos", "hijos": ["mateo"]},
    "sofia": {"padre": "carlos"},
    "mateo": {"padre": "luis"},
}

def padre_de(persona):
    return familia.get(persona, {}).get("padre")

def hijos_de(persona):
    return familia.get(persona, {}).get("hijos", [])

def abuelo_de(persona):
    padre = padre_de(persona)
    if padre is None:
        return None
    return padre_de(padre)

def hermanos_de(persona):
    padre = padre_de(persona)
    if padre is None:
        return []
    return [hijo for hijo in hijos_de(padre) if hijo != persona]

def ancestros_de(persona):
    resultado = []
    actual = padre_de(persona)
    while actual is not None:
        resultado.append(actual)
        actual = padre_de(actual)
    return resultado

def agregar_hijo(padre, hijo):
    familia.setdefault(padre, {}).setdefault("hijos", [])
    familia.setdefault(hijo, {})
    if hijo not in familia[padre]["hijos"]:
        familia[padre]["hijos"].append(hijo)
    familia[hijo]["padre"] = padre

if __name__ == "__main__":
    print("CONSULTAS DIRECTAS:")
    print("Padre de Luis:", padre_de("luis"))
    print("Hijos de Carlos:", hijos_de("carlos"))

    print("\nREGLAS DE PARENTESCO:")
    print("Abuelo de Luis:", abuelo_de("luis"))
    print("Hermanos de Luis:", hermanos_de("luis"))
    print("Ancestros de Mateo:", ancestros_de("mateo"))