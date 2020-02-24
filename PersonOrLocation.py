#!/usr/bin/python

# findIndexOfUpperCase is a function that takes a string
# returns the index of the first upper-cased letter; -1 if no upper-case letter is found.
def findIndexOfUpperCase(string):
    for i in range(len(string)):
        if string[i].isUpper():
            return i
    return -1

# findPersonKeywords is a function that takes a list of words (or user's "chat" in this context)
# returns the list of person names in the given list
def findPersonKeywords(words):
    persons = []

    if 'my' in words:
        myIndex = words.index('my')
        persons.append(words[myIndex + 1])
        
    if 'with' in words:
        withIndex = words.index('with') # returns the index of the word 'with' in the list of words

        if words[withIndex + 1].lower() == 'my' and words[withIndex + 2] not in persons:
            persons.append(words[withIndex + 2])
        else:
            personName = words[withIndex + 1]
            personName = personName.capitalize()
            if personName not in persons:
                persons.append(personName)

    if 'to' in words:
        toIndex = words.index('to')

        if (words[toIndex - 1].lower() != 'went') and (words[toIndex - 1].lower() != 'how') and (words[toIndex - 1].lower() != 'go') and (words[toIndex - 1].lower() != 'visit'):
            if words[toIndex + 1].lower() == 'my' and words[toIndex + 2] not in persons:
                persons.append(words[toIndex + 2])
            else:
                personName = words[toIndex + 1]
                personName = personName[0].capitalize()
                if personName not in persons:
                    persons.append(personName)
            
    return persons

# findLocationKeywords is a function that takes a list of words (or user's "chat" in this context)
# returns the list of location names in the given list
def findLocationKeywords(words):
    locations = []

    if 'to' in words:
        toIndex = words.index('to')

        if ((words[toIndex - 1].lower() == 'went') or (words[toIndex - 1].lower() == 'go') or (words[toIndex - 1].lower() == 'goes') or (words[toIndex - 1].lower() == 'visit') or (words[toIndex - 1].lower() == 'visits')) and (words[toIndex - 1].lower() != 'how'):
            locationName = words[toIndex + 1].capitalize()
            if locationName not in locations:
                locations.append(locationName)
            
    return locations

# PersonOrLocation is a function that takes a string (or user's "chat" in this context)
# Returns a dictionary data type with the list of people's names and locations.
def PersonOrLocation(string):
    words = string.lstrip().rstrip().split() # removes unnecessary left/right spaces and returns a list of words in the string
    
    return {'Persons': findPersonKeywords(words), 'Locations': findLocationKeywords(words)}

while True:
    s = input("\n\nEnter sentence to find the list of person names >>> ")
    print(PersonOrLocation(s))