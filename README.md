# Ontología familiar

Ejemplo que consiste en un árbol genealógico. Los hechos describen quién es padre de quién. Las reglas permiten deducir relaciones de hijo, abuelo, hermanos

## HECHOS

padre(juan, carlos)<br>
padre(juan, ana)<br>
padre(carlos, luis)<br>
padre(carlos, sofia)

## REGLAS

Regla 1: hijo<br>
padre(X, Y) -> hijo(Y, X)<br>

Regla 2: hermanos<br>
padre(P, X) AND padre(P, Y) AND X != Y -> hermano(X, Y)

Regla 3: abuelo<br>
padre(X, Y) AND padre(Y, Z) -> abuelo(X, Z)<br>

## GRÁFICO

<img width="760" height="840" alt="DICT-TUPLES" src="https://github.com/user-attachments/assets/0abd0a00-987b-4d95-bc40-95d6cb803394" />
