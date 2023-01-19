import string
import random
import numpy as num
import nltk
from nltk import WordNetLemmatizer
import tensorflow as tensorF  # A multidimensional array of elements is represented by this symbol.
from tensorflow.keras import Sequential  # Sequential groups a linear stack of layers into a tf.keras.Model
from tensorflow.keras.layers import Dense, Dropout

import data_service

lm = WordNetLemmatizer()  # for getting words
# parameter definition
ourNewModel = Sequential()


def process_data(data):
    # lists
    our_classes = []
    new_words = []
    document_x = []
    document_y = []
    # Each intent is tokenized into words and the patterns and their associated tags are added to their respective
    # lists.
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            ournewTkns = nltk.word_tokenize(pattern)  # tokenize the patterns
            new_words.extend(ournewTkns)  # extends the tokens
            document_x.append(pattern)
            document_y.append(intent["tag"])

        if intent["tag"] not in our_classes:  # add unexisting tags to their respective classes
            our_classes.append(intent["tag"])

    new_words = [lm.lemmatize(word.lower()) for word in new_words if
                 word not in string.punctuation]  # set words to lowercase if not in punctuation
    new_words = sorted(set(new_words))  # sorting words
    our_classes = sorted(set(our_classes))  # sorting classes
    return our_classes, new_words, document_x, document_y


def design_nn_model(our_classes, new_words, document_x, document_y):
    trainingData = []  # training list array
    outEmpty = [0] * len(our_classes)
    # bow model
    for idx, doc in enumerate(document_x):
        bagOfwords = []
        text = lm.lemmatize(doc.lower())
        for word in new_words:
            bagOfwords.append(1) if word in text else bagOfwords.append(0)

        outputRow = list(outEmpty)
        outputRow[our_classes.index(document_y[idx])] = 1
        trainingData.append([bagOfwords, outputRow])

    random.shuffle(trainingData)
    trainingData = num.array(trainingData, dtype=object)  # coverting our data into an array afterv shuffling

    x = num.array(list(trainingData[:, 0]))  # first trainig phase
    y = num.array(list(trainingData[:, 1]))  # second training phase
    iShape = (len(x[0]),)
    oShape = len(y[0])

    # In the case of a simple stack of layers, a Sequential model is appropriate

    # Dense function adds an output layer
    ourNewModel.add(Dense(128, input_shape=iShape, activation="relu"))
    # The activation function in a neural network is in charge of converting the node's summed weighted input into
    # activation of the node or output for the input in question
    ourNewModel.add(Dropout(0.5))
    # Dropout is used to enhance visual perception of input neurons
    ourNewModel.add(Dense(64, activation="relu"))
    ourNewModel.add(Dropout(0.3))
    ourNewModel.add(Dense(oShape, activation="softmax"))
    # below is a callable that returns the value to be used with no arguments
    md = tensorF.keras.optimizers.Adam(learning_rate=0.01)
    # Below line improves the numerical stability and pushes the computation of the probability distribution into the
    # categorical crossentropy loss function.
    ourNewModel.compile(loss='categorical_crossentropy',
                        optimizer=md,
                        metrics=["accuracy"])
    # Output the model in summary
    print(ourNewModel.summary())
    # Whilst training your Nural Network, you have the option of making the output verbose or simple.
    ourNewModel.fit(x, y, epochs=200, verbose=1)


def ourText(text):
    newtkns = nltk.word_tokenize(text)
    newtkns = [lm.lemmatize(word) for word in newtkns]
    return newtkns


def wordBag(text, vocab):
    newtkns = ourText(text)
    bagOwords = [0] * len(vocab)
    for w in newtkns:
        for idx, word in enumerate(vocab):
            if word == w:
                bagOwords[idx] = 1
    return num.array(bagOwords)


def Pclass(text, vocab, labels):
    bagOwords = wordBag(text, vocab)
    ourResult = ourNewModel.predict(num.array([bagOwords]))[0]
    newThresh = 0.2
    yp = [[idx, res] for idx, res in enumerate(ourResult) if res > newThresh]

    yp.sort(key=lambda x: x[1], reverse=True)
    newList = []
    for r in yp:
        newList.append(labels[r[0]])
    return newList


def getRes(firstlist, fJson):
    tag = firstlist[0]
    listOfIntents = fJson["intents"]
    for i in listOfIntents:
        if i["tag"] == tag:
            ourResult = random.choice(i["responses"])
            break
    return ourResult


def build_ml_model():
    data_instance = data_service.DataService()
    data = data_instance.get_data()
    our_classes, new_words, document_x, document_y = process_data(data)
    design_nn_model(our_classes, new_words, document_x, document_y)
    return our_classes, new_words


class BuildModel:
    pass
