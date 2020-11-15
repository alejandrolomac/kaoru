import webbrowser
import speech_recognition as sr
import pyaudio

from functions.answers import question_check

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Hola, soy Kaoru")
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=3)
        text = r.recognize_google(audio, language='es')
        if text:
            try:
                question_check(text)
            except:
                print('No te he entendido')