import random

depressedPerson = [
    "Have you told anyone else about how you're feeling? \n",
    "Have you talked to a therapist about this in the past? \n",
    "Does anyone close to you know about your situation?\n",
    "Have you tried seeking medical attention?\n"
    "Do you think it will help if you seek medical attention?\n"
]

suicidalPerson = [
    "Okay, do you want me to give you the number for a therapist in your area\n",
    "I think it would be better if you talk to an actual psychiatrist face to face\n",
    "okay here are the list of numbers for therapists in your area:\n"
]
depressedPlace = [
    "What did you do there? \n",
    "Why did you go there? \n",
    "Who did you go with? \n",
    "What made you you go there in the first place?"
]
depressedGen = [
    "Alright, tell me more. \n",
    "What makes you feel this way? \n",
    "What else do you think would help you at this point ? \n"


]
neutralPerson = [
    "How long have you known this person? \n",
    "Has this person helped in anyway ? \n"
]
neutralPlace = [
    "What did you do there ? \n",
    "Where else did you go ? \n"
]
neutralGen= [
    "And how is that been helping you? \n"
    "That's good to know. tell me more about how how you've been feeling lately\n?"
    "That's good. have you thought about spending more time outside with friends and family?\n"
    "That's nice to know. Do you feel lonely?"
]
general = [
    "alright, do you want to tell me more about it\n",
    "okay, do you want to elaborate on that ?\n"
]

def response(branch, type): #type is person or place
    if branch == 'depressed':
        if type == 'person':
            return depressedPerson[random.randint(0,len(depressedPerson)-1)]
        else:
            return depressedPlace[random.randint(0, len(depressedPerson)-1)]
    elif branch == 'neutral':
       if type == 'person':
           return neutralPerson[random.randint(0, len(depressedPerson)-1)]
       else:
            return neutralPlace[random.randint(0, len(depressedPerson)-1)]
    else:
        return general[random.randint(0, len(general)-1)]

def genResponse(branch): #generic response
    if branch == 'depressed':
        return depressedGen[random.randint(0,len(depressedGen)-1)]
    elif branch == 'suicidal':
        return suicidalPerson[random.randint(0,len(suicidalPerson)-1)]
    elif branch == 'neutral':
        return neutralGen[random.randint(0,len(neutralGen)-1)]
    else:
        return general[random.randint(0,len(general)-1)]