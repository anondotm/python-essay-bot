#Anan McHarris
#3/27/2017
#Section 001

#introduce the user, call intro function
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
    print("----------------------------")
    print("TOPIC AND RESEARCH QUESTION")
    print("----------------------------")
    print()
    
    #user = input("Here, we will discuss the topic and research question of your paper.")
    #print()
    user = input("Your topic for the paper can be summed up in two nouns whose relationship you will go on to explore, for example: 'Companion AI' and 'Femininity'")
    print()
    user = input("The first noun is usually a characteristic of games, such as 'Companion AI,' 'Environment Design' or 'Dialogue System,' while the second is often an abstract noun\
 that is being represented by the first (Class Relations, Cultural Identity, etc)")
    print()
    #user = input("Turning to your topic:")

    print("Finding topic:")
    #ask the user what their topic is with two nouns
    while(user != "My topic is " + noun1 + " and " + noun2):
        print()
        noun1 = input("The first noun (concrete) making up the topic...\n>")
        noun2 = input("The second noun (abstract) making up the topic...\n>")
        #confirm that these are the nouns
        user = input("Type out: 'My topic is " + noun1 + " and " + noun2 + "' to confirm\n>")

    print()

    user = input("The research question for the paper is pretty simple, investigating whether a particular relationship between your nouns exists, for example:")
    user = input("Do virtual spaces (concrete noun) in 'walking simulators' challenge (verb) conventional ideas about the process of 'making place (abstract noun)?")

    print()                         
        
    #ask the user to enter a question: how does one noun affect (verb) other "in games?"
    print("Formulating question:")
    question = input("A question concerning whether " + noun1 + " affects " + noun2 + " in a particular way...\n>")
    print()
    #print("Research Question:", question)

    #ask the user for the text they are using
    game = input("What game are you using to explore your research question?\n>")

    print()

    #call "examples" (maybe pass through nouns as arguments, or pass through the number of texts/examples for arguments?
    example(noun1, noun2, question, game)


#"examples" function that asks for a text that you're using  
def example(n1, n2, q, text):
    noun1 = n1
    noun2 = n2
    question = q
    #global game
    user = "yes"

    print()
    print("----------------------------")
    print("BODY")
    print("----------------------------")
    print()

    #print("Here we will use your text to evaluate your research question.")
    #print()
                         
    restate(noun1, noun2, question)
          
    print()

    prompt = input("It can be useful to take note of specific details or moments in games that represent your topic.")
    print()
    prompt = input("We can use these moments to learn more about your nouns and their relationship")
    print()

    print("Observing detail...")     
    while (user == "yes"):
        #ask for a "moment" in the text that involves the relationship b/w your nouns
        prompt = input("What is a detail in " + text + " that demonstrates the relationship between " + noun1 + " and " + noun2 + "?\n>")
        
        #ask for a summary of this moment
        prompt = input("Summarizing this 'moment' in a sentence...\n>")
        
        #ask for the significance of this moment in terms of your nouns WHY are nouns like this (what does it REVEAL?) underlying reason
        prompt = input("In context, what is the significance of this detail? What does this reveal about " + noun1 + " and/or " + noun2 + "? ((summary) happens, because of...)\n>")

        prompt = input("What are the consequences of these observations regarding your research question? (this happens because of (underlying reason), therefore...\n>")
        
        #ask the user if they want to add another "moment" of the game (ONLY ONE MORE)
        user = str.lower(input("Would you like to discuss another detail? (yes/no)\n>"))

        print()
                   
    conclusion(noun1, noun2, question)

#"conclusion" function that asks you to form a thesis
def conclusion(n1 ,n2, q):
    noun1 = n1
    noun2 = n2
    question = q
    
    print("----------------------------")
    print("CONCLUSION")
    print("----------------------------")

    print()
    restate(noun1, noun2, question)
    print()

    user = input("By observing the text, you've uncovered some aspects of the relationship between nouns, which hold significance in regards to your research question")
    print()

    print("Concluding:")
    #ask the user to assert a relationship: because noun is this, this is true abt other noun (because virtual place is so vulnerable, open to others making place is portrayed as incr. messy 
    user = input("Using your observations, a description of the relationship between nouns...\n>")
                         
    #ask the user to assert general relationship: (virtual space) affects (making place in games
        #in an unconventional and [implications] somewhat liberatory way)
    user = input("An answer to your research question...\n>")
                         
    #ask user about the implications of this
    user = input("What are some of the implications of this finding regarding other topics \n>")


#"restate" function reminds user of important information: topic and research question
def restate(n1, n2, q):
    print("TOPIC:", n1, "and", n2, "\nQUESTION:", q)



#a possible function is one that takes your topics and creates a question
#how [noun] creates [noun]
#as [noun] is [synthesis/descriptor], [noun] potrays [noun] into something that is [conclusion]



#The Ortega's arrival/boxes and angela's reaction reveals/is because virtual space is
#vulnerable, and therefore, making space is not intentional
