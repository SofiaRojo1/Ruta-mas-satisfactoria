import heapq
import math
import unicodedata

# ============================================================
# TOUR MATCH: encuentra tu ruta turística ideal (Antioquia)
# ============================================================

# ---------- 1. DATOS: 53 destinos con múltiples atributos ----------
# (clave, nombre, municipio, tipo, intereses, altitud msnm, temp °C,
#  calificación, entrada COP, duración min, latitud, longitud)
# Nota: valores aproximados con fines académicos.
DATOS = [
    # --- Medellín ---
    ("arvi", "Parque Arví", "Medellín", "naturaleza", {"senderismo", "vistas", "aventura"}, 2500, 14, 4.8, 20000, 180, 6.2790, -75.5020),
    ("jardin", "Jardín Botánico", "Medellín", "naturaleza", {"familia", "ciencia", "flora"}, 1475, 22, 4.7, 6000, 120, 6.2720, -75.5630),
    ("explora", "Parque Explora", "Medellín", "ciencia", {"familia", "cultura", "interactivo"}, 1490, 22, 4.7, 32000, 150, 6.2713, -75.5663),
    ("deseos", "Parque de los Deseos", "Medellín", "recreacion", {"familia", "ciencia", "paseo"}, 1490, 22, 4.4, 0, 60, 6.2697, -75.5650),
    ("planetario", "Planetario de Medellín", "Medellín", "ciencia", {"familia", "astronomia", "educacion"}, 1490, 22, 4.5, 15000, 90, 6.2709, -75.5648),
    ("pueblito", "Pueblito Paisa", "Medellín", "historia", {"cultura", "vistas", "tradicion"}, 1600, 21, 4.5, 0, 60, 6.2352, -75.5792),
    ("museo", "Museo de Antioquia", "Medellín", "arte", {"cultura", "historia", "museo"}, 1495, 22, 4.7, 30000, 120, 6.2519, -75.5686),
    ("botero", "Plaza Botero", "Medellín", "arte", {"cultura", "historia", "escultura"}, 1495, 22, 4.6, 0, 45, 6.2523, -75.5694),
    ("comuna13", "Comuna 13", "Medellín", "cultura", {"arte", "aventura", "grafiti"}, 1560, 22, 4.8, 0, 120, 6.2570, -75.6130),
    ("mercado", "Mercado del Río", "Medellín", "gastronomia", {"cultura", "paseo", "comida"}, 1495, 22, 4.5, 0, 90, 6.2610, -75.5663),
    ("lleras", "Parque Lleras", "Medellín", "recreacion", {"gastronomia", "nocturna", "paseo"}, 1560, 22, 4.2, 0, 90, 6.2087, -75.5675),
    ("poblado", "Parque El Poblado", "Medellín", "recreacion", {"paseo", "gastronomia", "urbano"}, 1560, 22, 4.3, 0, 60, 6.2088, -75.5706),
    ("volador", "Cerro El Volador", "Medellín", "naturaleza", {"senderismo", "vistas", "paseo"}, 1650, 21, 4.4, 0, 120, 6.2640, -75.5800),
    ("berrio", "Parque Berrío", "Medellín", "historia", {"cultura", "urbano", "tradicion"}, 1495, 22, 4.2, 0, 45, 6.2518, -75.5669),
    ("catedral", "Basílica Metropolitana", "Medellín", "historia", {"cultura", "arquitectura", "religion"}, 1495, 22, 4.6, 0, 40, 6.2537, -75.5676),
    ("luces", "Parque de las Luces", "Medellín", "arte", {"urbano", "cultura", "paseo"}, 1495, 22, 4.4, 0, 45, 6.2478, -75.5688),
    ("mamm", "Museo de Arte Moderno", "Medellín", "arte", {"cultura", "museo", "contemporaneo"}, 1520, 22, 4.5, 15000, 90, 6.2300, -75.5740),
    ("memoria", "Museo Casa de la Memoria", "Medellín", "historia", {"cultura", "museo", "educacion"}, 1495, 22, 4.7, 0, 90, 6.2470, -75.5570),
    ("norte", "Parque Norte", "Medellín", "recreacion", {"familia", "aventura", "atracciones"}, 1480, 22, 4.2, 25000, 180, 6.2750, -75.5650),
    ("espana", "Parque Biblioteca España", "Medellín", "cultura", {"arte", "vistas", "urbano"}, 1800, 20, 4.5, 0, 60, 6.2876, -75.5413),
    ("sanpedro", "Cementerio Museo San Pedro", "Medellín", "historia", {"cultura", "museo", "arte"}, 1500, 22, 4.6, 0, 60, 6.2566, -75.5620),
    ("pies", "Parque de los Pies Descalzos", "Medellín", "recreacion", {"familia", "paseo", "agua"}, 1500, 22, 4.5, 0, 60, 6.2432, -75.5735),
    ("castillo", "Museo El Castillo", "Medellín", "historia", {"cultura", "arquitectura", "museo"}, 1600, 21, 4.5, 20000, 90, 6.1990, -75.5660),
    # --- Valle de Aburrá ---
    ("envigado", "Parque Principal de Envigado", "Envigado", "pueblo", {"cultura", "gastronomia", "paseo"}, 1575, 22, 4.3, 0, 60, 6.1705, -75.5833),
    ("sabaneta", "Parque Principal de Sabaneta", "Sabaneta", "pueblo", {"gastronomia", "paseo", "tradicion"}, 1550, 22, 4.2, 0, 60, 6.1515, -75.6165),
    ("itagui", "Parque Principal de Itagüí", "Itagüí", "pueblo", {"arte", "cultura", "paseo"}, 1550, 22, 4.0, 0, 45, 6.1846, -75.5991),
    ("bello", "Parque Principal de Bello", "Bello", "pueblo", {"cultura", "historia", "paseo"}, 1450, 23, 4.1, 0, 45, 6.3373, -75.5579),
    ("copacabana", "Parque Principal de Copacabana", "Copacabana", "pueblo", {"gastronomia", "paseo", "tradicion"}, 1425, 23, 4.1, 0, 60, 6.3480, -75.5100),
    ("girardota", "Girardota", "Girardota", "pueblo", {"gastronomia", "tradicion", "paseo"}, 1425, 24, 4.2, 0, 60, 6.3790, -75.4450),
    ("barbosa", "Barbosa", "Barbosa", "pueblo", {"paseo", "naturaleza", "tradicion"}, 1300, 25, 4.1, 0, 60, 6.4380, -75.3300),
    ("caldas", "Parque Principal de Caldas", "Caldas", "pueblo", {"naturaleza", "paseo", "tradicion"}, 1750, 19, 4.1, 0, 60, 6.0910, -75.6360),
    ("estrella", "Parque Principal de La Estrella", "La Estrella", "pueblo", {"paseo", "cultura", "tradicion"}, 1775, 19, 4.0, 0, 45, 6.1580, -75.6430),
    # --- Oriente y norte de Antioquia ---
    ("guatape", "Pueblo de Guatapé", "Guatapé", "pueblo", {"cultura", "gastronomia", "colorido"}, 1925, 18, 4.8, 0, 150, 6.2338, -75.1590),
    ("penol", "Piedra del Peñol", "El Peñol", "aventura", {"vistas", "naturaleza", "senderismo"}, 2135, 17, 4.8, 25000, 120, 6.2216, -75.1800),
    ("embalse", "Embalse Peñol-Guatapé", "Guatapé", "naturaleza", {"agua", "aventura", "vistas"}, 1900, 18, 4.7, 40000, 150, 6.2400, -75.1800),
    ("rionegro", "Parque San Nicolás de Rionegro", "Rionegro", "historia", {"cultura", "gastronomia", "paseo"}, 2125, 17, 4.4, 0, 90, 6.1550, -75.3740),
    ("marinilla", "Marinilla", "Marinilla", "pueblo", {"cultura", "gastronomia", "tradicion"}, 1900, 18, 4.3, 0, 60, 6.1740, -75.3360),
    ("retiro", "El Retiro", "El Retiro", "pueblo", {"gastronomia", "artesanias", "paseo"}, 2175, 16, 4.6, 0, 120, 6.0620, -75.5030),
    ("laceja", "La Ceja", "La Ceja", "pueblo", {"naturaleza", "gastronomia", "paseo"}, 2200, 16, 4.4, 0, 90, 6.0300, -75.4300),
    ("carmen", "El Carmen de Viboral", "El Carmen de Viboral", "pueblo", {"artesanias", "cultura", "tradicion"}, 2150, 16, 4.4, 0, 90, 6.0830, -75.3340),
    ("guarne", "Guarne", "Guarne", "pueblo", {"gastronomia", "paseo", "naturaleza"}, 2150, 16, 4.2, 0, 60, 6.2790, -75.4440),
    ("sanpedrom", "San Pedro de los Milagros", "San Pedro de los Milagros", "pueblo", {"gastronomia", "religion", "tradicion"}, 2475, 14, 4.2, 0, 60, 6.4600, -75.5570),
    ("santarosa", "Santa Rosa de Osos", "Santa Rosa de Osos", "historia", {"cultura", "religion", "arquitectura"}, 2550, 14, 4.2, 0, 60, 6.6470, -75.4600),
    # --- Occidente y suroeste ---
    ("santafe", "Santa Fe de Antioquia", "Santa Fe de Antioquia", "historia", {"cultura", "gastronomia", "arquitectura"}, 550, 27, 4.7, 0, 180, 6.5560, -75.8270),
    ("puente", "Puente de Occidente", "Santa Fe de Antioquia", "historia", {"arquitectura", "paseo", "cultura"}, 520, 28, 4.5, 0, 45, 6.5395, -75.8050),
    ("sopetran", "Sopetrán", "Sopetrán", "pueblo", {"gastronomia", "paseo", "tradicion"}, 750, 25, 4.2, 0, 60, 6.5010, -75.7430),
    ("sanjeronimo", "San Jerónimo", "San Jerónimo", "pueblo", {"naturaleza", "gastronomia", "paseo"}, 780, 25, 4.2, 0, 60, 6.4480, -75.7270),
    ("titiribi", "Titiribí", "Titiribí", "pueblo", {"naturaleza", "historia", "tradicion"}, 1450, 22, 4.2, 0, 60, 6.0620, -75.7900),
    ("fredonia", "Fredonia", "Fredonia", "pueblo", {"naturaleza", "cultura", "tradicion"}, 1800, 19, 4.3, 0, 60, 5.9260, -75.6740),
    ("jerico", "Jericó", "Jericó", "pueblo", {"cultura", "religion", "gastronomia"}, 1950, 19, 4.7, 0, 150, 5.7910, -75.7850),
    ("jardinpueblo", "Jardín (Antioquia)", "Jardín", "pueblo", {"naturaleza", "cultura", "colorido"}, 1750, 20, 4.8, 0, 180, 5.5990, -75.8190),
    ("andes", "Andes", "Andes", "pueblo", {"cafe", "naturaleza", "paseo"}, 1350, 22, 4.2, 0, 60, 5.6570, -75.8800),
    ("napoles", "Hacienda Nápoles", "Puerto Triunfo", "recreacion", {"familia", "aventura", "naturaleza"}, 300, 27, 4.3, 60000, 240, 5.8930, -74.7140),
]

