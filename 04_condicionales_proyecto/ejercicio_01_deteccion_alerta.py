# 🎓 EJERCICIO 1: Decisión de Alerta por Confianza
# ------------------------------------------------------------------
# Tu cámara IP Hikvision enviará un flujo constante de fotogramas.
# MediaPipe analizará cada fotograma y nos devolverá la confianza de
# detección de la mano (de 0.0 a 1.0).
# Debemos decidir si activamos las alertas en función de este valor.

print("--- EJERCICIO 1: ALERTA POR CONFIANZA ---")

# Variables iniciales (puedes cambiar este valor para probar tu código)
confianza_deteccion = 0.88
buzzer_activo = False
telegram_enviado = False

# INSTRUCCIONES:
# Escribe una estructura condicional (if, elif, else) que evalúe 'confianza_deteccion':
# 
# 1. Si la confianza es mayor o igual a 0.85:
#    - Imprime el mensaje: "Mano detectada con alta confianza. ¡Activando buzzer y enviando Telegram!"
#    - Cambia 'buzzer_activo' a True
#    - Cambia 'telegram_enviado' a True
# 2. Si la confianza es menor a 0.85 pero mayor o igual a 0.50:
#    - Imprime el mensaje: "Detección débil. Monitoreando..."
#    - Mantén 'buzzer_activo' y 'telegram_enviado' en False
# 3. Si la confianza es menor a 0.50:
#    - Imprime el mensaje: "No hay manos detectadas en el rango aceptable."
#    - Mantén 'buzzer_activo' y 'telegram_enviado' en False

# TU CÓDIGO AQUÍ:



# ------------------------------------------------------------------
# 🛑 NO MODIFIQUES ESTAS LÍNEAS DE PRUEBA
print("\n--- Verificación de Resultados ---")
try:
    # Verificación para confianza_deteccion = 0.88
    if confianza_deteccion >= 0.85:
        assert buzzer_activo == True, "Error: El buzzer debería estar activo para confianza >= 0.85"
        assert telegram_enviado == True, "Error: El mensaje de Telegram debería haberse enviado"
        print("✅ ¡Prueba superada con éxito para alta confianza!")
    else:
        print("⚠️ Cambiaste el valor de confianza_deteccion. Recuerda dejarlo en 0.88 para la verificación final.")
except AssertionError as e:
    print(f"❌ {e}")
except NameError as e:
    print(f"❌ Asegúrate de que las variables 'buzzer_activo' y 'telegram_enviado' existan y estén bien escritas. Detalle: {e}")
