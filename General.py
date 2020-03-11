import random

depressedPerson = [
    "Tell me about name \n",
    "Have you talked to name \n",
    "Does name know about how you are feeling? \n"
]

suicidalPerson = [
    "I'm sorry to hear that, but I may not be the best person to talk to. A psychiatrist at (764)-122 584 might help "+
    "you more.\n",
    "I think it would be better if you talk to an actual psychiatrist face to face. \n"
]
depressedPlace = [
    "What did you do there? \n",
    "Why did you go there? \n",
    "Who did you go with? \n",
    "What made you you go there in the first place? \n"
]
depressedGen = [
    "Alright, tell me more. \n",
    "What makes you feel this way? \n",
    "What else do you think would help you at this point? \n",
    "Go on, I'm listening. \n",
    "I'm here. Tell me more. \n",
    "Has there been anything else bothering you lately? \n",
    "Anything else on your mind? \n",
    "Why is that? \n",
    "That's alright, tell me more. \n"

]
neutralPerson = [
    "How long have you known name ? \n",
    "Tell me about name \n",
    "How is name ?\n",
]
neutralPlace = [
    "What did you do there? \n",
    "How was it? \n",
    "Did you like it? \n",
    "Would you recommend it?\n",
    "That sounds niceeee \n"
]
neutralGen= [
    ":) Tell me more! \n",
    "That's good to know. tell me more about how how you've been feeling lately?\n",
    "That's good. have you thought about spending more time outside with friends and family?\n",
    "That's nice to know. Do you feel lonely? \n"
]
general = [
    "Tell me more about it\n",
    "What else?\n"
]
global lastSentence
lastSentence=""

def response(branch, type, name): #type is person or place
    if branch == 'depressed':
        if type == 'person':
            output = depressedPerson[random.randint(0,len(depressedPerson)-1)]
            while (output == getLastSentence()):
                output = depressedPerson[random.randint(0,len(depressedPerson)-1)]
            setLastSentence(output)
            return output.replace("name",name)
        else:
            output = depressedPlace[random.randint(0, len(depressedPlace)- 1)]
            while (output == getLastSentence()):
                output = depressedPlace[random.randint(0, len(depressedPlace) - 1)]
            setLastSentence(output)
            return output
    elif branch == 'neutral':
       if type == 'person':
           output = neutralPerson[random.randint(0, len(neutralPerson) - 1)]
           while (output == getLastSentence()):
               output = neutralPerson[random.randint(0, len(neutralPerson) - 1)]
           setLastSentence(output)
           return output.replace("name",name)
       else:
           output = neutralPlace[random.randint(0, len(neutralPlace) - 1)]
           while (output == getLastSentence()):
               output = neutralPlace[random.randint(0, len(neutralPlace) - 1)]
           setLastSentence(output)
           return output
    else:
        output = general[random.randint(0, len(general) - 1)]
        while (output == getLastSentence()):
            output = general[random.randint(0, len(general) - 1)]
        setLastSentence(output)
        return output

def genResponse(branch): #generic response
    if branch == 'depressed':
        output = depressedGen[random.randint(0, len(depressedGen) - 1)]
        while (output == getLastSentence()):
            output = depressedGen[random.randint(0, len(depressedGen) - 1)]
        setLastSentence(output)
        return output
    elif branch == 'suicidal':
        output = suicidalPerson[random.randint(0, len(suicidalPerson) - 1)]
        while (output == getLastSentence()):
            output = suicidalPerson[random.randint(0, len(suicidalPerson) - 1)]
        setLastSentence(output)
        return output
    elif branch == 'neutral':
        output = neutralGen[random.randint(0, len(neutralGen) - 1)]
        while (output == getLastSentence()):
            output = neutralGen[random.randint(0, len(neutralGen) - 1)]
        setLastSentence(output)
        return output
    else:
        output = general[random.randint(0, len(general) - 1)]
        while (output == getLastSentence()):
            output = general[random.randint(0, len(general) - 1)]
        setLastSentence(output)
        return output

def setLastSentence(sentence):
    global lastSentence
    lastSentence = sentence

def getLastSentence():
    return lastSentence