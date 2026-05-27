# 🎓 EJERCICIO 2: Zonas de Seguridad en Pantalla
# ------------------------------------------------------------------
# Queremos que la alerta solo sea MÁXIMA si la mano entra en un recuadro
# específico en el centro de la pantalla de la cámara (por ejemplo,
# sobre una máquina peligrosa).
# 
# La cámara Hikvision captura una resolución de 640x480 píxeles.
# - Rango X total: 0 a 640
# - Rango Y total: 0 a 480
# 
# ZONAS DE ALERTA:
# 🔴 Zona ROJA (Peligro): X entre 200 y 440 (inclusive), Y entre 150 y 330 (inclusive).
# 🟡 Zona AMARILLA (Advertencia): X entre 100 y 540 (inclusive), Y entre 50 y 430 (inclusive), pero fuera de la zona roja.
# 🟢 Zona VERDE (Seguro): Cualquier otra coordenada fuera de las anteriores.

print("--- EJERCICIO 2: ZONAS DE SEGURIDAD ---")

# Coordenadas actuales de la mano (puedes cambiar estos valores para probar)
mano_x = 300
mano_y = 200
nivel_alerta = ""  # Deberás cambiar este valor a "ROJO", "AMARILLO" o "VERDE" según corresponda.

# INSTRUCCIONES:
# Escribe la lógica condicional para evaluar 'mano_x' y 'mano_y':
# 1. Si está en la zona ROJA:
#    - Imprime: "¡ALERTA MÁXIMA! Mano en zona restringida."
#    - Asigna a 'nivel_alerta' el valor "ROJO"
# 2. Si está en la zona AMARILLA:
#    - Imprime: "Advertencia: Mano cerca de zona restringida."
#    - Asigna a 'nivel_alerta' el valor "AMARILLO"
# 3. De lo contrario (zona VERDE):
#    - Imprime: "Estado seguro."
#    - Asigna a 'nivel_alerta' el valor "VERDE"

# TU CÓDIGO AQUÍ:
if 200 <= mano_x <= 440 and 150 <= mano_y <=330:
    print("¡ALERTA MÁXIMA! Mano en zona restringida.")
    nivel_alerta = "ROJO"
elif 100 <= mano_x <= 540 and 50 <= mano_y <= 430:
    print("Advertencia: Mano cerca de zona restringida.")
    nivel_alerta = "AMARILLO"
else:
    print("Estado seguro.")
    nivel_alerta = "VERDE"


# --- CÓDIGO SUGERIDO POR EL TUTOR ---
# if 200 <= mano_x <= 440 and 150 <= mano_y <= 330:
#     print("¡ALERTA MÁXIMA! Mano en zona restringida.")
#     nivel_alerta = "ROJO"
# elif 100 <= mano_x <= 540 and 50 <= mano_y <= 430:
#     print("Advertencia: Mano cerca de zona restringida.")
#     nivel_alerta = "AMARILLO"
# else:
#     print("Estado seguro.")
#     nivel_alerta = "VERDE"

# ------------------------------------------------------------------
# 🛑 NO MODIFIQUES ESTAS LÍNEAS DE PRUEBA
print("\n--- Verificación de Resultados ---")
try:
    if mano_x == 300 and mano_y == 200:
        assert nivel_alerta == "ROJO", f"Error: Con X={mano_x} e Y={mano_y} la zona debería ser ROJO, obtuviste {nivel_alerta}"
        print("✅ ¡Prueba superada con éxito para la zona ROJA!")
    else:
        print("⚠️ Cambiaste los valores de mano_x o mano_y. Recuerda dejarlos en 300 y 200 para la verificación final.")
except AssertionError as e:
    print(f"❌ {e}")
except NameError as e:
    print(f"❌ La variable 'nivel_alerta' no está definida correctamente. Detalle: {e}")
