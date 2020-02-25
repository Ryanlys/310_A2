#!/usr/bin/python

import random

def buildQuestion(matchingCategories, location=None, persons=None):
    reply = ""

    # The following "understanding words" is the little intro to a chat/question the program gives out.
    neutralUnderstandingWords = ["", "Ah, I see.", "Okay.", "I understand.", "Alright."]
    sadUnderstandingWords = ["Oh no!", "Aiyoo...", "I feel terrible for you.", "That's not a good thing to hear."]
    happyUnderstandingWords = ["That's great to hear!", "I'm glad to hear that!", "Ohh that's nice to know.", "That's good."]

    askFeelingQuestions = ["How did you feel about", "How was", "Did you enjoy"]
    askLocationQuestions = ["Where did you go to", "Did you go anywhere interesting"]
    askPersonQuestions = ["Could you tell me more about", "Who's", "Ya mind introducing me to", "How would you describe"]
    askMoreFeelingQuestions = ["Tell me more about why you're feeling", "Could you be more specific by feeling"]
    askGeneralQuestions = ["Is there anything else you would want to talk about?"]
                               
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
                        relationshipStatus = input("\n" + reply + "\n\t> ").lstrip().rstrip().split()

                        while 'my' not in relationshipStatus:
                            reply = random.choice(askPersonQuestions) + (" %s again?" % person.personName)
                            relationshipStatus = input("\nUmm sorry, I don't understand your reply just now. " + reply + "\n\t> ").lstrip().rstrip().split()
                            
                        if 'my' in relationshipStatus:
                            relationshipStatus = " ".join(relationshipStatus[(relationshipStatus.index('my') + 1):]) # Joins all words after 'my'
                            person.isIntroduced = True
                            person.relationshipStatus = relationshipStatus
                            reply = random.choice(neutralUnderstandingWords) + ".. Your " + relationshipStatus + ". "
     
                    if person.lengthOfRelationship is None:
                        lengthOfRelationship = input(reply + "How long have you known %s for?\n\t> " % person.personName)
                        person.lengthOfRelationship = lengthOfRelationship
                        reply = random.choice(neutralUnderstandingWords) + random.choice(askMoreFeelingQuestions)
                        
                    else:
                        reply += " " + random.choice(askGeneralQuestions)
                               
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
