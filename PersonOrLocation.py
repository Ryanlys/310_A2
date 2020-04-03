#!/usr/bin/python

print ("\n\n*****\nPersonOrLocation.py\n\nHold on while I'm loading up NLTK (Natural Language Toolkit) external library for Python...\n\t-> If you see an \"NLTK Downloader\" window and this is your first time using NLTK, click on \"all-nltk\" from the list and \"Download\".\n\t\tOtherwise, just close the window.\n*****\n\n")

# WORD-PROCESSING TOOLKIT
import nltk
nltk.download()

# Person is an object that stores information of a person 
class Person:
    def __init__(self, personName):
        self.personName = personName
        self.isIntroduced = False   # This variable tells the program if the user has introduced the person to the the software
        self.relationshipStatus = None # This variable tells the program the user's relationship status with the person
        self.lengthOfRelationship = None # This variable tells the program the length of relationship between the user and the
        
    def __repr__(self):
        return self.personName

# findPersonKeywords is a function that takes a list of words (or user's "chat" in this context)
# returns the list of person names in the given list
def findPersonKeywords(words):
    persons = []
    personsObject = []

    # Utilizing NLTK library to categorize each word
    words_and_categories = nltk.pos_tag(words)

    for word_and_cat in words_and_categories:
        if word_and_cat[1] == "VBD": # Verb (Action word), in past tense; e.g. took, went, met
            index = words_and_categories.index(word_and_cat)
            if words_and_categories[index + 1][1] != "TO" and words_and_categories[index + 1][1] != "RP" and words_and_categories[index + 1][1] != "RB" and (words_and_categories[index][0].lower() != 'did') and words_and_categories[index + 1][1] != "JJ" and ("VB" not in words_and_categories[index + 1][1]): # Preposition "to" AND particle "give UP", "stressed OUT" AND adverbs AND adjectives
                if words_and_categories[index + 1][1] == "PRP$" and ((words_and_categories[index - 1][0].lower() != 'went') and (words_and_categories[index - 1][0].lower() != 'go') or (words_and_categories[index - 1][0].lower() != 'goes') or (words_and_categories[index - 1][0].lower() != 'visit') or (words_and_categories[index - 1][0].lower() != 'visits') or (words_and_categories[index - 1][0].lower() != 'visited')): # Possessive pronouns; e.g. my, his, hers
                    entity = words_and_categories[index + 2][0]
                    if entity not in persons:
                        persons.append(entity)
                        personsObject.append(Person(entity))

                elif words_and_categories[index + 1][1] != "IN" and words_and_categories[index + 1][1] != "DT": # if word is not a preposition or determiner
                    personName = words_and_categories[index + 1][0]
                    personName = personName[0].upper() + personName[1:]
                    if personName not in persons:
                        persons.append(personName)
                        personsObject.append(Person(personName))

        elif word_and_cat[1] == "NNP" and words_and_categories[words_and_categories.index(word_and_cat) - 1][1] != "IN": # Proper noun; e.g. Ryan, Nat, Eugene, Radhika AND the word before isn't a preposition (the sentence could be "went to KFC on Thursday"; 'Thursday' is a proper noun, 'on' is a preposition)
            if word_and_cat[0] not in persons:
                persons.append(word_and_cat[0])
                personsObject.append(Person(word_and_cat[0]))
                
    if 'with' in words:
        withIndex = words.index('with') # returns the index of the word 'with' in the list of words

        if words[withIndex + 1].lower() == 'my' and words[withIndex + 2] not in persons:
            persons.append(words[withIndex + 2])
            personsObject.append(Person(words[withIndex + 2]))
        else:
            personName = words[withIndex + 1]
            personName = personName.capitalize()
            if personName not in persons:
                persons.append(personName)
                personsObject.append(Person(personName))

    if 'to' in words:
        toIndex = words.index('to')

        if (words[toIndex - 1].lower() != 'went') and (words[toIndex - 1].lower() != 'how') and (words[toIndex - 1].lower() != 'go') and (words[toIndex - 1].lower() != 'visit'):
            if words[toIndex + 1].lower() == 'my' and words[toIndex + 2] not in persons:
                persons.append(words[toIndex + 2])
                personsObject.append(Person(words[toIndex + 2]))
            
    return persons

# findLocationKeywords is a function that takes a list of words (or user's "chat" in this context)
# returns the list of location names in the given list
def findLocationKeywords(words):
    locations = []
    words_and_categories = nltk.pos_tag(words)

    for word_and_cat in words_and_categories: 
        if word_and_cat[1] == "TO":
            index = words_and_categories.index(word_and_cat)

            if ((words_and_categories[index - 1][0].lower() == 'went') or (words_and_categories[index - 1][0].lower() == 'go') or (words_and_categories[index - 1][0].lower() == 'goes') or (words_and_categories[index - 1][0].lower() == 'visit') or (words_and_categories[index - 1][0].lower() == 'visits') or (words_and_categories[index - 1][0].lower() == 'visited')) and (words_and_categories[index - 1][0].lower() != 'how'):
                if words_and_categories[index + 1][1] != "IN" and words_and_categories[index + 1][1] != "DT": # If next word isn't a preposition nor determiner
                    locationName = words_and_categories[index + 1][0]
                    locationName = locationName[0].upper() + locationName[1:]
                    if locationName not in locations:
                        locations.append(locationName)

                elif words_and_categories[index + 1][1] == "DT":
                    locationName = words_and_categories[index + 2][0]
                    locationName = locationName[0].upper() + locationName[1:]
                    if locationName not in locations:
                        locations.append(locationName)
                    
    return locations

# PersonOrLocation is a function that takes a string (or user's "chat" in this context)
# Returns a dictionary data type with the list of Person objects and locations.
def PersonOrLocation(string):
    words = string.lstrip().rstrip().split() # removes unnecessary left/right spaces and returns a list of words in the string
    
    return {'Persons': findPersonKeywords(words), 'Locations': findLocationKeywords(words)}

while True:
    s = input("\n\nEnter sentence to find the list of person names >>> ")
    print(PersonOrLocation(s))
