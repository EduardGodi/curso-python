# 🎓 EJERCICIO B: Semáforo de Confianza 🚦
# ------------------------------------------------------------------
# MediaPipe devuelve un valor de confianza entre 0.0 y 1.0 cada vez
# que detecta una mano. Tu sistema necesita clasificar ese valor en
# 4 niveles de alerta, como un semáforo extendido.
#
# RANGOS DE CONFIANZA:
# 🔴 ROJO    : 0.0 hasta 0.50 (inclusive) → Falsa alarma, ignorar.
# 🟠 NARANJA : Mayor a 0.50 hasta 0.70 (inclusive) → Detección dudosa, registrar.
# 🟡 AMARILLO: Mayor a 0.70 hasta 0.90 (inclusive) → Detección probable, advertir.
# 🟢 VERDE   : Mayor a 0.90 hasta 1.0 (inclusive)  → Detección confirmada, alertar.
#
# REGLA OBLIGATORIA:
# Debes usar comparaciones encadenadas en TODAS tus condiciones.
# ✅ Correcto:  0.50 < confianza <= 0.70
# ❌ Prohibido: confianza > 0.50 and confianza <= 0.70
#
# Esto es para que practiques y te acostumbres a la sintaxis de Python.
# ------------------------------------------------------------------

print("--- EJERCICIO B: SEMÁFORO DE CONFIANZA ---")

# Valor de confianza de MediaPipe (puedes cambiarlo para probar)
confianza = 0.85
color_semaforo = ""
accion = ""

# INSTRUCCIONES:
# 1. Evalúa 'confianza' y asigna el color correcto a 'color_semaforo'.
# 2. Según el color, asigna también el valor correcto a 'accion':
#    - ROJO     → accion = "Ignorar detección."
#    - NARANJA  → accion = "Registrar en log."
#    - AMARILLO → accion = "Enviar advertencia."
#    - VERDE    → accion = "Activar buzzer y enviar alerta a Telegram."
# 3. Imprime: "Confianza X.XX → 🎨 COLOR: [accion]"
#    Ejemplo:  "Confianza 0.85 → 🟡 AMARILLO: Enviar advertencia."

# TU CÓDIGO AQUÍ:

if 0.0 < confianza <=0.50:
    color_semaforo = "ROJO"
    accion = "Ignorar detección."
elif 0.50 < confianza <= 0.70:
    color_semaforo = "NARANJA"
    accion = "Registrar en el log."
elif 0.70 < confianza <= 0.90:
    color_semaforo = "AMARILLO"
    accion = "Enviar advertencia."
else:
    color_semaforo = "VERDE"
    accion = "Activar Buzzer y enviar alerta a Telegram."
    
    
    

# ------------------------------------------------------------------
# 🛑 NO MODIFIQUES ESTAS LÍNEAS DE PRUEBA
print("\n--- Verificación de Resultados ---")
try:
    if confianza == 0.85:
        assert color_semaforo == "AMARILLO", f"Error: Con confianza=0.85 el color debería ser 'AMARILLO', obtuviste '{color_semaforo}'"
        assert accion == "Enviar advertencia.", f"Error: La acción debería ser 'Enviar advertencia.', obtuviste '{accion}'"
        print("✅ ¡Semáforo calibrado correctamente!")
    else:
        print("⚠️ No cambies el valor de confianza para la verificación final. Debe ser 0.85")
except AssertionError as e:
    print(f"❌ {e}")
except NameError as e:
    print(f"❌ Revisa que 'color_semaforo' y 'accion' estén definidas. Detalle: {e}")
