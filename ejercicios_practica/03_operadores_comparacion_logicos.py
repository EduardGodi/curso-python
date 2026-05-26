# 🎓 EJERCICIO 3: Operadores de Comparación y Lógicos
# ------------------------------------------------------------------
# En tu proyecto, tomarás decisiones constantemente: ¿el objeto está lo suficientemente
# cerca? ¿el modelo está seguro de lo que ve? ¿se cumplen ambas condiciones?

print("--- EJERCICIO 3: OPERADORES DE COMPARACIÓN Y LÓGICOS ---")

# 1. Umbral de Confianza (Threshold):
# Para evitar falsos positivos, solo procesamos detecciones con confianza mayor a 0.80.
# Si el modelo de Mediapipe detecta una mano con una confianza de 0.87:
confianza_deteccion = 0.87

# Compara si 'confianza_deteccion' es mayor o igual a 0.80 y guarda el resultado en 'es_valida':
# (Debe ser un valor booleano: True o False)

# TU CÓDIGO AQUÍ:
es_valida = confianza_deteccion >= 0.80


# 2. Rango de Coordenadas:
# Queremos saber si la punta del dedo índice se encuentra dentro de un "área de botón virtual".
# El botón virtual está en el eje X entre 200 y 400 píxeles.
# Si la coordenada actual del dedo en X es:
dedo_x = 310

# Evalúa si 'dedo_x' es mayor o igual a 200 Y menor o igual a 400.
# Guarda el resultado en 'dedo_en_boton' usando operadores de comparación y el operador lógico 'and'.

# TU CÓDIGO AQUÍ:
dedo_en_boton = dedo_x >= 200 and dedo_x <= 400


# 3. Alertas de Seguridad o Gestos:
# Supongamos que estamos controlando una interfaz.
# Queremos activar una accón si "se detecta la mano izquierda" O si "la confianza de la mano derecha es alta".
mano_izquierda_detectada = False
mano_derecha_detectada = True
confianza_derecha = 0.92

# Escribe una condición que evalúe si:
# - 'mano_izquierda_detectada' es True
# O
# - 'mano_derecha_detectada' es True Y 'confianza_derecha' es mayor a 0.85
# Guarda el resultado en la variable 'activar_control':

# TU CÓDIGO AQUÍ:
activar_control = mano_izquierda_detectada or (mano_derecha_detectada and confianza_derecha > 0.85)


# 4. Operador de Negación (not):
# Si la cámara está apagada, debemos lanzar un error.
camara_encendida = False

# Evalúa si la cámara NO está encendida usando el operador 'not' y la variable 'camara_encendida'.
# Guarda el resultado en 'lanzar_alerta'.

# TU CÓDIGO AQUÍ:
lanzar_alerta = not camara_encendida

# ------------------------------------------------------------------
# 🛑 NO MODIFIQUES ESTAS LÍNEAS DE PRUEBA
print("\n--- Verificación de Resultados ---")
try:
    print(f"1. Detección válida: {es_valida} (esperado True)")
    print(f"2. Dedo dentro de botón: {dedo_en_boton} (esperado True)")
    print(f"3. Activar control: {activar_control} (esperado True)")
    print(f"4. Lanzar alerta de cámara: {lanzar_alerta} (esperado True)")
except Exception as e:
    print(f"Ocurrió un error en la verificación. Detalle: {e}")
