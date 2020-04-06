import random

depressedPerson = [
    "Tell me about name \n >",
    "Have you talked to name ?\n >",
    "Does name know about how you are feeling? \n>"
]

suicidalPerson = [
    "I'm sorry to hear that, but I may not be the best person to talk to. A psychiatrist at (764)-122 584 might help "+
    "you more.\n >",
    "I think it would be better if you talk to an actual psychiatrist face to face. \n >"
]
depressedPlace = [
    "What did you do there? \n >",
    "Why did you go there? \n >",
    "Who did you go with? \n >",
    "What made you you go there in the first place? \n >"
]
depressedGen = [
    "Alright, tell me more. \n >",
    "What makes you feel this way? \n >",
    "What else do you think would help you at this point? \n >",
    "Go on, I'm listening. \n >",
    "I'm here. Tell me more. \n >",
    "Has there been anything else bothering you lately? \n > ",
    "Anything else on your mind? \n >",
    "Why is that? \n >",
    "That's alright, tell me more. \n >"

]
neutralPerson = [
    "How long have you known name ? \n >",
    "Tell me about name \n >",
    "How is name ?\n >",
]
neutralPlace = [
    "What did you do there? \n >",
    "How was name? \n >",
    "Did you like name? \n >",
    "Would you recommend it? name ?\n >",
    "That sounds niceeee, how was it? \n >"
]
neutralGen= [
    ":) Tell me more! \n >",
    "Cool, you been doing anything else lately?\n >",
    "I saw you at the bus stop today, did you go anywhere else?\n >",
    "That's nice to know. Have you been to any new restaurants lately? \n >"
]
general = [
    "Hm, can you tell me more about it? \n >",
    "Go on...\n >",
    "What happened after that? \n >",
    "What a story! Can I get a sequel? \n >"
]
global lastSentence
lastSentence=""

def response(branch, type, name): #type is person or place
    if branch == 'depressed':
        if type == 'person':
            output = depressedPerson[random.randint(0,len(depressedPerson)-1)]
            while (output == getLastSentence().split("!!")[0]):
                output = depressedPerson[random.randint(0,len(depressedPerson)-1)]
            setLastSentence(output,"!!person")
            return output.replace("name",name)
        else:
            output = depressedPlace[random.randint(0, len(depressedPlace)- 1)]
            while (output == getLastSentence().split("!!")[0]):
                output = depressedPlace[random.randint(0, len(depressedPlace) - 1)]
            setLastSentence(output,"!!place")
            return output
    elif branch == 'neutral':
       if type == 'person':
           output = neutralPerson[random.randint(0, len(neutralPerson) - 1)]
           while (output == getLastSentence().split("!!")[0]):
               output = neutralPerson[random.randint(0, len(neutralPerson) - 1)]
           setLastSentence(output,"!!person")
           return output.replace("name",name)
       else:
           output = neutralPlace[random.randint(0, len(neutralPlace) - 1)]
           while (output == getLastSentence().split("!!")[0]):
               output = neutralPlace[random.randint(0, len(neutralPlace) - 1)]
           setLastSentence(output,"!!place")
           return output.replace("name",name)
    else:
        output = general[random.randint(0, len(general) - 1)]
        while (output == getLastSentence().split("!!")[0]):
            output = general[random.randint(0, len(general) - 1)]
        setLastSentence(output,"")
        return output

def genResponse(branch): #generic response
    if branch == 'depressed':
        output = depressedGen[random.randint(0, len(depressedGen) - 1)]
        while (output == getLastSentence()):
            output = depressedGen[random.randint(0, len(depressedGen) - 1)]
        setLastSentence(output,"")
        return output
    elif branch == 'suicidal':
        output = suicidalPerson[random.randint(0, len(suicidalPerson) - 1)]
        while (output == getLastSentence()):
            output = suicidalPerson[random.randint(0, len(suicidalPerson) - 1)]
        setLastSentence(output,"")
        return output
    elif branch == 'neutral':
        output = neutralGen[random.randint(0, len(neutralGen) - 1)]
        while (output == getLastSentence()):
            output = neutralGen[random.randint(0, len(neutralGen) - 1)]
        setLastSentence(output,"")
        return output
    else:
        output = general[random.randint(0, len(general) - 1)]
        while (output == getLastSentence()):
            output = general[random.randint(0, len(general) - 1)]
        setLastSentence(output,"")
        return output

def setLastSentence(sentence,plus):
    global lastSentence
    lastSentence = sentence+plus

def getLastSentence():
    global lastSentence
    return lastSentence