DESTINOS = {}
for (k, nom, mun, tipo, ints, alt, temp, cal, ent, dur, lat, lon) in DATOS:
    DESTINOS[k] = {"nombre": nom, "municipio": mun, "tipo": tipo,
                   "tags": {tipo} | set(ints), "altitud": alt, "temp": temp,
                   "calificacion": cal, "entrada": ent, "duracion": dur,
                   "lat": lat, "lon": lon}

INTERESES_DISPONIBLES = sorted({t for d in DESTINOS.values() for t in d["tags"]})

CLIMAS = {"1": "Frío (hasta 17 °C)", "2": "Templado (18 a 23 °C)",
          "3": "Cálido (24 °C o más)", "4": "Me es indiferente"}


def clima_de(temp):
    if temp <= 17:
        return "1"
    if temp <= 23:
        return "2"
    return "3"


# ---------- 2. GRAFO PONDERADO (lista de adyacencia) ----------
# Las distancias se calculan a partir de las coordenadas (Haversine).
GRAFO = {k: [] for k in DESTINOS}
_PARES = set()
K_VECINOS = 3


def distancia_directa(a, b):
    """Distancia en línea recta (km) entre dos destinos."""
    la1, lo1 = math.radians(DESTINOS[a]["lat"]), math.radians(DESTINOS[a]["lon"])
    la2, lo2 = math.radians(DESTINOS[b]["lat"]), math.radians(DESTINOS[b]["lon"])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * 6371 * math.asin(math.sqrt(h))


