# import library

import speech_recognition as sr
from datetime import datetime


def speech_to_text():
    # Initialize recognizer class (for recognizing the speech)

    r = sr.Recognizer()
    r.energy_threshold = 4000

    # Reading Microphone as source
    # listening the speech and store in audio_text variable

    with sr.Microphone() as source:
        print("Talk")
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        r.adjust_for_ambient_noise(source)
        audio_text = r.listen(source)
        print("Time over, thanks")
        print("Current Time =", datetime.now().strftime("%H:%M:%S"))
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            # using google speech recognition
            interpreted_text = r.recognize_google(audio_text, show_all= False)
            print("Text: " + interpreted_text)
            return interpreted_text
        except:
            print("Sorry, I did not get that")

        return ''
