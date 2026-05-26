# 🎓 EJERCICIO 2: Operadores Aritméticos en Visión Artificial
# ------------------------------------------------------------------
# En OpenCV, las imágenes son matrices de píxeles. Para dibujar círculos o líneas,
# necesitamos calcular posiciones usando matemáticas básicas.

print("--- EJERCICIO 2: OPERADORES ARITMÉTICOS ---")

# Datos iniciales para el ejercicio
ancho_pantalla = 640
alto_pantalla = 480

# 1. Normalización a Píxeles:
# Mediapipe nos entrega coordenadas normalizadas (valores entre 0.0 y 1.0).
# Para dibujarlos con OpenCV, debemos multiplicarlos por el ancho y alto en píxeles.
# Si la coordenada normalizada de un dedo es:
x_normalizada = 0.75
y_normalizada = 0.40

# Calcula las coordenadas reales en píxeles ('x_pixel' e 'y_pixel'):
# Multiplica 'x_normalizada' por 'ancho_pantalla', e 'y_normalizada' por 'alto_pantalla'.
# Tip: Convierte el resultado a entero usando int(...) ya que OpenCV no dibuja en "medio píxel".

# TU CÓDIGO AQUÍ:
x_pixel = int(x_normalizada * ancho_pantalla);
y_pixel = int(y_normalizada*alto_pantalla);


# 2. Encontrar el punto medio (Centro):
# Queremos saber el punto medio entre dos dedos (por ejemplo, el índice y el pulgar).
# Las coordenadas son:
# Dedo índice: x1 = 120, y1 = 300
# Dedo pulgar: x2 = 200, y2 = 360
x1, y1 = 120, 300
x2, y2 = 200, 360

# Calcula el punto medio ('x_medio' e 'y_medio') usando la fórmula matemática:
# x_medio = (x1 + x2) / 2
# y_medio = (y1 + y2) / 2
# Usa el operador de división entera (//) para asegurarte de que el resultado sea un número entero.

# TU CÓDIGO AQUÍ:
x_medio = (x1+y1)/2
y_medio = (x2+y2)/2


# 3. Escalar una caja de detección (Bounding Box):
# Supongamos que OpenCV detecta una cara en un cuadrado de 100x100 píxeles.
# Queremos agrandar esa caja de detección en un 50% (es decir, multiplicarla por 1.5).
caja_ancho = 100
caja_alto = 100

# Calcula el nuevo tamaño ('caja_ancho_escalada' y 'caja_alto_escalada')
# aplicando el incremento. Asegúrate de que el tipo de dato final sea un entero (int).

# TU CÓDIGO AQUÍ:
caja_ancho_escalada = int(caja_ancho*1.5)
caja_alto_escalada = int(caja_alto*1.5)


# 4. Operador Módulo (%):
# En un bucle de video, a veces no queremos procesar todos los frames (para no ralentizar la PC).
# Queremos procesar solo 1 de cada 5 frames. El operador módulo (%) nos ayuda a saber si un número es divisible.
frame_actual = 25

# Calcula el residuo de dividir 'frame_actual' entre 5 en la variable 'es_divisible_5':
# TU CÓDIGO AQUÍ:
es_divisible_5 = frame_actual%5


# ------------------------------------------------------------------
# 🛑 NO MODIFIQUES ESTAS LÍNEAS DE PRUEBA
print("\n--- Verificación de Resultados ---")
try:
    print(f"1. Coordenadas píxel calculadas: X = {x_pixel} (esperado 480), Y = {y_pixel} (esperado 192)")
    print(f"2. Punto medio calculado: X = {x_medio} (esperado 160), Y = {y_medio} (esperado 330)")
    print(f"3. Caja de detección escalada: Ancho = {caja_ancho_escalada} (esperado 150), Alto = {caja_alto_escalada} (esperado 150)")
    print(f"4. Residuo de frame_actual % 5: {es_divisible_5} (esperado 0)")
except Exception as e:
    print(f"Ocurrió un error en la verificación. Detalle: {e}")
