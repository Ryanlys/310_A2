import Chat
import nltk
nltk.download('twitter_samples')
nltk.download('stopwords')
nltk.download('wordnet') 
from nltk.corpus import wordnet as wn
#!/usr/bin/python

# findPersonKeywords is a function that takes a list of words (or user's "chat" in this context)
# returns the list of person names in the given list

def getSynonyms(words):
    synonyms = []
    for word in words:
        for s in wn.synsets(word):
            for l in s.lemmas():
                synonyms.append(l.name())
    return set(synonyms)

def findPersonKeywords(words):
    persons = []

    if 'my' in words:
        myIndex = words.index('my')
        if (words[myIndex+1] !=  "roommate" and words[myIndex+1] != "friend" and words[myIndex+1] != "classmate"):
            persons.append(words[myIndex + 1])

    if 'with' in words:
        withIndex = words.index('with') # returns the index of the word 'with' in the list of words

        if words[withIndex + 1].lower() == 'my' and words[withIndex + 2].lower() != 'him' and words[withIndex + 2].lower() != 'her' and words[withIndex + 2].lower() != 'them':
            if words[withIndex+2] not in persons:
                persons.append(words[withIndex+2])


    '''if 'to' in words:
        toIndex = words.index('to')

        if (words[toIndex - 1].lower() != 'went') and (words[toIndex - 1].lower() != 'how') and (words[toIndex - 
        1].lower() != 'go') and (words[toIndex - 1].lower() != 'visit'): if words[toIndex + 1].lower() == 'my' and 
        words[toIndex + 2] not in persons: persons.append(words[toIndex + 2]) else: personName = words[toIndex + 1] 
        personName = personName.capitalize() if personName not in persons: persons.append(personName) '''
            
    return persons

# findLocationKeywords is a function that takes a list of words (or user's "chat" in this context)
# returns the list of location names in the given list
def findLocationKeywords(words):
    locations = []
    synonyms = getSynonyms(["travel"])

    if 'to' in words:
        toIndex = words.index('to')
        if (words[toIndex - 1].lower() in synonyms): 
            if (words[toIndex+1] == "the"):
                locationName = words[toIndex + 2].capitalize()
                if locationName not in locations:
                    locations.append(locationName)
            elif (words[toIndex+1]=="to"):
                if (words[toIndex + 1] == "the"):
                    locationName = words[toIndex + 2].capitalize()
                    if locationName not in locations:
                        locations.append(locationName)
            else:
                locationName = words[toIndex + 1].capitalize()
                if locationName not in locations:
                    locations.append(locationName)
    return locations

def determineBranch(words):
    depressedWordsList = ['stress','stressing','depressed','lonely','sad','unhappy', 'not well', 'unwell', 'miserable', 'upset', 'discouraged','broken-hearted','down', 'glum']
    neutralWords = ['good','alright','okay', 'fine', 'so-so', 'happy', 'content', 'cheery', 'blessed', 'thrilled']

    depressedWords = getSynonyms(depressedWordsList)
    neutralWords = getSynonyms(neutralWordsList)

    if (any(string in words for string in depressedWords)):
        branch = 'depressed'
        return branch
    if (any(string in words for string in neutralWords)):
        branch = 'neutral'
        return branch
    if 'suicidal' in words:
        branch = 'suicidal'
        return branch
    if 'not' in words:
        notIndex = words.index('not')
        if (words[notIndex+1] == "good") or (words[notIndex+1] == "well") or (words[notIndex+1] == "happy"):
            branch = 'depressed'
            return branch

    branch = Chat.getBranch()
    if branch=="":
        branch = "general"

    return branch

# PersonOrLocation is a function that takes a string (or user's "chat" in this context)
# Returns a dictionary data type with the list of people's names and locations.
def PersonOrLocation(string):
    words = string.split() # removes unnecessary left/right spaces and returns a list of words in the string
    return [findPersonKeywords(words),findLocationKeywords(words)]
