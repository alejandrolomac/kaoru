import time

def greeting():
    hours = time.strftime("%H")
    if int(hours) > 6 and int(hours) < 12:
        greetingtext = "Buenos dias, estoy aqui para cuando necesites algo"
    elif int(hours) >= 12 and int(hours) < 17:
        greetingtext = "Buenas tardes, ¿que tal tu tarde?"
    elif int(hours) >= 17 and int(hours) < 24:
        greetingtext = "Buenas noches, estoy disponible a cualquier hora"
    else:
        greetingtext = "Hola, ¿que haces conectado a esta hora?"

    return greetingtext