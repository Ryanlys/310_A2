import PersonOrLocation, random, General, sys, main

global branch
branch=''

global stack
stack = []

def Chat(words): #type is person or place
    global stack
    global branch
    branch = PersonOrLocation.determineBranch(words.split())
    keywords = PersonOrLocation.PersonOrLocation(words)

    if("bye" in words or "that's it" in words):
        print("It was nice talking to you :)")
        sys.exit()

    if(len(keywords[0]) == 0) and (len(keywords[1]) == 0):
        if len(stack) == 0:
            stack.append(General.genResponse(branch))
        return


    for place in keywords[1]:
        print(place)
        sentence = General.response(branch,'place',place)
        stack.append(sentence)
        print(stack)
    for person in keywords[0]:
        print(person)
        sentence = General.response(branch,'person',person)
        stack.append(sentence)
        print(stack)

def setBranch(b):
    global branch
    branch = b

def getBranch():
    return branch

def popStack():
    return stack.pop()