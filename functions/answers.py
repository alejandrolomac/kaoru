# -*- coding: UTF-8 -*-
import webbrowser
import speech_recognition as sr
import pyaudio
import json
import random

with open('functions/answers.json') as file:
    ans = json.load(file)

def question_check(question):
    print("Haz dicho: {}".format(question))
    for i in ans['answer']:
        if question in i['quest']:
            ansnum = random.randrange(0, len(i['ans']))
            answer = i['ans'][ansnum]
            break
        else:
            print("entramos al ciclo pero no encontre nada")

    if "amazon" in question:
        webbrowser.open('https://www.amazon.es')
        answer = "Abriendo Amazon"
    elif "google" in question:
        webbrowser.open('https://www.google.com')
        answer = "Abriendo Google"
    elif "youtube" in question:
        webbrowser.open('https://www.youtube.com')
        answer = "Abriendo Youtube"
    elif "terracron" in question:
        webbrowser.open('https://www.terracron.net')
        answer = "Abriendo Terracron"

    return answer