# 🎓 EJERCICIO C: Decisión Multicondición para Telegram 📱
# ------------------------------------------------------------------
# Tu sistema de detección necesita decidir si envía o no una notificación
# a Telegram. Pero no es tan simple como "si hay alerta → envía".
# Hay 3 variables que deben evaluarse juntas para tomar la decisión.
#
# VARIABLES DEL SISTEMA:
# - nivel_alerta          : Puede ser "ROJO", "AMARILLO" o "VERDE"
# - notificacion_reciente : True si ya se envió una notificación en los
#                           últimos 30 segundos (para no spamear Telegram)
# - notificaciones_activas: True si el usuario tiene las notifs activadas
#
# LÓGICA DE DECISIÓN:
#
# ✅ ENVIAR notificación SOLO si se cumplen LAS 3 condiciones a la vez:
#    1. notificaciones_activas es True
#    2. notificacion_reciente es False (no spamear)
#    3. nivel_alerta es "ROJO" o "AMARILLO" (el verde no genera alerta)
#
# Si se envía, el mensaje depende del nivel:
#    - ROJO     → mensaje = "🚨 ALERTA CRÍTICA: Mano en zona restringida."
#    - AMARILLO → mensaje = "⚠️ Advertencia: Mano cerca de zona de riesgo."
#
# ❌ Si NO se envía, imprime la razón específica:
#    - Si notificaciones_activas es False → "Notificaciones desactivadas por el usuario."
#    - Si notificacion_reciente es True   → "Notificación reciente. Esperando intervalo."
#    - Si nivel_alerta es "VERDE"         → "Sin novedad. No se requiere notificación."
#
# PISTA: Vas a necesitar 'and', 'or', y 'not' en este ejercicio.
# ------------------------------------------------------------------

print("--- EJERCICIO C: DECISIÓN MULTICONDICIÓN PARA TELEGRAM ---")

# Variables del sistema (puedes cambiarlas para probar distintos escenarios)
nivel_alerta = "ROJO"
notificacion_reciente = False
notificaciones_activas = True

# Variables de salida que debes actualizar:
enviar_notificacion = False
mensaje = ""

# TU CÓDIGO AQUÍ:
if notificaciones_activas == True and notificacion_reciente == False and nivel_alerta == "ROJO":
    mensaje = "🚨 ALERTA CRÍTICA: Mano en zona restringida."
    enviar_notificacion = True
elif notificaciones_activas == True and notificacion_reciente == False and nivel_alerta == "AMARILLO":
    mensaje = "⚠️ Advertencia: Mano cerca de zona de riesgo."
    enviar_notificacion = True
else:
    if not notificaciones_activas:
        print("Notificaciones desactivadas por el usuario.")
    if notificacion_reciente == True:
        print("Notificación reciente. Esperando intervalo.")
    else:
        print("Sin novedad. No se requiere notificación.")
    

# ------------------------------------------------------------------
# 🛑 NO MODIFIQUES ESTAS LÍNEAS DE PRUEBA
print("\n--- Verificación de Resultados ---")
try:
    if nivel_alerta == "ROJO" and not notificacion_reciente and notificaciones_activas:
        assert enviar_notificacion == True, "Error: Debería enviarse la notificación."
        assert mensaje == "🚨 ALERTA CRÍTICA: Mano en zona restringida.", f"Error: Mensaje incorrecto para ROJO. Obtuviste: '{mensaje}'"
        print("✅ ¡Decisión correcta! Notificación de alerta crítica enviada.")
    else:
        print("⚠️ Cambiaste los valores de entrada. Para la verificación usa: nivel_alerta='ROJO', notificacion_reciente=False, notificaciones_activas=True")
except AssertionError as e:
    print(f"❌ {e}")
except NameError as e:
    print(f"❌ Revisa que 'enviar_notificacion' y 'mensaje' estén definidas. Detalle: {e}")
