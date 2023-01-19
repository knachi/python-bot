class DataService:

    def __init__(self):
        pass

    data_old = [
        {
            "question_context": ["c1", "c2"],
            "answer_context": ["a1", "a2"]
        },
        {
            "question_context": ["c1", "c2"],
            "answer_context": ["don't get it", "do not get it"]
        }
    ]

    ourData = {"intents": [
        {"tag": "age",
         "patterns": ["how old are you?"],
         "responses": ["I am 2 years old and my birthday was yesterday"]
         },
        {"tag": "greeting",
         "patterns": ["Hi", "Hello", "Hey"],
         "responses": ["Hi there", "Hello", "Hi :)"],
         },
        {"tag": "goodbye",
         "patterns": ["bye", "later"],
         "responses": ["Bye", "take care"]
         },
        {"tag": "name",
         "patterns": ["what's your name?", "who are you?"],
         "responses": ["I have no name yet," "You can give me one, and I will appreciate it"]
         }

    ]}

    def get_data(self):
        return self.ourData
