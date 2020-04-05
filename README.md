# 310_A2
UBCO COSC 310 Assignment 2 Group Repository

Hello! Is a friendly chat bot that is always there to talk to you and listen to your stories 24/7. If you’re sad, it consoles you, if you’re happy, it celebrates with you. It’s the friend that has all the time in the world just to hang out with you whenever you’re lonely.

# How to run the code
Download the files, and run main.py
There may be a 3-5 minute download time for NLTK modules. 
When the program is started, it may seem like it is frozen, but will have functionality after a minute of waiting.

# Classes
The main class initiates the program by asking the initial question to allow it to loop indefinitely.

The chat class calls itself recursively for each identified person or place keyword in the user sentence.

The PersonOrLocation class takes in the user reply and scans for keywords, then determines and returns a list of people and places the user said.

General class contains all the canned responses, and is responsible to randomly selecting a response based on whether the keyword is a person or a place, or a general response that is used to prompt users for more input.

# Additional features implemented
* Sentiment analysis with NLTK
  * Additional phrases will be added into response based on sentiment of user's last input regarding a specific place or person, which allows for more complex and human like responses to different input.
* Synonym recognition with WordNet
* Simple GUI
  * GUI is implemented using PyQt5, with a read-only textedit to store chat log, and a lineedit widget to act as user input box. 

# Members Full Name
- Ryan Lam 54122072
-
-
- 
