#!/usr/bin/python

import random

def removePersonFromList(person, persons):
    index = persons.index(person)
    persons.pop(index)
    return persons

def buildQuestion(matchingCategories, location=None, persons=None):
    reply = ""

    # The following "understanding words" is the little intro to a chat/question the program gives out.
    neutralUnderstandingWords = ["", "Ah, I see.", "Okay.", "I understand.", "Alright."]
    sadUnderstandingWords = ["Oh no!", "Aiyoo...", "I feel terrible for you.", "That's not a good thing to hear."]
    happyUnderstandingWords = ["That's great to hear!", "I'm glad to hear that!", "Ohh that's nice to know.", "That's good."]

    askLocationQuestions = ["Where did you go to today?", "Did you do anywhere interesting?"]
    askMoreLocationQuestions = ["What made you you go to %s in the first place?", "Why did you go to the %s?", "How was %s?", "Did you enjoy going to %s?"]
    askPersonQuestions = ["Could you tell me more about %s?", "Who's %s?", "Would you mind telling me a bit about %s?", "Who is %s to you?"]
    askMoreFeelingQuestions = ["Tell me more why you're feeling %s right now.", "Could you be more specific by feeling %s?", "Since you're feeling %s, have you been doing anything else lately?"]
    askGeneralQuestions = ["Is there anything else you would want to talk about?"]
    askKeepGoing = ["Tell me more", "What makes you feel this way?", "What else do you think would help you at this point?", "Go on, I'm listening.", "I'm here. Tell me more.", "Has there been anything else bothering you lately?"]
                               
    if len(matchingCategories) == 0:
        if location is None or len(location) == 0:
            if persons is None or len(persons) != 0:
                for person in persons:
                    if not person.isIntroduced:
                        reply = random.choice(askPersonQuestions) % person.personName
                        relationshipStatus = input("\n" + reply + "\n\t> ").lstrip().rstrip().split()

                        while 'my' not in relationshipStatus:
                            reply = random.choice(askPersonQuestions) + (" %s again?" % person.personName)
                            relationshipStatus = input("\nUmm sorry, I don't understand your reply just now. " + reply + "\n\t> ").lstrip().rstrip().split()
                            return reply
                            
                        if 'my' in relationshipStatus:
                            relationshipStatus = " ".join(relationshipStatus[(relationshipStatus.index('my') + 1):]) # Joins all words after 'my'
                            person.isIntroduced = True
                            person.relationshipStatus = relationshipStatus
                            persons = removePersonFromList(person, persons)
                            reply = "Your " + relationshipStatus + ". " + random.choice(neutralUnderstandingWords)
     
                    if person.lengthOfRelationship is None:
                        lengthOfRelationship = input(reply + "How long have you known %s for?\n\t> " % person.personName)
                        person.lengthOfRelationship = lengthOfRelationship
                        reply = random.choice(neutralUnderstandingWords) + random.choice(askMoreFeelingQuestions)
                        return reply
                        
                    else:
                        reply += " " + random.choice(askGeneralQuestions)
                        return reply

                reply = random.choice(neutralUnderstandingWords) + " " + random.choice(askKeepGoing)
                return reply
            else:
                reply = random.choice(askLocationQuestions)           
            return reply
                           
        else:
            if len(persons) == 0:
                input(("\n" + random.choice(askMoreLocationQuestions) + "\n\t>") % location[0])
                reply += random.choice(neutralUnderstandingWords) + " Who did you go to %s with?" % location[0]
                return reply
            else:
                input(("\n" + random.choice(askMoreLocationQuestions) + "\n\t> ") % location[0])
                for person in persons:
                    if not person.isIntroduced:
                        reply = random.choice(askPersonQuestions) % person.personName
                        relationshipStatus = input("\n" + reply + "\n\t> ").lstrip().rstrip().split()

                        while 'my' not in relationshipStatus:
                            reply = random.choice(askPersonQuestions) + (" %s again?" % person.personName)
                            relationshipStatus = input("\nUmm sorry, I don't understand your reply just now. " + reply + "\n\t> ").lstrip().rstrip().split()
                            return reply
                            
                        if 'my' in relationshipStatus:
                            relationshipStatus = " ".join(relationshipStatus[(relationshipStatus.index('my') + 1):]) # Joins all words after 'my'
                            person.isIntroduced = True
                            persons = removePersonFromList(person, persons)
                            person.relationshipStatus = relationshipStatus
                            reply = "Your " + relationshipStatus + ". " + random.choice(neutralUnderstandingWords)
     
                    if person.lengthOfRelationship is None:
                        lengthOfRelationship = input(reply + "How long have you known %s for?\n\t> " % person.personName)
                        person.lengthOfRelationship = lengthOfRelationship
                        reply = random.choice(neutralUnderstandingWords) + random.choice(askMoreFeelingQuestions)
                        return reply
                        
                    else:
                        reply += " " + random.choice(askGeneralQuestions)
                        return reply

                reply = random.choice(neutralUnderstandingWords) + " " + random.choice(askKeepGoing)
                return reply
    else:
        if len(location) != 0:
            return (("\n" + random.choice(askMoreLocationQuestions)) % location[0])
        else:
            if len(persons) != 0:
                for person in persons:
                    if not person.isIntroduced:
                        reply = ("By the way, " + random.choice(askPersonQuestions)) % person.personName
                        relationshipStatus = input("\n" + reply + "\n\t> ").lstrip().rstrip().split()

                        while 'my' not in relationshipStatus:
                            reply = random.choice(askPersonQuestions) + (" %s again?" % person.personName)
                            relationshipStatus = input("\nUmm sorry, I don't understand your reply just now. " + reply + "\n\t> ").lstrip().rstrip().split()
                            return reply
                            
                        if 'my' in relationshipStatus:
                            relationshipStatus = " ".join(relationshipStatus[(relationshipStatus.index('my') + 1):]) # Joins all words after 'my'
                            person.isIntroduced = True
                            persons = removePersonFromList(person, persons)
                            person.relationshipStatus = relationshipStatus
                            reply = "Your " + relationshipStatus + ". " + random.choice(neutralUnderstandingWords)
     
                    if person.lengthOfRelationship is None:
                        lengthOfRelationship = input(reply + "How long have you known %s for?\n\t> " % person.personName)
                        person.lengthOfRelationship = lengthOfRelationship
                        reply = (random.choice(neutralUnderstandingWords) + random.choice(askMoreFeelingQuestions)) % matchingCategories[0].lower()
                        return reply
                        
                    else:
                        reply = random.choice(neutralUnderstandingWords) + " " + random.choice(askKeepGoing)
                        return reply

            else:   
                if matchingCategories[0] == "Depressed":
                    reply = random.choice(sadUnderstandingWords)
                elif matchingCategories[0] == "Neutral":
                    reply = random.choice(neutralUnderstandingWords)
                elif matchingCategories[0] == "Happy":
                    reply = random.choice(happyUnderstandingWords)

                reply += " " + (random.choice(askMoreFeelingQuestions) % matchingCategories[0].lower())
                return reply
            
