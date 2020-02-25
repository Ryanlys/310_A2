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
neutralCategory = Category("Neutral")
depressedCategory = Category("Depressed")

# Add the keywords into the categories
neutralCategory.addKeywords(["alright", "okay", "fine", "happy", "glad", "like", "liked", "amazing", "fun", "good"])
depressedCategory.addKeywords(["sad", "depressed", "stressed", "lonely", "gloomy", "bad", "awful", "terrible"])

categories = [neutralCategory, depressedCategory]

### Testing
while True:
    sentence = input("\n\nEnter a sentence to find out which category/categories it falls in >>> ").split(" ")
    matchingCategories = []
    
    for word in sentence:
        for category in categories:
            if word in category.keywords:
                matchingCategories.append(category)

    print(matchingCategories)
