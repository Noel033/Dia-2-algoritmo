class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad            # Capacidad máxima de la cola
        self.queue = [None] * capacidad       # Lista para almacenar los elementos
        self.front = 0                       # Índice del frente de la cola (inicio)
        self.rear = 0                        # Índice del final de la cola (donde se agrega)
        self.count = 0                      # Contador de elementos en la cola

    def enqueue(self, element):
        if self.isFull():                   # Verifica si la cola está llena antes de agregar
            return "La cola está llena"
        self.queue[self.rear] = element     # Coloca el nuevo elemento al final
        self.rear = (self.rear + 1) % self.capacidad  # Actualiza el índice rear circularmente
        self.count += 1                    # Incrementa el contador de elementos

    def enqueue_front(self, element):
        if self.isFull():                   # Verifica si la cola está llena antes de agregar al frente
            return "La cola está llena"
        # Retrocede el índice front (circularmente) para insertar al frente
        self.front = (self.front - 1 + self.capacidad) % self.capacidad
        self.queue[self.front] = element    # Inserta el elemento al frente
        self.count += 1                    # Incrementa el contador de elementos

    def dequeue(self):
        if self.isEmpty():                  # Verifica si la cola está vacía antes de eliminar
            return "La cola está vacía"
        element = self.queue[self.front]    # Guarda el elemento que está al frente para retornarlo
        self.queue[self.front] = None       # Limpia el espacio donde estaba el elemento eliminado
        self.front = (self.front + 1) % self.capacidad  # Mueve el índice front al siguiente elemento (circular)
        self.count -= 1                    # Decrementa el contador de elementos
        return element                     # Devuelve el elemento eliminado

    def peek(self):
        if self.isEmpty():                  # Verifica si la cola está vacía
            return "La cola está vacía"
        return self.queue[self.front]       # Retorna el elemento al frente sin eliminarlo

    def peek_last(self):
        if self.isEmpty():                  # Verifica si la cola está vacía
            return "La cola está vacía"
        # Calcula el índice del último elemento (antes de rear) circularmente
        last_index = (self.rear - 1 + self.capacidad) % self.capacidad
        return self.queue[last_index]       # Retorna el último elemento sin eliminarlo

    def isEmpty(self):
        return self.count == 0             # Retorna True si no hay elementos en la cola

    def isFull(self):
        return self.count == self.capacidad  # Retorna True si la cola está llena

    def size(self):
        return self.count                  # Retorna el número de elementos actuales en la cola

    def mostrar(self):
        resultado = []
        index = self.front                 # Empieza desde el frente
        for _ in range(self.count):       # Recorre todos los elementos que hay en la cola
            resultado.append(self.queue[index])
            index = (index + 1) % self.capacidad  # Avanza circularmente
        return resultado                  # Devuelve una lista con los elementos en orden


# Uso del objeto ColaCircular

myColaMatricula = ColaCircular(5)      # Crea una cola con capacidad para 5 elementos

myColaMatricula.enqueue('Aldo')        # Agrega "Aldo" al final de la cola
myColaMatricula.enqueue('Bianca')      # Agrega "Bianca" al final
myColaMatricula.enqueue('Carlos')      # Agrega "Carlos" al final

print("Cola: ", myColaMatricula.mostrar())    # Muestra todos los elementos de la cola
print("Primer elemento: ", myColaMatricula.peek())  # Muestra el primer elemento
print("Último elemento: ", myColaMatricula.peek_last())  # Muestra el último elemento
print("Elimina: ", myColaMatricula.dequeue())  # Elimina el primer elemento y lo muestra
print("Cola después de eliminar: ", myColaMatricula.mostrar())  # Muestra la cola tras eliminar

print("Está vacía: ", myColaMatricula.isEmpty())  # Verifica si está vacía (False)
print("Tamaño: ", myColaMatricula.size())         # Muestra la cantidad de elementos actuales

myColaMatricula.enqueue('Diana')                    # Agrega "Diana" al final
print("Cola después de agregar un nuevo elemento: ", myColaMatricula.mostrar())
print("Nuevo primer elemento: ", myColaMatricula.peek())
print("Último elemento: ", myColaMatricula.peek_last())
print("Tamaño: ", myColaMatricula.size())

myColaMatricula.enqueue_front('Elena')              # Agrega "Elena" al frente de la cola
print("Cola después de agregar un nuevo elemento al inicio: ", myColaMatricula.mostrar())
print("Nuevo primer elemento: ", myColaMatricula.peek())     # Ahora "Elena" es el primer elemento
print("Último elemento: ", myColaMatricula.peek_last())      # Último elemento sigue igual

