from game_components.story_input import Story
from game_components.storyline import Storyline


madlibs = Story()
story_line = Storyline()
#Get user input
game_input = madlibs.user_input()

#Put input into story
story_line.madlibs(game_input)
#Print out story

'''
Encapsulation: Make stuff private: _ makes it private only used in the class
Abstraction: Taking something complex and making it simple using a method without knowing how it is working under the hood. Storyline being used in main without seeing the dettailed information.
Inheritance: Child class has a copy of parent methods
Polymorphism: overwriting a method
'''