#Anan McHarris
#4/30/2017
#Section 001

import random
import datetime
import sys

file_name = ""
noun1 = ""
noun2 = ""

question = ""
game = ""
synth = ""

#"intro" function that establishes your topic and question
def intro():
    noun1 =  ""
    noun2 = ""
    question = ""

    print()
    header("topic and research question")
    print()
    
    #user = input("Here, we will discuss the topic and research question of your paper.")
    #print()
    user = input("Your topic for the paper can be summed up in two nouns whose relationship you will go on to explore, for example: 'Companion AI' and 'Femininity'")
    print()
    user = input("The first noun is usually a characteristic of games, such as 'Companion AI,' 'Environment Design' or 'Dialogue System,' while the second is often an abstract noun\
 that is being represented by the first (Class Relations, Cultural Identity, etc)")
    print()
    #user = input("Turning to your topic:")

    print("Finding topic...")
    #ask the user what their topic is with two nouns
    noun1 = userCheck(input("The first noun (concrete) making up the topic...\n>"))
    if (noun1 == "random"):
        noun1 = seekrit("noun1")
    noun2 = userCheck(input("The second noun (abstract) making up the topic...\n>"))
    if (noun2 == "random"):
        noun2 = seekrit("noun2")
        #confirm that these are the nouns
        #user = userCheck(input("Type out: 'My topic is " + noun1 + " and " + noun2 + "' to confirm\n>"))
    print()

    user = input("The research question for the paper is pretty simple, investigating whether a particular relationship between your nouns exists, for example:")
    user = input(readQuestion())
    #user = input("Do virtual spaces (concrete noun) in 'walking simulators' challenge (verb) conventional ideas about the process of 'making place (abstract noun)?")

    print()                         
        
    #ask the user to enter a question: how does one noun affect (verb) other "in games?"
    print("Formulating question (enter 'example' for another example)...")
    question = userCheck(input("A question concerning whether " + noun1 + " affects " + noun2 + " in a particular way...\n>"))
    #if the user types in "example", call the "example" function and ask again
    if (question == "example"):
        while (question == "example"):
            readQuestion()
            print()
            question = userCheck(input("A question concerning whether " + noun1 + " affects " + noun2 + " in a particular way...\n>"))
    print()
    #print("Research Question:", question)

    #ask the user for the text they are using
    game = userCheck(input("What game are you using to explore your research question?\n>"))

    print()

    #call "examples" (maybe pass through nouns as arguments, or pass through the number of texts/examples for arguments?
    body(noun1, noun2, question, game)


#"body" function that asks for a text that you're using  
def body(n1, n2, q, text):
    noun1 = n1
    noun2 = n2
    question = q
    #global game
    user = "yes"

    print()
    header("body")
    print()

    #print("Here we will use your text to evaluate your research question.")
    #print()
                         
    restate(noun1, noun2, question)

    #SAVING ALL THE USER'S INFORMATION
    saveInfo(True, "topic", noun1 + " and " + noun2)
    saveInfo(False, "question", question)
    saveInfo(False, "game", text)
          
    print()

    prompt = input("It can be useful to take note of specific details or moments in games that represent your topic.")
    print()
    prompt = input("We can use these moments to learn more about your nouns and their relationship")
    print()

    print("Observing detail...")     
    while (user == "yes"):
        #ask for a "moment" in the text that involves the relationship b/w your nouns
        prompt_1 = userCheck(input("What is a detail in " + text + " that demonstrates the relationship between " + noun1 + " and " + noun2 + "?\n>"))
        #if the user types in "example", call the "example" function and ask again

        """
        if (question == "example"):
            while (question == "example"):
                readDetail()
                print()
                prompt_1 = userCheck(input("What is a detail in " + text + " that demonstrates the relationship between " + noun1 + " and " + noun2 + "?\n>"))
        """
        
        #ask for a summary of this moment
        prompt_2 = userCheck(input("Summarizing this 'moment' in a sentence...\n>"))
        
        #ask for the significance of this moment in terms of your nouns WHY are nouns like this (what does it REVEAL?) underlying reason
        prompt_3 = userCheck(input("In context, what is the significance of this detail? What does this reveal about " + noun1 + " and/or " + noun2 + "? ((summary) happens, because of...)\n>"))

        prompt_4 = userCheck(input("What are the consequences of these observations regarding your research question? (this happens because of (underlying reason), therefore...\n>"))

        #save all detail_info into a detail_list
        detail_list = [prompt_1,prompt_2,prompt_3,prompt_4]

        #SAVE USERS DETAIL INFORMATION TO THE FILE
        saveInfo(False, "detail", detail_list)

        print()
        
        #ask the user if they want to add another "moment" of the game
        user = userCheck(str.lower(input("Would you like to discuss another detail? (yes/no)\n>")))

        print()

    #if (prompt != "yes"):              
    conclusion(noun1, noun2, question)

#"conclusion" function that asks you to form a thesis/re-evaluate questions, etc.
def conclusion(n1 ,n2, q):
    noun1 = n1
    noun2 = n2
    question = q
    
    header("conclusion")

    print()
    restate(noun1, noun2, question)
    print()

    user = input("By observing the text, you've uncovered some aspects of the relationship between nouns, which hold significance in regards to your research question")
    print()

    print("Concluding:")
    #ask the user to assert a relationship: because noun is this, this is true abt other noun (because virtual place is so vulnerable, open to others making place is portrayed as incr. messy 
    prompt_1 = userCheck(input("Using your observations, a description of the relationship between nouns...\n>"))
                     
    #ask the user to assert general relationship: (virtual space) affects (making place in games
        #in an unconventional and [implications] somewhat liberatory way)
    prompt_2 = userCheck(input("An answer to your research question...\n>"))

    #ask user about the implications of this
    prompt_3 = userCheck(input("What are some of the implications of this finding regarding other topics \n>"))

    #save all conclusion info to a conclusion list
    conclusion_list = [prompt_1,prompt_2,prompt_3]

    #SAVE CONCLUSION INFORMATION TO THE FILE
    saveInfo(False, "conclusion", conclusion_list)

    #bye
    end()

