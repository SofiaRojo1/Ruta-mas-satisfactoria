Ruta mas satisfactoria
# Tour Match: encuentra tu ruta turística ideal

Programa en Python que recomienda un tour de 5 destinos turísticos de Medellín y Antioquia según los gustos, el presupuesto y las prioridades del usuario. Usa **grafos** y el **algoritmo de Dijkstra** para encontrar los desplazamientos más convenientes entre destinos.

## Cómo funciona

- **Datos:** 53 destinos, cada uno con tipo, intereses, altitud (msnm), temperatura promedio, calificación, costo de entrada, duración de la visita y coordenadas.
- **Grafo ponderado:** cada destino es un nodo y se representa con una lista de adyacencia. Las distancias se calculan con la fórmula de Haversine a partir de las coordenadas, y cada ruta guarda kilómetros, minutos y costo de transporte.
- **Satisfacción (0 a 100):** 60 % similitud de intereses y 40 % calificación del destino.
- **Dijkstra:** calcula el camino de menor costo desde el destino actual a cada candidato. Distancia, tiempo y costo se normalizan y se combinan según lo que el usuario priorice.
- **Selección progresiva:** parte del destino favorito y en cada paso elige el que mejor equilibre satisfacción y desplazamiento, respetando el presupuesto y el clima preferido.

## Cómo ejecutarlo

Requiere Python 3 y no necesita instalar librerías.

```
python3 RutaOptima.py
```

## Ejemplo de uso

1. En el menú elige la opción **2** (Encontrar un tour personalizado).
2. Escribe `arvi` como destino favorito.
3. Ingresa intereses (`naturaleza`), presupuesto (`100000`), clima y prioridad (ahorrar tiempo).
4. El programa muestra el tour con el orden de visita, la satisfacción de cada destino, distancias, tiempos y costos.

## Limitaciones

- La selección progresiva es una **heurística**: encuentra recorridos razonables, pero no garantiza la combinación óptima de 5 destinos.
- Calificaciones, entradas, temperaturas y coordenadas son aproximadas, y los costos y tiempos de transporte son estimaciones con fines académicos.

## Autora

Sofi, Universidad EAFIT. Proyecto del parcial final de Algoritmos.