def datos_ruta(a, b):
    """Km por carretera (x1.3), minutos y costo estimado de transporte."""
    km = distancia_directa(a, b) * 1.3
    if km <= 1.2:                       # caminando
        minutos, costo = km * 12, 0
    elif km <= 15:                      # ciudad: metro/bus
        minutos, costo = km / 25 * 60 + 5, 2500
    else:                               # intermunicipal
        minutos = km / 45 * 60 + 5
        costo = int(round((2500 + 400 * (km - 15)) / 500) * 500)
    return {"km": round(km, 1), "min": max(1, int(round(minutos))), "costo": costo}


def agregar_ruta(a, b):
    par = frozenset((a, b))
    if par in _PARES:
        return
    _PARES.add(par)
    datos = datos_ruta(a, b)
    GRAFO[a].append((b, datos))
    GRAFO[b].append((a, datos))


def componentes():
    marca, n = {}, 0
    for nodo in GRAFO:
        if nodo in marca:
            continue
        marca[nodo] = n
        pila = [nodo]
        while pila:
            u = pila.pop()
            for v, _ in GRAFO[u]:
                if v not in marca:
                    marca[v] = n
                    pila.append(v)
        n += 1
    return marca, n


def construir_grafo():
    claves = list(DESTINOS)
    for a in claves:  # cada destino se conecta con sus vecinos más cercanos
        vecinos = sorted((b for b in claves if b != a),
                         key=lambda b: distancia_directa(a, b))[:K_VECINOS]
        for b in vecinos:
            agregar_ruta(a, b)
    while True:  # garantiza que el grafo quede conectado
        marca, n = componentes()
        if n == 1:
            break
        a, b = min(((x, y) for x in claves for y in claves if marca[x] != marca[y]),
                   key=lambda p: distancia_directa(*p))
        agregar_ruta(a, b)