#sends you off with greeting and then terminates the program
def end():
    print()
    print("***")  
    user = input("All done walking through argument")
    print()
    print("Good bye!")
    sys.exit("Bye!")#FOREVER

#"restate" function reminds user of important information: topic and research question
def restate(n1, n2, q):
    print("TOPIC:", n1, "and", n2, "\nQUESTION:", q)

#functions created for assign7

#"header" function transforms a string into a "HEADER" [assign 7]
def header(headString):
    print("----------------------------")
    print(str.upper(headString))
    print("----------------------------")

#SECRET FUNCTION that generates random topic/question (have your computer write amazing essays for you!) [assign7]
def seekrit(part):
    nounsListOne = ["Companion AI", "Menu UI", "Enemy AI", "Shaders", "Movement Controls", "Controller", "Online Multiplayer", "Jump Physics"]
    nounsListTwo = ["The Invisible Hand of the Market", "Transhumanism", "The Sharing Economy", "Respectful Dialogue", "Free Speech", "Passion over Profit", "Game Theory"]

    if (part == "noun1"):
        randSelect = random.randint(0,len(nounsListOne))
        return nounsListOne[randSelect]   
    elif (part == "noun2"):
        randSelect = random.randint(0,len(nounsListTwo))
        return nounsListTwo[randSelect]

#Function that takes text and textType, and stores users information (topic, question, argument) to a file [assign8]
def saveInfo(first, textType, textContent):
    global file_name
    
    #if this is the first time that the user is using the file, use the "w" flag when opening file_object (create!)
    if (first == True):

        #format the name properly
        textContent=textContent.lower()
        textContent=textContent.replace(" ","_")
        file_name = textContent+".txt"

        #use your newly-formatted topics as the file-name
        file_object = open(file_name,"w")
        
    #otherwise, use the "a" flag when opening file_object (append!)
    else:
        file_object = open(file_name,"a")

    #depending on what type of information, the user is passing (textType), write or append textContent with a certain format
    if (textType == "topic"):
        file_object.write("I'm walking through an argument:\n")
        file_object.write("----------------------------\n")
        file_object.write("INTRO\n")
        file_object.write("----------------------------\n\n")
        
    if (textType == "question"):
        file_object.write("RESEARCH QUESTION:\n")
        file_object.write(textContent + "\n\n")

    elif (textType == "game"):
        file_object.write("CASE STUDY:\n")
        file_object.write(textContent + "\n\n")
        
        file_object.write("----------------------------\n")
        file_object.write("BODY\n")
        file_object.write("----------------------------\n\n")

    elif (textType == "detail"):
        file_object.write("DETAIL: " +textContent[0]+ "\n")
        file_object.write("\tThis happened: " +textContent[1]+ "\n")
        file_object.write("\tWhich reveals: " +textContent[2]+ "\n")
        file_object.write("\tTherefore: " +textContent[3]+ "\n\n")

    if (textType == "conclusion"):
        file_object.write("----------------------------\n")
        file_object.write("CONCLUSION\n")
        file_object.write("----------------------------\n\n")

        file_object.write("RELATIONSHIP B/W NOUNS:\n")
        file_object.write(textContent[0]+ "\n\n")
        file_object.write("CONCLUSION:\n")
        file_object.write(textContent[1]+ "\n\n")
        file_object.write("IMPLICATIONS:\n")
        file_object.write(textContent[2]+ "\n\n")

#Function that reads and prints out a random research question from a .txt file
def readQuestion():
    #create a file object that we "r"ead off of
    file_object = open("questions.txt", "r")
    #store the entire string in a variable with "read()" function
    uncut_data = file_object.read()
    #turn uncut_data into a list with "split()" function
    cut_data = uncut_data.split("\n")
    #select a random value and print!
    selection = random.randint(0,len(cut_data)-1)
    return(cut_data[selection])

"""
#Function that reads and prints out a random research question from a .txt file
def readDetail():
    #create a file object that we "r"ead off of
    file_object = open("details.txt", "r")
    #store the entire string in a variable with "read()" function
    uncut_data = file_object.read()
    #turn uncut_data into a list with "split()" function
    cut_data = uncut_data.split("\n")
    #select a random value and print!
    selection = random.randint(0,len(cut_data)-1)
    print("example:", cut_data[selection])
"""
    
#Function that validates user input, making sure they didn't accidentally skip questions
def userCheck(user):
    if(user == ""):
        print()
        correction = ""

        #while there is no input, continue asking for a correction
        while(correction==""):
            correction = input("It looks like you accidentally skipped the question? (Re-)enter intended input...\n>")
        
        return correction
    elif(user == "restart"):
        print()
        print("----------------------------")
        print("RE-STARTING")
        print("----------------------------")
        print()
        
        noun1 = input("Noun one for Topic...\n>")
        noun2 = input("Noun two for Topic...\n>")
        question = input("Your queston...\n>")
        text = input("The game your using as a case study...\n>")
        body(noun1, noun2, question, text)
    else:
        return user
        

