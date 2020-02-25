#!/usr/bin/python

import PersonOrLocation

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

# Add the Categories into the "database"
happyCategory = Category("Happy")
neutralCategory = Category("Neutral")
depressedCategory = Category("Depressed")

# Add the keywords into the categories
happyCategory.addKeywords(["happy", "glad", "liked", "like", "amazing", "fun", "fantastic", "good"])
neutralCategory.addKeywords(["alright", "okay", "fine"])
depressedCategory.addKeywords(["sad", "suicidal", "depressed", "stressed", "lonely", "gloomy", "bad", "awful", "terrible"])

categories = [neutralCategory, depressedCategory, unknownMoodCategory, happyCategory]

### Testing
while True:
    sentence = input("\n\nEnter a sentence to find out which category/categories it falls in >>> ").lower().split(" ")
    matchingCategories = []
    
    for word in sentence:
        for category in categories:
            if word in category.keywords:
                matchingCategories.append(category)

    print(matchingCategories)
