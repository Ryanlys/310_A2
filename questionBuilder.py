#!/usr/bin/python

import random

def buildQuestion(matchingCategories, location=None, persons=None):
    reply = ""

    # The following "understanding words" is the little intro to a chat/question the program gives out.
    neutralUnderstandingWords = ["", "Ah, I see.", "Okay.", "I understand.", "Alright."]
    sadUnderstandingWords = ["Oh no!", "I feel terrible for you.", "That's not a good thing to hear."]
    happyUnderstandingWords = ["That's great to hear!", "I'm glad to hear that!", "Ohh that's nice to know.", "That's good."]

    askFeelingQuestions = ["How did you feel about", "How was", "Did you enjoy"]
    askLocationQuestions = ["Where did you go to", "Did you go anywhere interesting"]
    askPersonQuestions = ["Could you tell me more about", "Who's", "Ya mind introducing me to", "How would you describe"]
    askMoreFeelingQuestions = ["Tell me more about why you're feeling"]
                               
    if len(matchingCategories) == 0:
        if len(location) == 0:
            if len(persons) != 0:
                reply += " with "
                for person in persons:
                    reply += person.personName
            else:
                reply = random.choice(askLocationQuestions)
                           
            reply += "?"
            return reply
                           
        else:
            if len(persons) == 0:
                reply += random.choice(neutralUnderstandingWords) + " Who did you go to %s with?" % location[0]
            else:
                for person in persons:
                    if not person.isIntroduced:
                        reply = random.choice(askPersonQuestions)
                        reply += " %s?" % person.personName
                        return reply
                    elif not person.lengthOfRelationship:
                        reply = "How long have you known %s for?" % person.personName
                               
            return reply
    else:
        if matchingCategories[0] == "Depressed":
            reply = random.choice(sadUnderstandingWords)
        elif matchingCategories[0] == "Neutral":
            reply = random.choice(neutralUnderstandingWords)
        elif matchingCategories[0] == "Happy":
            reply = random.choice(happyUnderstandingWords)

        reply += " " + random.choice(askMoreFeelingQuestions) + " " + matchingCategories[0].lower() + "."
        return reply
