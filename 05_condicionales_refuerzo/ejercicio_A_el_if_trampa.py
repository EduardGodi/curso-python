# 🎓 EJERCICIO A: El if Trampa 🪤
# ------------------------------------------------------------------
# Uno de los errores más peligrosos en programación es el "hueco lógico":
# cuando usas varios 'if' sueltos en vez de 'if/elif/else', puedes crear
# situaciones donde más de un bloque se ejecuta, o donde ninguno lo hace.
#
# Abajo tienes un código BUGUEADO que analiza la confianza de detección
# de MediaPipe. Parece correcto a primera vista, pero tiene 2 bugs.
#
# TU MISIÓN:
# 1. Ejecuta el código tal como está y observa la salida.
# 2. En la sección de análisis, escribe en comentarios QUÉ está mal y POR QUÉ.
# 3. En la sección de corrección, reescribe el código correctamente.
# ------------------------------------------------------------------

print("--- EJERCICIO A: EL IF TRAMPA ---")

confianza_deteccion = 0.75
estado_sistema = ""

# ============================================================
# ⚠️  CÓDIGO BUGUEADO — No modificar esta sección
# ============================================================
print("\n[Resultado del código bugueado:]")

if confianza_deteccion > 0.90:
    print("🔴 Alerta crítica: Mano detectada con alta confianza.")
    estado_sistema = "CRITICO"

if confianza_deteccion > 0.60:
    print("🟡 Alerta moderada: Posible detección.")
    estado_sistema = "MODERADO"

if confianza_deteccion < 0.60:
    print("🟢 Sin alerta: Confianza baja.")
    estado_sistema = "NORMAL"

print(f"Estado final del sistema: {estado_sistema}")

# ============================================================
# 📝 PARTE 1 — Tu análisis (escribe en comentarios)
# ============================================================
# Pregunta 1: ¿Qué imprime el código cuando confianza_deteccion = 0.75?
# Tu respuesta:

# Pregunta 2: ¿Cuántos bloques 'if' se ejecutan con ese valor? ¿Por qué?
# Tu respuesta:

# Pregunta 3: ¿Qué valor tiene 'estado_sistema' al final? ¿Es el correcto?
# Tu respuesta:

# Pregunta 4: ¿Qué pasa si confianza_deteccion = 0.95? ¿Cuántos bloques se ejecutan?
# Tu respuesta:

# Pregunta 5: ¿Hay algún valor de confianza que no entre en ningún bloque? ¿Cuál?
# Tu respuesta:

# ============================================================
# 🔧 PARTE 2 — Tu corrección
# ============================================================
# Reescribe el código correctamente usando if / elif / else.
# Las reglas son:
# 🔴 CRITICO  : confianza mayor a 0.90
# 🟡 MODERADO : confianza entre 0.60 y 0.90 (inclusive en ambos extremos)
# 🟢 NORMAL   : confianza menor a 0.60
#
# Con confianza = 0.75, el resultado correcto debe ser MODERADO.

print("\n[Tu corrección:]")
estado_sistema = ""  # Reiniciamos la variable

# TU CÓDIGO AQUÍ:


# ------------------------------------------------------------------
# 🛑 NO MODIFIQUES ESTAS LÍNEAS DE PRUEBA
print("\n--- Verificación de Resultados ---")
try:
    if confianza_deteccion == 0.75:
        assert estado_sistema == "MODERADO", f"Error: Con confianza=0.75 el estado debería ser 'MODERADO', obtuviste '{estado_sistema}'"
        print("✅ ¡Corrección exitosa! El hueco lógico fue eliminado.")
    else:
        print("⚠️ No cambies el valor de confianza_deteccion para la verificación final.")
except AssertionError as e:
    print(f"❌ {e}")
except NameError as e:
    print(f"❌ La variable 'estado_sistema' no está definida. Detalle: {e}")
