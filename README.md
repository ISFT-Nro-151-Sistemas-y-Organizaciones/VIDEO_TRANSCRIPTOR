# 🎙️ VideoTranscriptor

Pequeño programa en Python para transcribir a texto el audio de los videos cargados en el mismo, utilizando el motor de inferencia optimizado [Faster Whisper](https://github.com/SYSTRAN/faster-whisper). 

Este proyecto fue desarrollado y documentado como parte de un análisis desde la perspectiva de la **Teoría General de Sistemas (TGS)**, demostrando el control de ambientes y la estructuración de dependencias.

---

## 🚀 Entornos de Ejecución

El sistema está preparado para ser ejecutado en dos entornos aislados: en la nube (Google Colab) y de forma local (Windows).

### ☁️ Opción A: Ejecución en Google Colab (Nube)

Ideal para aprovechar los recursos de hardware (CPU/GPU) delegados en los servidores de Google.

1. **Abrir el entorno:** Ingresá a [Google Colab](https://colab.research.google.com/) y creá un nuevo Notebook (o abrí tu Notebook de trabajo).
2. **Cargar el insumo:** En la barra lateral izquierda (ícono de la carpeta `Archivos`), subí el archivo multimedia que vas a procesar, nombrándolo obligatoriamente como `video.mp4`.
3. **Instalar dependencias:** En la primera celda de código, instalá la biblioteca aislando el comando del sistema operativo:
   `!pip install faster-whisper`
4. **Ejecutar el sistema principal:** En una segunda celda, pegá y ejecutá el script `VideoTranscriptor.py`.
5. **Recolectar salidas:** Una vez que la consola imprima `"Proceso finalizado"`, actualizá el panel de archivos y descargá el archivo generado `transcripcion.txt`.

---

### 💻 Opción B: Ejecución Local (Windows)

Despliegue estructural aislando dependencias para evitar conflictos sistémicos (Entropía) en la instalación global de Python.

**Requisitos previos:**
* [Python](https://www.python.org/downloads/) instalado en tu sistema.
* Un editor de código como [Visual Studio Code](https://code.visualstudio.com/).

**Pasos de despliegue:**
1. **Posicionamiento:** Abrí tu terminal y navegá al directorio raíz del proyecto:
   `cd "ruta\a\tu\carpeta\VideoTranscriptor"`
2. **Aislamiento del entorno:** Creá un entorno virtual encapsulado:
   `python -m venv .venv`
3. **Activación:** Activá el subsistema para que la terminal utilice las librerías locales:
   `.\.venv\Scripts\activate`
   *(Deberías ver el prefijo `(.venv)` en la línea de comandos).*
4. **Instalación de dependencias (Neguentropía):**
   `pip install faster-whisper`
5. **Ejecución:** Asegurate de tener el archivo `video.mp4` en la misma raíz de la carpeta y ejecutá el proceso de transformación:
   `python VideoTranscriptor.py`

---

## 📂 Estructura de Archivos Esperada

Para que el script opere correctamente y mantenga su estado de homeostasis, el directorio local debe lucir así:

> VideoTranscriptor/
> │
> ├── .venv/                   # Entorno virtual aislado (No se sube a GitHub)
> ├── VideoTranscriptor.py     # Código fuente principal
> ├── video.mp4                # Archivo de entrada (Input)
> └── transcripcion.txt        # Archivo generado (Output)

---
*Desarrollado para la materia Sistemas y Organizaciones.*