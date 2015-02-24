#import modules
import random

#setup dictionaries and lists
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

adjective = ["Windy", "Water Logged", "Dastardly"]
noun = ["Shipwreck", "Parrot", "Eye Patch"]

#get preferences based off the questions dictionary
def preferences():
    answers = {}
    for n in questions:
        answer = raw_input(questions[n])
        if answer == "y" or answer == "Y":
            answers[n] = True
        else:
            answers[n] = False
    return answers
#Use results of preferences to pull ingredients
def drink_selection(answers):
    drink = []
    for n in answers:
        if answers[n] == True:
            drink.append(random.choice(ingredients[n]))
    return drink

def drink_name():
    cocktail = random.choice(adjective) + " " + random.choice(noun)
    return cocktail

#order in which to run the functions
def main():
    answers = preferences()
    drink = drink_selection(answers)
    cocktail_name = drink_name()
    print "Ye would like a ", cocktail_name
    print "The recipe is"
    print drink
    another = raw_input("Would ye like another?")
    if another == "y" or another == "Y":
        main()


#force run of the functions if not in in the command line
if __name__ == "__main__":
    main()

