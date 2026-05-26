# 🎓 EJERCICIO 1: Variables y Tipos de Datos (Orientado a Mediapipe)
# ------------------------------------------------------------------
# En Mediapipe, cuando detectamos una mano o cara, recibimos coordenadas (X, Y)
# y listas de puntos (landmarks). Vamos a practicar cómo representar esto en Python.

print("--- EJERCICIO 1: VARIABLES Y TIPOS DE DATOS ---")

# 1. Variables Simples:
# Declara una variable llamada 'resolucion_ancho' con el valor 1280 (tipo int)
# Declara una variable llamada 'resolucion_alto' con el valor 720 (tipo int)
# Declara una variable llamada 'nombre_proyecto' con el texto "Detector de Gestos" (tipo string)

# TU CÓDIGO AQUÍ:
resolucion_ancho = 128;
resolucion_alto = 720;
nombre_proyecto = "Detector de gestos";


# 2. Tuplas:
# Las tuplas se usan para datos que no van a cambiar, como una coordenada (X, Y).
# Declara una tupla llamada 'punto_indice' que contenga las coordenadas X e Y de la punta del dedo índice:
# El valor de X es 350, y el valor de Y es 480.

# TU CÓDIGO AQUÍ:
punto_indice = (350,480);


# 3. Listas:
# Las listas guardan secuencias de datos que sí podemos modificar.
# Mediapipe detecta 21 puntos (landmarks) de la mano. 
# Crea una lista llamada 'dedo_pulgar' que contenga 4 tuplas (cada una con coordenadas X, Y):
# - Tupla 1 (base): (100, 500)
# - Tupla 2: (120, 480)
# - Tupla 3: (140, 470)
# - Tupla 4 (punta): (160, 465)

# TU CÓDIGO AQUÍ:
dedo_pulgar = [(100,500), (120,480), (140,470), (160,465)];


# 4. Diccionarios:
# Los diccionarios nos permiten etiquetar los datos con "claves" (keys).
# Crea un diccionario llamado 'mano_detectada'. Debe tener las siguientes claves y valores:
# - "id": 1
# - "tipo": "Izquierda" (un string)
# - "confianza": 0.95 (un float que representa el 95% de seguridad)
# - "punto_clave": punto_indice (la tupla que creaste en el paso 2)

# TU CÓDIGO AQUÍ:
mano_detectada = {
    "id": 1,
    "tipo": "Izquierda",
    "confianza": 0.95,
    "punto_clave": punto_indice
}


# 5. Concatenación (f-strings):
# Imprime un mensaje usando f-strings que diga exactamente:
# "Proyecto: [nombre_proyecto] corriendo a [resolucion_ancho]x[resolucion_alto] píxeles."
# Reemplaza los corchetes con las variables correspondientes.

# TU CÓDIGO AQUÍ:
# print(...)


# ------------------------------------------------------------------
# 🛑 NO MODIFIQUES ESTAS LÍNEAS DE PRUEBA (sirven para verificar tu código)
print("\n--- Verificación de Resultados ---")
try:
    print(f"Resolución: {resolucion_ancho}x{resolucion_alto} | Proyecto: {nombre_proyecto}")
    print(f"Tipo de punto_indice: {type(punto_indice).__name__} | Valor: {punto_indice}")
    print(f"Elementos en dedo_pulgar: {len(dedo_pulgar)} | Punta: {dedo_pulgar[-1] if dedo_pulgar else None}")
    print(f"Mano detectada -> ID: {mano_detectada.get('id')}, Lado: {mano_detectada.get('tipo')}, Confianza: {mano_detectada.get('confianza')}")
except Exception as e:
    print(f"Ocurrió un error en la verificación. ¿Completaste todas las variables? Detalle: {e}")