construir_grafo()

MAX_KM = max(d["km"] for u in GRAFO for _, d in GRAFO[u])
MAX_MIN = max(d["min"] for u in GRAFO for _, d in GRAFO[u])
MAX_COSTO = max(d["costo"] for u in GRAFO for _, d in GRAFO[u])

# Prioridad del usuario -> pesos (distancia, tiempo, costo)
PRIORIDADES = {
    "1": ("Ahorrar tiempo", (0.2, 0.6, 0.2)),
    "2": ("Gastar menos dinero", (0.2, 0.2, 0.6)),
    "3": ("Recorrer distancias cortas", (0.6, 0.2, 0.2)),
}


# ---------- 3. ALGORITMOS ----------
def peso_arista(datos, pesos):
    """Combina distancia, tiempo y costo normalizados en un solo número."""
    w_km, w_min, w_costo = pesos
    return (w_km * datos["km"] / MAX_KM
            + w_min * datos["min"] / MAX_MIN
            + w_costo * datos["costo"] / MAX_COSTO)


def dijkstra(origen, pesos):
    """Camino de menor costo ponderado desde origen hacia todos los nodos."""
    dist = {n: float("inf") for n in GRAFO}
    previo = {}
    dist[origen] = 0
    cola = [(0, origen)]
    while cola:
        d, u = heapq.heappop(cola)
        if d > dist[u]:
            continue
        for v, datos in GRAFO[u]:
            nuevo = d + peso_arista(datos, pesos)
            if nuevo < dist[v]:
                dist[v] = nuevo
                previo[v] = u
                heapq.heappush(cola, (nuevo, v))
    return dist, previo


def reconstruir_camino(previo, origen, destino):
    camino = [destino]
    while camino[-1] != origen:
        camino.append(previo[camino[-1]])
    return camino[::-1]


def totales_camino(camino):
    """Suma km, minutos y costo real de transporte a lo largo de un camino."""
    km = mi = co = 0
    for a, b in zip(camino, camino[1:]):
        datos = next(d for v, d in GRAFO[a] if v == b)
        km += datos["km"]
        mi += datos["min"]
        co += datos["costo"]
    return km, mi, co


def satisfaccion(clave, perfil):
    """Puntaje 0-100: 60% similitud de intereses (Jaccard) + 40% calificación."""
    tags = DESTINOS[clave]["tags"]
    similitud = len(tags & perfil) / len(tags | perfil)
    calif = DESTINOS[clave]["calificacion"] / 5
    return round(100 * (0.6 * similitud + 0.4 * calif), 1)


