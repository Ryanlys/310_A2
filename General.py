import random

depressedPerson = [
    "dperson \n",
    "dperson \n"
]
depressedPlace = [
    "dplace \n",
    "dplace \n"
]
depressedGen = [
    "dgen \n"
]
neutralPerson = [
    "nperson \n",
    "nperson \n"
]
neutralPlace = [
    "nplace \n",
    "nplace \n"
]
neutralGen= [
    "ngen \n"
]
general = [
    "this is general \n",
    "this is gen \n"
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
    elif branch == 'neutral':
        return neutralGen[random.randint(0,len(neutralGen)-1)]
    else:
        return general[random.randint(0,len(general)-1)]