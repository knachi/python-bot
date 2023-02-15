import build_model
from data_service import DataService


def transform_and_get_input_message(new_message, previous_context):
    affermative_responses = ["Yes", "yes sure", "Yes definitely", "sure", "yes"]
    if new_message.lower() in (map(str.lower, affermative_responses)):
        if previous_context and previous_context == 'after_introduction':
            return 'Yes, we can start with Java'
        elif previous_context and previous_context == 'after_greeting|Introduction Starts':
            return 'Yes, we can get started'
        elif previous_context and previous_context == 'greeting_positive_response':
            return 'Yes, we can get started'

    return new_message


def initiate():
    our_classes, new_words = build_model.build_ml_model()
    previous_context = ''
    previous_question = ''
    previous_answer = ''
    while True:
        new_message = input("")
        transformed_message = transform_and_get_input_message(new_message, previous_context)
        intents = build_model.Pclass(transformed_message, new_words, our_classes)
        data = DataService()
        reply, tag = build_model.getRes(intents, data.get_data())
        previous_context = tag
        previous_question = reply
        previous_answer = new_message
        print(reply)


initiate()
