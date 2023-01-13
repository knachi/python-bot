import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", int(150))  # setting up new voice rate
    engine.say(text)
    engine.runAndWait()
