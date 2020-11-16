# -*- coding: UTF-8 -*-
import webbrowser
import speech_recognition as sr
import pyaudio
import json

with open('functions/answers.json') as file:
    ans = json.load(file)

for dict in ans:
    if dict['quest'].question == "hola":
        print(dict['ans'][1].answer)

def question_check(question):
    print("Haz dicho: {}".format(question))
    if "Amazon" in question:
        webbrowser.open('https://www.amazon.es')
        answer = "Abriendo Amazon"
    elif "Google" in question:
        webbrowser.open('https://www.google.com')
        answer = "Abriendo Google"
    elif "Youtube" in question:
        webbrowser.open('https://www.youtube.com')
        answer = "Abriendo Youtube"
    elif "Vendo en Casa" in question:
        webbrowser.open('https://www.vendoencasa.net')
        answer = "Abriendo Vendo en Casa"
    elif "Hola" in question or "hola" in question:
        answer = "Hola, en que te puedo ayudar"
    elif "quien eres" in question or "quién eres" in question:
        answer = "Soy Kaoru, una Inteligencia Artificial"
    elif "kaoru" in question or "porque que te llamas asi" in question:
        answer = "Me llamo Kaoru, en honor a una de las artistas favoritas de mi creador, Kaouru Mori"
    else:
        answer = "no escuche bien, podrias repetirlo"

    return answer