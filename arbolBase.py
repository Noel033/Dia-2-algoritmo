# Ejemplo de implementación de un árbol genealógico en Python
# Abol no binario, cada nodo puede tener múltiples hijos
# Cada nodo representa a una persona con su nombre  
#Es el constructor de la clase. Se ejecuta cuando se crea una nueva instancia del árbol
class Arbol:
    def __init__(self, elemento):
        self.hijos = [] #Inicializa una lista vacía que almacenará los nodos hijos del nodo actual. Esto permite que cada nodo tenga múltiples hijos.
        self.elemento = elemento #Guarda el valor o contenido del nodo

def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre);
    subarbol.hijos.append(Arbol(elemento))


def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
    return None
# Ejemplo de uso
abuela = "Pele"
hija1 = "Cr7"
hija2 = "Michael Jackson"
hija3 = "Palmer"
nieto1 = "messi"
nieta2 = "yamal"
nieta3 = "raphina"
nieto4 = "bad bunny"
nieto5 = "Gavi"    
nieto6 = "lewandowski"    
arbol = Arbol(abuela)

agregarElemento(arbol, hija2, abuela)
agregarElemento(arbol, hija3, abuela)
agregarElemento(arbol, nieto4, hija2)
agregarElemento(arbol, hija1, abuela)
agregarElemento(arbol, nieto1, hija1)
agregarElemento(arbol, nieta2, hija1)
agregarElemento(arbol, nieta3, hija1)
agregarElemento(arbol, nieto5, hija3)
agregarElemento(arbol, nieto6, hija3)

def imprimirArbol(arbol, nivel=0):
    print("  " * nivel + arbol.elemento)
    for hijo in arbol.hijos:
        imprimirArbol(hijo, nivel + 1)
# Imprimir el árbol
imprimirArbol(arbol)

def eliminarNodo(arbol):
    nombre = input("Ingrese el nombre para eliminar: ")

    def eliminar(arbol, nombre):
        for hijo in arbol.hijos:
            if hijo.elemento == nombre:
                arbol.hijos.remove(hijo)
                return True
            if eliminar(hijo, nombre):
                return True
        return False

    if arbol.elemento == nombre:
        print("No se puede eliminar.")
    elif eliminar(arbol, nombre):
        print(f"'{nombre}' eliminado del mundial.")
    else:
        print(f"'{nombre}' no encontrado.")
eliminarNodo(arbol)
imprimirArbol(arbol)
