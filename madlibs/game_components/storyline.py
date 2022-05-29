from game_components.story_input import Story

class Storyline(Story):
    def __init__(self):
        self.story = ""

    def madlibs(self, story_output):
        story = f"""My name is {story_output[0]} and I am {story_output[1]} years old. If I were
president, I'd do a whole bunch of {story_output[2]} things:
1. I would drive the biggest {story_output[3]} car in the country. And that
car would go faster than any other {story_output[4]} in the world!
2. Everyone would eat pepperoni {story_output[5]} OF FOOD for dinner.
3. I would live in the Statue of {story_output[6]} and build a 
{story_output[7]} pool at her feet. 
4. I would wear a/an {story_output[8]} on my head, and 
everyone would say I look {story_output[9]} like {story_output[10]}.
5. School would be open only {story_output[11]} of days a year.
6. I would give my friends the best jobs. I would nominate
{story_output[12]} to be secretary of (the) {story_output[13]}, and
{story_output[14]} could be vice {story_output[15]}!"""

        print(story)
