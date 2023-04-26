import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

with open("intents.json") as file:
    data = json.load(file)

# load trained model
model = keras.models.load_model('chat_model')

# load tokenizer object
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load label encoder object
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)
    

# parameters
max_len = 20

class Chatbot:

    def __init__(self):
        self.state = 'initialise'


    def getResult(self, input):
        inp = input
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                                truncating='post', maxlen=max_len))
        return result

    def getTag(self, result):
        res = result
        tag = lbl_encoder.inverse_transform([np.argmax(res)])
        return tag

    def cleanupTag(self, tag):
        inputTag = tag
        outputTag = ""
        for char in inputTag:
            if char.isalnum():
                outputTag += char
        return outputTag


    # def diagnose(input):
        inp = input
        result = getResult(inp)
        tag = getTag(result)
        for i in data['intents']:
            if i['tag'] == tag:
                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(i['responses']))
                
            else:
                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , 'I am not sure i understood what the problem is, could you re-state it?')

    def chat(self):
        while True:
            print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
            inp = input()

            if inp.lower() == "quit":
                break

            result = self.getResult(inp)
            tag = self.getTag(result)

            # cleanup the tag into alphanumeric string.
            alNumTagSTR = self.cleanupTag(tag)
            print(alNumTagSTR)

            # if alNumTagSTR[:4] == 'diag':
            #     print('made it')
            #     diagnose(inp)


            for i in data['intents']:
                if i['tag'] == tag:
                    print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(i['responses']))
                    self.state = alNumTagSTR
                    print(self.state)
                    break


            # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))

chatbot = Chatbot()
print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
chatbot.chat()






