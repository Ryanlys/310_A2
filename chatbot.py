#!/usr/bin/python

'''
    PLEASE NOTE:
        ONLY RUNS ON PYTHON 3+.
        Python 2's GUI library (tkinter) uses a slightly-different library name and hence will crash upon loading 'tkinter' library, if run on Py2.
'''

import PersonOrLocation
import questionBuilder
import tkinter # GUI library
import tkinter.font
from tkinter import ttk

# Person is an object that stores information of a person 
class Person:
    def __init__(self, personName):
        self.personName = personName
        self.isIntroduced = False   # This variable tells the program if the user has introduced the person to the the software
        self.relationshipStatus = None # This variable tells the program the user's relationship status with the person
        self.lengthOfRelationship = None # This variable tells the program the length of relationship between the user and the
        
    def __repr__(self):
        return self.personName
    
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

# --- GUI stuffs
def GUI_btnReply_onClick():
    pass

mainWindow = tkinter.Tk()

font_verdana12 = tkinter.font.Font(family = "Verdana", size = 12)

scrollbar = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL)
listbox = tkinter.Listbox(mainWindow, yscrollcommand = scrollbar.set)
textInput = tkinter.Entry(mainWindow, font = font_verdana12)
btnReply = tkinter.Button(mainWindow, font = font_verdana12, text = "Reply >", command = GUI_btnReply_onClick)

for i in range(100):
    listbox.insert(tkinter.END, str(i))

listbox.grid(row = 0, columnspan = 1, rowspan = 2, sticky = "nw")
scrollbar.grid(row = 0, column = 1, sticky = "nse")
textInput.grid(row = 1, column = 0, sticky = "sw")
btnReply.grid(row = 1, column = 1, sticky = "se")

scrollbar.config(command = listbox.yview)

mainWindow.columnconfigure(1, weight = 1)
mainWindow.rowconfigure(1, weight = 1)

mainWindow.mainloop()
# ---

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
name = name[0].upper() + name[1:]
sentence = input("Hello " + name + ", how are ya feeling today?\n\t> ")
                      
### Testing
while True:
    words = sentence.split(" ")
    locations = []
    
    for word in words:
        for category in categories:
            if word in category.keywords:
                matchingCategories.append(category.categoryName)

    if len(matchingCategories) > 1:
        matchingCategories = matchingCategories[1:]

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
    
