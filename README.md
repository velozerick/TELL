# TELL: Traductor Erick Luis Luis

TELL es una aplicación en Python diseñada para traducir voz en tiempo real mediante una interfaz gráfica intuitiva.

---

## **Tecnologías Usadas**
- **Reconocimiento de Voz**: `SpeechRecognition` para convertir voz en texto.
- **Traducción**: `googletrans` para traducir texto entre idiomas.
- **Texto a Voz**: `pyttsx3` para reproducir las traducciones en audio.
- **Interfaz Gráfica**: `tkinter` para proporcionar una experiencia de usuario amigable.

---

## **Características**
- Traducción de voz en tiempo real a múltiples idiomas.
- Interfaz gráfica fácil de usar con selección de idioma.
- Reproducción de la traducción a través de un sintetizador de voz.

---

## **Cómo Usar**

### **Requisitos Previos**
1. **Python 3.7 o superior** instalado en tu máquina.
2. Instalar las dependencias necesarias desde el archivo `requirements.txt`.

### **Instrucciones**
```bash
# Clona este repositorio en tu máquina local:
git clone https://github.com/velozerick/TELL.git
cd TELL

# Instala las dependencias:
pip install -r requirements.txt

# Ejecuta la aplicación:
python TELL.py

En la interfaz:

    Selecciona un idioma de traducción.
    Haz clic en Iniciar Traducción y habla al micrófono.
    Presiona Escuchar Traducción para reproducir la traducción en audio.

Arquitectura del Software
Componentes Principales

    Interfaz Gráfica: Maneja la interacción con el usuario. Permite seleccionar idioma, grabar voz y reproducir traducciones.

    Reconocimiento de Voz: Convierte el audio capturado en texto usando la API de Google.

    Traducción: Traduce el texto al idioma seleccionado utilizando la biblioteca googletrans.

    Texto a Voz: Reproduce la traducción utilizando el motor pyttsx3.

Diagrama de Flujo

[Inicio] --> [Interfaz Gráfica] --> [Reconocimiento de Voz]
       --> [Traducción] --> [Texto a Voz] --> [Reproducción]

Estructura del Proyecto

TELL/
│
├── TELL.py               # Archivo principal con el código de la aplicación
├── README.md             # Documentación del proyecto
├── requirements.txt      # Lista de dependencias necesarias
└── .gitignore            # Archivos que Git debe ignorar

Contribuciones
Cómo Contribuir

    Haz un fork de este repositorio.

    Clona tu fork:

git clone https://github.com/TuUsuario/TELL.git

Crea una rama nueva para tus cambios:

git checkout -b nombre-rama

Realiza tus cambios y haz un commit:

    git commit -m "Descripción de los cambios"

    Envía un pull request detallando tus modificaciones.

Preguntas Frecuentes (FAQ)
1. ¿Por qué no reconoce mi voz?

    Asegúrate de estar en un ambiente silencioso.
    Configura correctamente el índice de tu micrófono en el código.

2. ¿Cómo puedo agregar más idiomas?

    Edita la lista idioma_seleccionado en el archivo TELL.py.

