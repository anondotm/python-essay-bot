#Anan McHarris
#3/27/2017
#Section 001

import myFunctions

user = input("Hi, I'm a bot designed to help you walk through an argument for 'Tackling Representation in Games.'")

while (user != "yes" and user != "no"):
    user = str.lower(input("Do you already know your topic and Research Question(yes/no)?\n>"))
    if (user == "no"):
        myFunctions.intro()
    elif (user == "yes"):
        noun1 = input("Noun one for Topic...\n>")
        noun2 = input("Noun two for Topic...\n>")
        question = input("Your queston...\n>")
        game = input("The game you're using as a case study...\n>")
        myFunctions.example(noun1, noun2, question, game)
    else:
        print("I'm sorry, I didn't understand that.")
        print()
print()
print("***")  
user = input("All done walking through argument")
print()
print("Good bye!")
