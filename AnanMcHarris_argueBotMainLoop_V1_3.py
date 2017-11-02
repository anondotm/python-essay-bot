#Anan McHarris
#4/30/2017
#Section 001

import AnanMcHarris_argueBotModule_V1_3

user = ""

prompt = input("Hi, I'm a bot designed to help you walk through an argument for 'Tackling Representation in Games.'")

while (user != "yes" and user != "no"):
    user = str.lower(input("Do you already know your topic and Research Question(yes/no)?\n>"))
    if (user == "no"):
        AnanMcHarris_argueBotModule_V1_3.intro()
    elif (user == "yes"):
        noun1 = AnanMcHarris_argueBotModule_V1_3.userCheck(input("Noun one for Topic...\n>"))
        noun2 = AnanMcHarris_argueBotModule_V1_3.userCheck(input("Noun two for Topic...\n>"))
        question = AnanMcHarris_argueBotModule_V1_3.userCheck(input("Your queston...\n>"))
        game = AnanMcHarris_argueBotModule_V1_3.userCheck(input("The game you're using as a case study...\n>"))
        AnanMcHarris_argueBotModule_V1_3.body(noun1, noun2, question, game)
    else:
        print("I'm sorry, I didn't understand that.")
        print()