def construir_tour(inicio, prefs, cantidad=5):
    """Selección progresiva: en cada paso elige el destino con mejor balance
    entre satisfacción y desplazamiento, respetando presupuesto y clima."""
    pesos = PRIORIDADES[prefs["prioridad"]][1]
    perfil = set(DESTINOS[inicio]["tags"]) | set(prefs["intereses"])
    satis = {k: satisfaccion(k, perfil) for k in DESTINOS}

    gasto = DESTINOS[inicio]["entrada"]
    if gasto > prefs["presupuesto"]:
        return None
    tour = [inicio]
    tramos = []
    actual = inicio

    while len(tour) < cantidad:
        dist, previo = dijkstra(actual, pesos)
        candidatos = []
        for k in DESTINOS:
            if k in tour or dist[k] == float("inf"):
                continue
            if prefs["clima"] != "4" and clima_de(DESTINOS[k]["temp"]) != prefs["clima"]:
                continue  # no coincide con el clima preferido
            camino = reconstruir_camino(previo, actual, k)
            km, mi, co = totales_camino(camino)
            if gasto + co + DESTINOS[k]["entrada"] > prefs["presupuesto"]:
                continue  # supera el presupuesto
            candidatos.append((k, camino, km, mi, co, dist[k]))
        if not candidatos:
            break
        max_peso = max(c[5] for c in candidatos) or 1
        # Valor = satisfacción - penalización por desplazamiento (0 a 40 puntos)
        mejor = max(candidatos, key=lambda c: satis[c[0]] - 40 * (c[5] / max_peso))
        k, camino, km, mi, co, _ = mejor
        gasto += co + DESTINOS[k]["entrada"]
        tramos.append({"camino": camino, "km": km, "min": mi, "costo": co})
        tour.append(k)
        actual = k

    return {"tour": tour, "tramos": tramos, "satis": satis,
            "gasto": gasto, "perfil": perfil}


# ---------- 4. INTERFAZ DE USUARIO ----------
def cop(valor):
    return "$" + f"{valor:,.0f}".replace(",", ".")


def normalizar(texto):
    t = unicodedata.normalize("NFD", texto.lower().strip())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def leer_opcion(mensaje, validas):
    while True:
        op = input(mensaje).strip()
        if op in validas:
            return op
        print("  Opción no válida, intenta de nuevo.")


def listar_destinos():
    print(f"\n--- Destinos disponibles ({len(DESTINOS)}) ---")
    for i, d in enumerate(DESTINOS.values(), 1):
        print(f"{i:>2}. {d['nombre']} ({d['municipio']}) | {d['tipo']} | "
              f"{d['altitud']} msnm | {d['temp']} °C | ★ {d['calificacion']} | "
              f"Entrada: {cop(d['entrada'])}")


def elegir_destino(mensaje):
    claves = list(DESTINOS)
    listar_destinos()
    print("(Puedes escribir el número o parte del nombre, ej. 'arvi')")
    while True:
        txt = input(mensaje).strip()
        if txt.isdigit() and 1 <= int(txt) <= len(claves):
            return claves[int(txt) - 1]
        buscado = normalizar(txt)
        coinc = [k for k in claves if buscado and buscado in normalizar(DESTINOS[k]["nombre"])]
        if len(coinc) == 1:
            return coinc[0]
        if len(coinc) > 1:
            print("  Varias coincidencias: " + ", ".join(DESTINOS[k]["nombre"] for k in coinc))
            print("  Sé más específico o usa el número.")
        else:
            print("  No encontré ese destino, intenta de nuevo.")


def configurar_preferencias(prefs):
    print("\n--- Preferencias de viaje ---")
    print("Intereses disponibles:", ", ".join(INTERESES_DISPONIBLES))
    texto = input("Escribe tus intereses separados por coma (Enter para omitir): ")
    prefs["intereses"] = {normalizar(t) for t in texto.split(",")
                          if normalizar(t) in INTERESES_DISPONIBLES}
    if prefs["intereses"]:
        print("  Intereses registrados:", ", ".join(sorted(prefs["intereses"])))
    while True:
        try:
            prefs["presupuesto"] = int(input("Presupuesto máximo en COP (ej. 100000): "))
            if prefs["presupuesto"] >= 0:
                break
        except ValueError:
            pass
        print("  Ingresa un número entero válido.")
    print("¿Qué clima prefieres?")
    for k, nombre in CLIMAS.items():
        print(f"  {k}. {nombre}")
    prefs["clima"] = leer_opcion("Elige 1, 2, 3 o 4: ", CLIMAS.keys())
    print("¿Qué deseas priorizar en los desplazamientos?")
    for k, (nombre, _) in PRIORIDADES.items():
        print(f"  {k}. {nombre}")
    prefs["prioridad"] = leer_opcion("Elige 1, 2 o 3: ", PRIORIDADES.keys())
    print("¡Preferencias guardadas!")


