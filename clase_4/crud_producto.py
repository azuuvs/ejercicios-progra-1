# ============================================================
# INTRODUCCIÓN A CRUD EN PYTHON
# Modelo: Entidad-Relación con Producto, Cliente y Venta
# Estructura de datos: primero con listas, luego con diccionarios
# ============================================================


# ============================================================
# PARTE 1 — REPRESENTACIÓN CON LISTAS
# ============================================================

# Una "tabla" en código puede representarse como una lista de listas.
# Cada sublista es un registro (fila), y cada posición es un atributo (columna).

# Atributos de Producto (en orden):
# [0] id_producto | [1] categoria | [2] nombre | [3] precio_unitario

producto_1 = [1, "Escritura", "Lápiz negro HB", 350]
producto_2 = [2, "Escritura", "Bolígrafo azul", 500]

# Armamos la tabla: una lista de registros (matriz)
productos = [producto_1, producto_2]

# Acceder a un atributo específico: hay que recordar el índice (poco legible)
print("Precio de producto_1:", producto_1[3])  # → 350

# Mostrar todos los registros
print("\nTabla Producto (con listas):")
for p in productos:
    print(p)

# PROBLEMA con las listas: para saber qué es cada dato,
# hay que recordar el índice. Si cambia el orden, todo se rompe.


# ============================================================
# PARTE 2 — REPRESENTACIÓN CON DICCIONARIOS
# ============================================================

# Refactorizamos: cada registro ahora es un diccionario.
# Los atributos se acceden por nombre (clave), no por posición.

print("\n--- Usando Diccionarios ---")

# Atributos: id_producto | categoria | nombre | precio_unitario
producto_1 = {
    "id_producto": 1,
    "categoria": "Escritura",
    "nombre": "Lápiz negro HB",
    "precio_unitario": 350
}

producto_2 = {
    "id_producto": 2,
    "categoria": "Escritura",
    "nombre": "Bolígrafo azul",
    "precio_unitario": 500
}

# La tabla sigue siendo una lista, pero ahora cada elemento es un diccionario
productos = [producto_1, producto_2]

# Acceder a un atributo: mucho más legible y robusto
print("Precio de producto_1:", producto_1["precio_unitario"])  # → 350

# Mostrar todos los registros
print("\nTabla Producto (con diccionarios):")
for p in productos:
    print(p)


# ============================================================
# PARTE 3 — OPERACIONES CRUD BÁSICAS (con diccionarios)
# ============================================================

# CRUD = Create, Read, Update, Delete
# Son las 4 operaciones fundamentales sobre cualquier conjunto de datos.

# --- CREATE: agregar un nuevo registro ---
producto_3 = {
    "id_producto": 3,
    "categoria": "Escritura",
    "nombre": "Marcador permanente",
    "precio_unitario": 1200
}
productos.append(producto_3)
print("\n[CREATE] Producto agregado:", producto_3)

# --- READ: buscar un registro por su clave primaria ---
id_buscado = 2
resultado = None
for p in productos:
    if p["id_producto"] == id_buscado:
        resultado = p
        break  # encontramos el registro, no hace falta seguir buscando
print(f"\n[READ] Producto con id {id_buscado}:", resultado)

# --- UPDATE: modificar un atributo de un registro existente ---
for p in productos:
    if p["id_producto"] == 1:
        p["precio_unitario"] = 400  # actualizamos el precio
        print("\n[UPDATE] Precio actualizado:", p)
        break

# --- DELETE: eliminar un registro por su clave primaria ---
id_a_eliminar = 3
productos = [p for p in productos if p["id_producto"] != id_a_eliminar]
print(f"\n[DELETE] Tabla luego de eliminar id {id_a_eliminar}:")
for p in productos:
    print(p)