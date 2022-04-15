tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("****Tareas desordenadas****")
for tarea in tareas:
    print(tarea[0], tarea[1])

from collections import deque

tareas.sort()

cola = deque()
for tarea in tareas:
    cola.append(tarea[1])

print("****Tareas ordenadas****")
for tarea in cola:
    print(tarea)
