# 🎓 EJERCICIO 3: Filtro de Falsos Positivos (Condicionales Anidados)
# ------------------------------------------------------------------
# Para evitar activar el buzzer de forma innecesaria o cuando la cámara
# está desconectada, usaremos condicionales anidados.
#
# Primero verificamos la conexión de la cámara, y solo si está activa
# analizamos los datos de confianza y el estado del buzzer.

print("--- EJERCICIO 3: FILTRO DE FALSOS POSITIVOS ---")

# Variables iniciales (puedes cambiar estos valores para hacer pruebas)
camara_conectada = True
confianza_deteccion = 0.95
buzzer_encendido = False

# Variables de salida que debes actualizar en tu código:
sistema_activo = False
cambiar_estado_buzzer = False

# INSTRUCCIONES:
# Escribe una estructura de condicionales anidados:
# 
# 1. Si 'camara_conectada' es False:
#    - Imprime: "Error: Cámara Hikvision fuera de línea."
#    - Asigna a 'sistema_activo' el valor False
# 2. Si 'camara_conectada' es True:
#    - Asigna a 'sistema_activo' el valor True
#    - AHORA, dentro de este bloque, evalúa 'confianza_deteccion':
#      - Si 'confianza_deteccion' es mayor a 0.90:
#        - Si el buzzer NO está encendido ('buzzer_encendido' es False):
#          * Imprime: "¡Alerta confirmada! Encendiendo buzzer..."
#          * Asigna a 'cambiar_estado_buzzer' el valor True
#        - Si el buzzer ya está encendido ('buzzer_encendido' es True):
#          * Imprime: "La alerta continúa, pero el buzzer ya está activo."
#          * Asigna a 'cambiar_estado_buzzer' el valor False
#      - Si 'confianza_deteccion' es menor o igual a 0.90:
#        * Imprime: "Señal de video estable. Sin novedades."
#        * Asigna a 'cambiar_estado_buzzer' el valor False

# TU CÓDIGO AQUÍ:



# ------------------------------------------------------------------
# 🛑 NO MODIFIQUES ESTAS LÍNEAS DE PRUEBA
print("\n--- Verificación de Resultados ---")
try:
    if camara_conectada == True and confianza_deteccion == 0.95 and buzzer_encendido == False:
        assert sistema_activo == True, "Error: El sistema debería estar activo si la cámara está conectada."
        assert cambiar_estado_buzzer == True, "Error: Se debería encender el buzzer si la confianza es > 0.90 y estaba apagado."
        print("✅ ¡Prueba superada con éxito para cámara conectada y alerta confirmada!")
    else:
        print("⚠️ Cambiaste los valores de entrada. Restáuralos a camara_conectada=True, confianza_deteccion=0.95, buzzer_encendido=False para la verificación final.")
except AssertionError as e:
    print(f"❌ {e}")
except NameError as e:
    print(f"❌ Revisa que todas las variables de salida estén bien escritas y declaradas. Detalle: {e}")
