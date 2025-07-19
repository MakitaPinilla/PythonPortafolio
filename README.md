# 🎁 Tienda de Regalos - Descuento por Cumpleaños 🎂

Este es un programa básico en Python que simula el proceso de compra en una tienda de regalos, donde se ofrece un **descuento especial por cumpleaños** si se cumplen ciertas condiciones.

---

## 📌 ¿Qué hace este programa?

- Solicita al usuario si está de cumpleaños.
- Pide cuántos productos desea comprar (mínimo 3 para obtener descuento).
- Solicita los precios de cada producto.
- Calcula el total de la compra.
- Si es cumpleaños y se compran al menos 3 productos, aplica un descuento equivalente a la edad del cliente en porcentaje.
- Muestra el total, el descuento y el precio final.

---

## 🧠 Conceptos de Python aplicados

Este ejercicio cumple con los **5 (más 1) objetivos básicos de aprendizaje**:

1. **Variables y operadores**
   - Uso de variables para almacenar datos como edad, precios y totales.
   - Operadores matemáticos para calcular el descuento.

2. **Tipos de datos**
   - Cadenas (`str`), números enteros (`int`), flotantes (`float`) y booleanos (`bool`).

3. **Condicionales**
   - Uso de `if`, `else` y operadores lógicos (`and`, `not`) para tomar decisiones.

4. **Bucles**
   - Uso de `for` para pedir los precios de los productos.
   - Uso de `while` para validar si la respuesta de cumpleaños es válida.

5. **Estructuras de datos**
   - Uso de **listas** para almacenar los precios de los productos.

6. **Funciones**
   - Se utiliza una función externa (`pedir_respuesta_cumple`) ubicada en un archivo aparte (`def_tienda.py`) para modularizar el código y validar la respuesta del usuario.

---

## 🚀 Cómo ejecutar el programa

1. Asegúrate de tener ambos archivos en la misma carpeta:
   - `tienda.py` (programa principal)
   - `def_tienda.py` (función importada)

2. Ejecuta el programa con Python:

```bash
python tienda.py
