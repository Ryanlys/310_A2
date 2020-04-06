# 310_A2
UBCO COSC 310 Assignment 2 Group Repository

Hello! Is a friendly chat bot that is always there to talk to you and listen to your stories 24/7. If you’re sad, it consoles you, if you’re happy, it celebrates with you. It’s the friend that has all the time in the world just to hang out with you whenever you’re lonely.

# How to run the code
* You should probably downloag nltk and PyQT5 (i.e. pip install nltk, pip instal PyQT5).
* Download the files, and run main.py. There may be a 3-5 minute download time for NLTK modules. 
* When the program is started, it may seem like it is frozen, but will have functionality after a minute of waiting.

# Classes
* The main class initiates the program by asking the initial question to allow it to loop indefinitely.
* The chat class calls itself recursively for each identified person or place keyword in the user sentence.
* The PersonOrLocation class takes in the user reply and scans for keywords, then determines and returns a list of people and places the user said.
* General class contains all the canned responses, and is responsible to randomly selecting a response based on whether the keyword is a person or a place, or a general response that is used to prompt users for more input.
* Sentiment class uses Twitter tweets to train the classifier for sentiment analysis. Code is sourced from [here](https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk)

# Additional features implemented
* GUI
 * GUI is implemented using PyQt5, with a read-only textedit to store chat log, and a lineedit widget to act as a user input box.
* Agent can give at least 5 different reasonable responses when user enters something outside of the two topics (3)
 * We have another branch called “general” that handles responses that don’t fit into the two main branches “depressed” and “neutral”
  * "Hm, can you tell me more about it? \n >"
  * "Go on...\n >"
  * "What happened after that? \n >"
  * "Anything else? \n >"
  * "Have you been to any place else lately? \n >"
* Wordnet Synonym Recognition
 * The agent can now recognize not only keywords that we explicitly specified, but synonyms of those keywords, which helps the agent respond to the user better.
  * Ex. Our code uses synonyms of the word “travel” to detect the word “go”:
     Heya, how are you?
     > good
     That’s nice to know. Have you been to any new restaurants lately?
     > I did go to Picnic 
     How was Picnic?
* Sentiment Analysis Tool
 * Additional phrases will be added into response based on the sentiment of the user's last input regarding a specific place or person, which allows for more complex and human-like responses to different inputs.
   How was Picnic?
   > It was great!
   I’ll definitely check it out, have you been to anywhere else lately? 

# Members Full Name and Student ID
* Ryan Lam 54122072
* Nathania Hendradjaja 34089243
* Radhika Sharma 94968294
* Jehezkiel Eugene 96657903
