# -*- coding: UTF-8 -*-
import pyttsx3
import webbrowser
import speech_recognition as sr
from difflib import SequenceMatcher as SM
import random
import time
import pyaudio
import unidecode

from functions.answers import question_check
from functions.greeting import greeting

r = sr.Recognizer()
microphone = sr.Microphone(device_index = 0)

eng = pyttsx3.init()
eng.setProperty("rate", 140)
eng.setProperty("volume", 1.0)
listVoices = eng.getProperty("voices")
eng.setProperty("voice", listVoices[0].id)

eng.say(greeting())
eng.runAndWait()

print("Escuchando...")

def recognizeMicAudio():
    with microphone as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio, language='es-ES')
    
    return text

text = ""

while text != "silencio":
    text = recognizeMicAudio()
    try:
        text = unidecode.unidecode(text)
        eng.say(question_check(text.lower()))
        eng.runAndWait()
    except:
        eng.say("No entendi bien lo que decias, podrias repetirmelo")
        eng.runAndWait()


#similitud = SM(None, entrada, palabra)
#if similitud > 0.7;
#   en.say(salida)