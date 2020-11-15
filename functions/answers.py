import webbrowser
import speech_recognition as sr
import pyaudio

def question_check(question):
    print("Haz dicho: {}".format(question))
    if "Amazon" in question:
        webbrowser.open('https://www.amazon.es')
    elif "Hola" in question or "hola" in question:
        print("Hola, en que te puedo ayudar")
    elif "quien eres" in question or "quién eres" in question:
        print("Soy Kaoru, una Inteligencia Aritificial")
    elif "kaoru" in question:
        print("Me llamo Kaoru, en honor a una de las artistas favoritas de mi creador, Kaouru Mori")
    else:
        print("no escuche bien")