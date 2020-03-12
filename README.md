# 310_A2
UBCO COSC 310 Assignment 2 Group Repository

Hello! Is a friendly chat bot that is always there to talk to you and listen to your stories 24/7. If you’re sad, it consoles you, if you’re happy, it celebrates with you. It’s the friend that has all the time in the world just to hang out with you whenever you’re lonely.

# How to run the code
Simply download the files, and run main.py with Python.

# Classes
The main class initiates the program by asking the initial question to allow it to loop indefinitely.

The chat class calls itself recursively for each identified person or place keyword in the user sentence.

The PersonOrLocation class takes in the user reply and scans for keywords, then determines and returns a list of people and places the user said.

General class contains all the canned responses, and is responsible to randomly selecting a response based on whether the keyword is a person or a place, or a general response that is used to prompt users for more input.
