import os
from faster_whisper import WhisperModel



# Definición de variables de entrada.
VIDEO = "video.mp4"

# Inicialización del modelo (Configurado para CPU según la consigna).
model = WhisperModel("small", device="cpu", compute_type="int8")

# Proceso de transformación.
print("Iniciando transcripción...")
segments, info = model.transcribe(VIDEO, language="es", beam_size=5)

# Subsistema de salida: Escritura y visualización.
with open("transcripcion.txt", "w", encoding="utf-8") as f:
    for segment in segments:
        texto = f"[{segment.start:.2f}s {segment.end:.2f}s] {segment.text}"
        print(texto)
        f.write(texto + "\n")

print("Proceso finalizado")