def mostrar_tour(res, prefs):
    tour, tramos, satis, perfil = res["tour"], res["tramos"], res["satis"], res["perfil"]
    print("\n" + "=" * 60)
    print("  TU TOUR PERSONALIZADO")
    print("=" * 60)
    total_km = total_min = 0
    for i, k in enumerate(tour):
        d = DESTINOS[k]
        print(f"\n{i + 1}. {d['nombre']} - {d['municipio']}  (satisfacción: {satis[k]}/100)")
        print(f"   {d['tipo'].capitalize()} | {d['altitud']} msnm | {d['temp']} °C | "
              f"Entrada: {cop(d['entrada'])} | Visita: ~{d['duracion']} min")
        comunes = sorted(d["tags"] & perfil)
        print(f"   Por qué: coincide en {', '.join(comunes) if comunes else 'calidad general'}; "
              f"calificación {d['calificacion']}/5")
        total_min += d["duracion"]
        if i > 0:
            t = tramos[i - 1]
            ruta = " -> ".join(DESTINOS[x]["nombre"] for x in t["camino"])
            print(f"   Desplazamiento: {ruta}")
            print(f"   {t['km']:.1f} km | {t['min']} min | transporte {cop(t['costo'])}")
            total_km += t["km"]
            total_min += t["min"]
    print("\n" + "-" * 60)
    print(f"Destinos: {len(tour)} | Distancia total: {total_km:.1f} km")
    print(f"Tiempo total aprox.: {total_min // 60} h {total_min % 60} min")
    print(f"Costo total aprox.: {cop(res['gasto'])} (presupuesto {cop(prefs['presupuesto'])})")
    if len(tour) < 5:
        print("Nota: con tu presupuesto, clima y las rutas disponibles no fue posible completar 5 destinos.")


def info_destino():
    k = elegir_destino("Destino a consultar (número o nombre): ")
    d = DESTINOS[k]
    print(f"\n{d['nombre']} - {d['municipio']}")
    print(f"  Tipo: {d['tipo']} | Intereses: {', '.join(sorted(d['tags']))}")
    print(f"  Altitud: {d['altitud']} msnm | Temperatura promedio: {d['temp']} °C")
    print(f"  Calificación: {d['calificacion']}/5 | Entrada: {cop(d['entrada'])}")
    print(f"  Duración sugerida: {d['duracion']} min")
    print("  Conexiones directas:")
    for v, datos in sorted(GRAFO[k], key=lambda x: x[1]["km"]):
        print(f"    - {DESTINOS[v]['nombre']}: {datos['km']} km, "
              f"{datos['min']} min, {cop(datos['costo'])}")


def main():
    prefs = {"intereses": set(), "presupuesto": None, "prioridad": None, "clima": "4"}
    print("=" * 60)
    print("  TOUR MATCH: encuentra tu ruta turística ideal")
    print(f"  {len(DESTINOS)} destinos de Medellín y Antioquia")
    print("=" * 60)
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Explorar destinos")
        print("2. Encontrar un tour personalizado")
        print("3. Modificar preferencias de viaje")
        print("4. Consultar información de un destino")
        print("5. Salir")
        op = leer_opcion("Elige una opción: ", ["1", "2", "3", "4", "5"])

        if op == "1":
            listar_destinos()
        elif op == "2":
            inicio = elegir_destino("¿Cuál destino te ha gustado más? (número o nombre): ")
            if prefs["presupuesto"] is None:
                configurar_preferencias(prefs)
            res = construir_tour(inicio, prefs)
            if res is None:
                print("\nEl destino inicial supera tu presupuesto. Aumenta el presupuesto en la opción 3.")
            else:
                mostrar_tour(res, prefs)
        elif op == "3":
            configurar_preferencias(prefs)
        elif op == "4":
            info_destino()
        else:
            print("\n¡Gracias por usar Tour Match! Buen viaje.")
            break


if __name__ == "__main__":
    main()
