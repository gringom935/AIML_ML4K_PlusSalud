#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "e7da0140-789f-11ec-b3ad-f98a9cb0eee67e251167-3a2e-4cc1-bd6d-b45e28fd83bf"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    
    if confidence < 75:
        print("No te entiendo bien, pregúntame de otra manera.")
    elif answerclass == "ninio":
        print("niño")
    elif answerclass == "mujer":
        print("mujer")
    elif answerclass == "hombre":
        print("hombre")
    

print("¿Para quién desea realizar su consulta médica?")

while True:
    answer_question()


# In[ ]:




