# Importar las bibliotecas necesarias
import tkinter as tk  # Para crear la interfaz gráfica
from tkinter import ttk  # Para usar widgets avanzados de la interfaz
import speech_recognition as sr  # Para reconocimiento de voz
from googletrans import Translator  # Para traducir texto
import pyttsx3  # Para convertir texto a voz
import threading  # Para ejecutar tareas en segundo plano

# Inicializar variables globales
grabando = False  # Variable para controlar si el micrófono está grabando
traduccion_actual = ""  # Variable para almacenar la traducción actual
engine = pyttsx3.init()  # Inicializar el motor de texto a voz para que esté disponible en todo el programa

# Definir función para iniciar la traducción de voz
def iniciar_traduccion():
    """
    Iniciar el proceso de grabación y traducción de voz.
    Actualizar el estado de la interfaz y ejecutar la grabación en un hilo separado
    para evitar que la interfaz gráfica se congele mientras se graba.
    """
    global grabando
    grabando = True  # Activar grabación
    estado.set("Grabando durante 10 segundos...")  # Actualizar mensaje de estado en la interfaz
    root.update_idletasks()  # Forzar actualización de la interfaz gráfica
    threading.Thread(target=procesar_audio).start()  # Ejecutar el procesamiento de audio en segundo plano

# Definir función para procesar el audio grabado
def procesar_audio():
    """
    Escuchar audio del micrófono, convertirlo a texto y traducirlo al idioma seleccionado.
    Manejar posibles errores como falta de audio o problemas con la conexión al servicio de reconocimiento.
    """
    global grabando, traduccion_actual  # Usar las variables globales para almacenar el estado y la traducción
    recognizer = sr.Recognizer()  # Inicializar el reconocedor de voz
    translator = Translator()  # Inicializar el traductor de texto

    # Obtener el idioma de destino seleccionado en la interfaz
    idioma_destino = idioma_seleccionado.get()

    try:
        # Configurar el micrófono con el índice específico
        with sr.Microphone(device_index=1) as source:
            # Ajustar el micrófono para el ruido ambiental
            recognizer.adjust_for_ambient_noise(source, duration=1)
            estado.set("Escuchando...")  # Actualizar mensaje de estado en la interfaz
            root.update_idletasks()  # Refrescar la interfaz gráfica

            # Escuchar el audio del micrófono durante 10 segundos
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            estado.set("Procesando audio...")  # Actualizar mensaje de estado en la interfaz
            root.update_idletasks()  # Refrescar la interfaz gráfica

            # Convertir el audio a texto utilizando la API de Google
            texto = recognizer.recognize_google(audio, language="es-ES")

            # Traducir el texto al idioma seleccionado
            traduccion_actual = translator.translate(texto, src="es", dest=idioma_destino).text

            # Mostrar los resultados en la interfaz gráfica
            texto_original.set(f"Texto original: {texto}")
            texto_traducido.set(f"Traducción: {traduccion_actual}")
            estado.set("Traducción completada.")  # Actualizar estado
    except sr.UnknownValueError:
        # Manejar error cuando no se puede entender el audio
        estado.set("No se pudo entender el audio.")
    except sr.RequestError as e:
        # Manejar error cuando hay un problema con el servicio de reconocimiento
        estado.set(f"Error con el servicio de reconocimiento: {e}")
    except Exception as e:
        # Manejar cualquier otro error inesperado
        estado.set(f"Error inesperado: {e}")
    finally:
        # Asegurarse de que la grabación se detenga independientemente de lo que ocurra
        grabando = False

# Definir función para reproducir la traducción en voz
def escuchar_traduccion():
    """
    Convertir la traducción actual en voz y reproducirla utilizando el motor de texto a voz.
    Mostrar un mensaje en caso de que no haya una traducción disponible.
    """
    global traduccion_actual, engine
    if traduccion_actual:
        try:
            # Cambiar el estado a "Reproduciendo traducción"
            estado.set("Reproduciendo traducción...")
            root.update_idletasks()  # Refrescar la interfaz gráfica

            # Usar el motor de texto a voz para reproducir la traducción
            engine.say(traduccion_actual)
            engine.runAndWait()  # Esperar a que termine la reproducción

            # Actualizar el estado cuando termine la reproducción
            estado.set("Reproducción completada.")
        except Exception as e:
            # Mostrar mensaje de error si algo falla durante la reproducción
            estado.set(f"Error al reproducir traducción: {e}")
    else:
        # Mostrar mensaje si no hay traducción disponible
        estado.set("No hay traducción disponible para reproducir.")

# Crear ventana principal de la aplicación
root = tk.Tk()
root.title("TELL")  # Establecer el título de la ventana TELL = TRADUCTOR ERICK LUIS LUIS

# Configurar el tamaño y el diseño de la ventana
root.geometry("500x500")  # Establecer el tamaño de la ventana
root.configure(bg="#f5f5f5")  # Establecer el color de fondo de la ventana

# Crear variables para los textos mostrados en la interfaz
estado = tk.StringVar(value="Presiona 'Iniciar' para comenzar.")  # Mensaje de estado inicial
texto_original = tk.StringVar(value="Texto original: ")  # Variable para el texto original
texto_traducido = tk.StringVar(value="Traducción: ")  # Variable para la traducción

# Crear etiqueta para el título
titulo = tk.Label(root, text="TELL", font=("Helvetica", 16), bg="#f5f5f5")
titulo.pack(pady=10)  # Agregar espacio alrededor del título

# Crear un desplegable para seleccionar el idioma de traducción
idioma_label = tk.Label(root, text="Selecciona el idioma de traducción:", bg="#f5f5f5")
idioma_label.pack(pady=5)  # Agregar espacio
idioma_seleccionado = ttk.Combobox(root, values=["en", "fr", "de", "it"], state="readonly", font=("Helvetica", 12))
idioma_seleccionado.set("en")  # Establecer inglés como idioma predeterminado
idioma_seleccionado.pack(pady=5)

# Crear un marco para los botones
botones_frame = tk.Frame(root, bg="#f5f5f5")
botones_frame.pack(pady=10)

# Crear botón para iniciar la traducción
iniciar_btn = tk.Button(botones_frame, text="Iniciar Traducción", command=iniciar_traduccion, bg="#4caf50", fg="white", font=("Helvetica", 12))
iniciar_btn.pack(side=tk.LEFT, padx=10)

# Crear botón para escuchar la traducción
escuchar_btn = tk.Button(botones_frame, text="Escuchar Traducción", command=escuchar_traduccion, bg="#2196F3", fg="white", font=("Helvetica", 12))
escuchar_btn.pack(side=tk.LEFT, padx=10)

# Crear etiquetas para mostrar los resultados de la traducción
resultado_original = tk.Label(root, textvariable=texto_original, wraplength=450, bg="#f5f5f5", font=("Helvetica", 12))
resultado_original.pack(pady=10)  # Agregar espacio alrededor
resultado_traducido = tk.Label(root, textvariable=texto_traducido, wraplength=450, bg="#f5f5f5", font=("Helvetica", 12))
resultado_traducido.pack(pady=10)  # Agregar espacio alrededor

# Crear etiqueta para mostrar el estado
estado_label = tk.Label(root, textvariable=estado, wraplength=450, fg="blue", bg="#f5f5f5", font=("Helvetica", 10))
estado_label.pack(pady=20)  # Agregar espacio alrededor

# Iniciar el bucle principal de la aplicación
root.mainloop()
