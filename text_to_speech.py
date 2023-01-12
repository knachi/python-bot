import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", int(150))  # setting up new voice rate
engine.say("I will speak this text")
engine.runAndWait()
