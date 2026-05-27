# 📚 Mi Progreso de Aprendizaje - Python (Ruta al Proyecto Final)

Este archivo es nuestro registro persistente para llevar un seguimiento de tu aprendizaje. Como tu tutor de Python, iré actualizando este documento para registrar los temas que vemos, tus fortalezas, las áreas que debemos reforzar y los próximos retos.

---

## 🎯 Meta Final: Proyecto Cámara IP + Detección de Manos + Telegram & Buzzer
* **Fecha de entrega:** 6 de Junio de 2026 (~11 días)
* **Objetivo:** Conectar una cámara IP Hikvision, detectar manos en tiempo real usando MediaPipe, activar un buzzer físico/simulado y enviar notificaciones de alerta con foto por Telegram al detectar una mano.
* **Metodología de Aprendizaje:** Práctica basada en retos (ejercicios de código estructurados) aplicados al contexto del proyecto final para evitar el aburrimiento y acelerar la asimilación.

## ⚙️ Reglas de la Sesión
* **Modo de Intervención:** El tutor solo analiza y lee el contexto de los ejercicios. No debe editar ningún archivo de código hasta que el estudiante pida explícitamente revisar o corregir.
* **Corrección No Destructiva:** Cuando el estudiante pida corregir un código, el tutor **no debe borrar el código del estudiante**. En su lugar, mantendrá el código original intacto y agregará la solución/corrección en la parte inferior del archivo (claramente diferenciada) para facilitar la comparación y el aprendizaje del error.
* **Git — El estudiante maneja sus propios commits:** El tutor nunca ejecutará comandos `git`. En su lugar, sugerirá el mensaje de commit en formato **Conventional Commits** (`tipo(scope): descripción`) para que el estudiante lo use al hacer `git commit` manualmente. Esto refuerza el aprendizaje de Git y GitHub.

---

## 📅 Plan de Ruta Acelerada (26-May al 06-Jun)

| Fase | Temas de Python | Aplicación al Proyecto | Estado |
| :--- | :--- | :--- | :--- |
| **Fase 1** | Condicionales (`if`, `elif`, `else`) | Tomar decisiones basadas en confianza de detección y coordenadas de la mano. | ✅ Completada |
| **Fase 2** | Bucles y Bucles Infinitos (`while`, `for`) | Simular y entender el procesamiento continuo de fotogramas de la cámara. | ⏳ Pendiente |
| **Fase 3** | Funciones y Módulos | Crear funciones reutilizables para enviar mensajes a Telegram y activar el buzzer. | ⏳ Pendiente |
| **Fase 4** | Listas y Diccionarios | Almacenar coordenadas de la mano (puntos de referencia de MediaPipe). | ⏳ Pendiente |
| **Fase 5** | OpenCV y Cámara IP | Conectar el stream RTSP de la cámara Hikvision en Python. | ⏳ Pendiente |
| **Fase 6** | Integración con MediaPipe | Detección de manos, landmarks y cálculo de distancias. | ⏳ Pendiente |
| **Fase 7** | Alertas y Buzzer | Programar el envío real a Telegram y la señal del buzzer. | ⏳ Pendiente |
| **Fase 8** | Pruebas e Integración Final | Integrar todo el pipeline de software y hardware. | ⏳ Pendiente |

---

## 📊 Historial de Sesiones (¡No borrar!)

* **Sesión 1 (2026-05-26 - Tarde):**
  * **Logro:** Corrección de la lógica de evaluación condicional y el funcionamiento de la negación (`not`) en el ejercicio 3.
  * **Decisión estratégica:** El estudiante comparte su proyecto de fin de curso (Cámara Hikvision + MediaPipe + Telegram + Buzzer) con fecha límite del 6 de Junio. Se diseña una ruta intensiva basada en ejercicios prácticos aplicados a este proyecto.
  * **Siguiente paso:** Crear carpeta `04_condicionales_proyecto` con 3 ejercicios contextualizados.

* **Sesión 2 (2026-05-26 - Fin de sesión):**
  * **Estado de la carpeta `04_condicionales_proyecto`:**
    * `ejercicio_01_deteccion_alerta.py`: ¡Completado con éxito! Lógica condicional básica para alertas de confianza resuelta.
    * `ejercicio_02_zonas_seguridad.py`: Pendiente de realizar.
    * `ejercicio_03_filtro_falsos_positivos.py`: En progreso (avanzada la estructura de cámara conectada; queda pendiente anidar correctamente la comprobación del buzzer y corregir una comparación lógica `==` por asignación `=`).
  * **Estado al finalizar:** Sesión finalizada por el estudiante a mitad del bloque de condicionales.

* **Sesión 3 (2026-05-26 - Noche / Pre-cena):**
  * **Logro:** Establecimiento de reglas claras de tutoría (intervenciones no destructivas, añadir sugerencias abajo y esperar confirmación del estudiante). Se revirtió el código del estudiante a su estado original y se colocaron las sugerencias del tutor abajo en `ejercicio_02` y `ejercicio_03` para su posterior comparación. Se explicó la lógica detallada del error en el ejercicio 3.
  * **Siguiente paso:** El estudiante comparará los códigos al regresar de cenar para dar por concluida la Fase 1.

* **Sesión 4 (2026-05-27 - Mañana):**
  * **Logro:** ✅ **Fase 1 completada.** Los 3 ejercicios de `05_condicionales_refuerzo` fueron resueltos y verificados correctamente:
    * `ejercicio_A_el_if_trampa.py`: ✅ Análisis correcto del bug y corrección con `if/elif/else`.
    * `ejercicio_B_semaforo_confianza.py`: ✅ Semáforo de 4 niveles usando comparaciones encadenadas (regla obligatoria cumplida).
    * `ejercicio_C_decision_telegram.py`: ✅ Lógica multicondición con `and`, `or` y `not` funcionando.
  * **Commit sugerido:** `feat(condicionales): completar ejercicios de refuerzo 05`
  * **Siguiente paso:** Iniciar **Fase 2 — Bucles** (`while`, `for`).

---
*Nota: En cada nueva conversación que iniciemos, puedes decirme: "Tutor, lee mi progreso" y yo sabré exactamente en qué nos quedamos.*
