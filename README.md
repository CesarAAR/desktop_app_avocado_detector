# Fruit Detection System (Avocado) 🥑

Este proyecto es una herramienta de escritorio profesional desarrollada en **Python** que implementa el modelo **YOLO11s** para la detección, conteo y análisis de confianza de aguacates en imágenes.

La aplicación permite un flujo de trabajo completo: desde la carga de archivos hasta la exportación de métricas, funcionando de manera **100% offline** para garantizar privacidad y operatividad en cualquier entorno.

-----

## 📸 Evidencia y Demo

### 1\. Interfaz Principal

Diseño moderno utilizando `ttkbootstrap` con una disposición de paneles para navegación, visualización y métricas.
![alt text](https://github.com/CesarAAR/desktop_app_avocado_detector/blob/main/capturas/main_screen.png "Main Screen")

### 2\. Procesamiento de Imágenes

Detección precisa de objetos con anotaciones automáticas (Bounding Boxes) y cálculo de confianza por cada fruto detectado.
![alt text](https://github.com/CesarAAR/desktop_app_avocado_detector/blob/main/capturas/image_processed.png "Image Processed")

### 3\. Gestión de Lotes (Sidebar)

Historial de imágenes procesadas durante la sesión, permitiendo el cambio rápido entre resultados sin perder los datos calculados.
![alt text](https://github.com/CesarAAR/desktop_app_avocado_detector/blob/main/capturas/set_imge_processed.png "Set Images Processed")

-----

## 🚀 Características Principales

  * **IA de Última Generación:** Implementación de **YOLO11s** de Ultralytics.
  * **Arquitectura Multihilo:** El procesamiento de imágenes ocurre en segundo plano, manteniendo la interfaz fluida y sin bloqueos.
  * **Métricas Detalladas:** Cálculo automático de:
      * Conteo total de frutos.
      * Confianza promedio del modelo.
      * Valores mínimos y máximos de confianza.
  * **Exportación de Datos:**
      * **CSV:** Reporte estructurado para análisis estadístico.
      * **ZIP:** Paquete de imágenes procesadas (con etiquetas) listo para compartir.

-----

## 🛠️ Instalación

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/CesarAAR/desktop_app_avocado_detector.git
    cd desktop_app_avocado_detector
    ```

2.  **Preparar el entorno virtual:**

    ```bash
    python -m venv venv
    # Activar en Windows
    .\venv\Scripts\activate
    ```

3.  **Instalar dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Modelo:**
    Crea la carpeta `models/` y coloca dentro tu archivo `yolo11s.pt`.

-----

## 💻 Ejecución

Para lanzar la aplicación:

```bash
python main.py
```

-----

## 🛠️ Stack Tecnológico

  * **Lenguaje:** Python 3.x
  * **Visión Artificial:** Ultralytics (YOLO11), OpenCV
  * **Interfaz Gráfica:** Tkinter, ttkbootstrap
  * **Manejo de Imágenes:** Pillow (PIL)

-----

## ✍️ Autor

**[César Alejandro Álvarez Rodríguez]** *Computer Systems Engineer* [LinkedIn](https://www.linkedin.com/in/cesar-alvarez-rodriguez-779446293/) | [GitHub](https://github.com/CesarAAR)
