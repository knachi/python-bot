import csv
from data_service import DataService


header = ['tag', 'patterns', 'response']

with open('resources/train.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    dataObject = DataService()
    data = dataObject.get_data()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            for response in intent["responses"]:
                tag = intent["tag"]
                row = [tag, pattern, tag + "|" + response]
                # write the data
                writer.writerow(row)



