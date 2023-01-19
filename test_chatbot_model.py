
import build_model
from data_service import DataService


def initiate():
    our_classes, new_words = build_model.build_ml_model()
    while True:
        new_message = input("")
        intents = build_model.Pclass(new_message, new_words, our_classes)
        data = DataService()
        reply = build_model.getRes(intents, data.get_data())
        print(reply)


initiate()
