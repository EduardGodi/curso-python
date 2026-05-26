# 🚦 Ejercicios: Condicionales aplicados al Proyecto de Detección

En esta sección aprenderás a utilizar estructuras condicionales (`if`, `elif`, `else`) para que tu sistema tome decisiones autónomas en base a la información que recibe de la cámara Hikvision y el modelo MediaPipe.

---

## 📝 Ejercicios a Resolver:

### 1. [ejercicio_01_deteccion_alerta.py](file:///C:/xampp/htdocs/curso-python/04_condicionales_proyecto/ejercicio_01_deteccion_alerta.py)
**Objetivo:** Decidir si activar los actuadores (notificación y buzzer) según la confianza de la detección.
* **Instrucciones:**
  * Si la confianza es mayor o igual a 0.85:
    * Imprime: `"Mano detectada con alta confianza. ¡Activando buzzer y enviando Telegram!"`
    * Cambia las variables `buzzer_activo` y `telegram_enviado` a `True`.
  * Si la confianza es menor a 0.85 pero mayor o igual a 0.50:
    * Imprime: `"Detección débil. Monitoreando..."`
  * Si es menor a 0.50:
    * Imprime: `"No hay manos detectadas en el rango aceptable."`

### 2. [ejercicio_02_zonas_seguridad.py](file:///C:/xampp/htdocs/curso-python/04_condicionales_proyecto/ejercicio_02_zonas_seguridad.py)
**Objetivo:** Determinar el nivel de peligro según las coordenadas X e Y de la mano detectada.
* **Instrucciones:**
  * Imaginemos que la pantalla de la cámara mide 640 píxeles de ancho (X) y 480 de alto (Y). La zona peligrosa es el centro: X entre 200 y 440 (inclusive), Y entre 150 y 330 (inclusive).
  * Evalúa las coordenadas de la mano (`mano_x` y `mano_y`):
    * Si la mano está dentro de este recuadro central (tanto en X como en Y):
      * Establece `nivel_alerta` en `"ROJO"` e imprime `"¡ALERTA MÁXIMA! Mano en zona restringida."`
    * Si la mano no está en la zona roja, pero está en la zona de advertencia (X entre 100 y 540 inclusive, Y entre 50 y 430 inclusive):
      * Establece `nivel_alerta` en `"AMARILLO"` e imprime `"Advertencia: Mano cerca de zona restringida."`
    * De lo contrario:
      * Establece `nivel_alerta` en `"VERDE"` e imprime `"Estado seguro."`

### 3. [ejercicio_03_filtro_falsos_positivos.py](file:///C:/xampp/htdocs/curso-python/04_condicionales_proyecto/ejercicio_03_filtro_falsos_positivos.py)
**Objetivo:** Evitar falsas alertas combinando el estado de la cámara, la confianza y el estado del buzzer mediante condicionales anidados.
* **Instrucciones:**
  * Primero, verifica si la cámara IP Hikvision está conectada (`camara_conectada == True`):
    * Si NO está conectada, imprime `"Error: Cámara Hikvision fuera de línea."` y pon `sistema_activo` en `False`.
    * Si está conectada, pon `sistema_activo` en `True` y evalúa la confianza de la detección:
      * Si la confianza es superior a 0.90 y el buzzer no está ya encendido (`buzzer_encendido == False`):
        * Imprime `"¡Alerta confirmada! Encendiendo buzzer..."` y pon `cambiar_estado_buzzer` en `True`.
      * Si la confianza es superior a 0.90 pero el buzzer ya está encendido:
        * Imprime `"La alerta continúa, pero el buzzer ya está activo."` y pon `cambiar_estado_buzzer` en `False`.
      * Si la confianza es menor o igual a 0.90:
        * Imprime `"Señal de video estable. Sin novedades."` y pon `cambiar_estado_buzzer` en `False`.

---

## 🏃 Cómo verificar tus respuestas:
Ejecuta cada script desde tu terminal. Cada uno incluye pruebas automáticas al final para indicarte si tu código funciona correctamente.
