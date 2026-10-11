import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
from translate import Translator
import random
# Diccionario de palabras en español
words_by_level = {
    "facil": ["gato", "perro", "manzana", "leche", "sol"],
    "medio": ["banano", "escuela", "amigo", "ventana", "amarillo"],
    "dificil": ["tecnologia", "universidad", "informacion", "pronunciacion", "imaginacion"]
}

# Traducciones correctas
translations = {
    "gato": "cat",
    "perro": "dog",
    "manzana": "apple",
    "leche": "milk",
    "sol": "sun",
    "banano": "banana",
    "escuela": "school",
    "amigo": "friend",
    "ventana": "window",
    "amarillo": "yellow",
    "tecnologia": "technology",
    "universidad": "university",
    "informacion": "information",
    "pronunciacion": "pronunciation",
    "imaginacion": "imagination"
}
# Dificultad 
dificultad=input("Elige una difcultad: ")
if dificultad == "facil":
    print(words_by_level["facil"])
if dificultad == "medio":
    print(words_by_level["medio"])
if dificultad == "dificil":
    print(words_by_level["dificil"])
else:
    print("Elige entre facil, medio y dificil")
    
    palabra = random.choice(words_by_level[dificultad])
    print("Tu palabra en español es :", palabra)








# Configuraciónen
duration = 5
sample_rate = 44100

# Grabar

print("Habla ahora...")

recording = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)

sd.wait()

# Guardar audio
wav.write("output.wav", sample_rate, recording)

print("Grabación completa, ahora reconociendo...")

# Reconocimiento de voz
recognizer = sr.Recognizer()

with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)


try:
    text = recognizer.recognize_google(
        audio,
        language="en-US"
    )

    print("Dijiste:", text)
    puntos = 0
    incorrectos = 0
    max_incorrectos=3
    correcta = translations[palabra]

    if text.lower().strip() == correcta:
        print("¡Es correcto! Tienes un punto.")
        puntos += 1
    else:
        print("Incorrecto. La respuesta era:", correcta)
        if incorrectos >= max_incorrectos:
            print("te equivocaste mas de 3 veces")
    
    



except sr.UnknownValueError:
    print("No se pudo reconocer el habla.")

except sr.RequestError as e:
    print(f"Error del servicio de reconocimiento: {e}")

except Exception as e:
    print(f"Error al traducir: {e}")
