#!/usr/bin/python

import PersonOrLocation
import questionBuilder
import pythonptk

class Category:
    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.parentCategory = None
        self.subCategories = []
        self.keywords = []

    def addSubCategory(self, category):        
        self.subCategories.append(category)

    # listOfWords must be a list data-type
    def addKeywords(self, listOfWords):
        for word in listOfWords:
            self.keywords.append(word)

    def __repr__(self):
        return self.categoryName

class Relationship:
    def __init__(self, relationshipName):
        self.relationshipName = relationshipName
        self.keywords = []

    def __repr__(self):
        return self.relationshipName

# Add the Categories into the "database"
happyCategory = Category("Happy")
neutralCategory = Category("Neutral")
depressedCategory = Category("Depressed")

# Add the keywords into the categories
happyCategory.addKeywords(["happy", "glad", "liked", "like", "amazing", "fun", "fantastic", "good"])
neutralCategory.addKeywords(["alright", "okay", "fine"])
depressedCategory.addKeywords(["sad", "suicidal", "depressed", "stressed", "lonely", "gloomy", "bad", "awful", "terrible"])

categories = [neutralCategory, depressedCategory, happyCategory]

persons = []
locations = []
matchingCategories = []

name = input("\n\nHey there, it's bot. Mind identifying yourself? What should I call you?\n\t> ")
name = name.lstrip().rstrip().split(" ")[-1] # Extracts the last word in the sentence
sentence = input("Hello " + name + ", how are ya feeling today?\n\t> ")
                      
### Testing
while True:
    words = sentence.split(" ")
    matchingCategories = []
    
    for word in words:
        for category in categories:
            if word in category.keywords:
                matchingCategories.append(category.categoryName)

    for personName in PersonOrLocation.PersonOrLocation(sentence)['Persons']:
        if personName not in persons:
            persons.append(Person(personName))

    for locationName in PersonOrLocation.PersonOrLocation(sentence)['Locations']:
        if locationName not in persons:
            locations.append(locationName)

    print ("Mood: ", matchingCategories)
    print ("Locations: ", locations)
    print ("Persons: ", persons)
    sentence = input("\n"+questionBuilder.buildQuestion(matchingCategories, locations, persons) + "\n\t> ")
    
