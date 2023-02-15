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

    ourData = {
        "intents": [

            {
                "tag": "initial_greeting",
                "patterns": ["Hi", "Hello", "Hey", "Hi there", "Hi are you there", "Am I audible ", "Good morning",
                             "Good afternoon", ""],
                "responses": ["Hi, Nice to have you in call. Am I audible to you?"]
            },
            {
                "tag": "greeting_positive_response",
                "patterns": ["Yes, you are audible", "I checked settings you are audible now",
                             "Yes you are", "Yes I can hear you"],
                "responses": ["Amazing.. Can we get started? Are you ready for your interview?",
                              "That's great, Are you ready for an interview?",
                              "Good, we can get started then"]
            },
            {
                "tag": "greeting_negative_response",
                "patterns": ["No", "Nope", "No, you are not", "Nope, you are not",
                             "No you are not audible", "Nope, you are not audible"],
                "responses": ["Oh that's sad, Can you please check your network connection "],
                "previous_context": "initial_greeting"
            },
            {
                "tag": "no_network_issue",
                "patterns": ["Yes, I did check my connection. Its fine ",
                             "Yes, I did check my connection. It is fine ",
                             "I am not facing any network issue",
                             "I do not have any issue with network",
                             "I have strong connection"],
                "responses": ["Oh, glad to hear that. Can you check settings once and let me know if you are audible?"],
                "previous_context": "initial_greeting"
            },
            {
                "tag": "after_greeting|Introduction Starts",
                "patterns": ["Yes, we can get started"],
                "responses": ["Great.. Would you like to introduce yourself?"],
                "previous_context": "greeting_acknowledged"
            },
            {
                "tag": "introduction",
                "patterns": ["My name is *", "I work in ", "I have experience of", "I am "],
                "responses": ["That's great, Let's start with Java section."],
                "previous_context": "intro_complete"
            },
            {
                "tag": "after_introduction",
                "patterns": ["Yes, I would love that", "Yes, we can start with Java"],
                "responses": ["What are 4 OOPS principal in java?"],
                "previous_context": "java_start"
            },
        ]}

    def get_data(self):
        return self.ourData
