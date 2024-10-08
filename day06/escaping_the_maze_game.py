"""

Escaping the maze game - Final Project

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    count = 0
    while right_is_clear() and count < 5:
        turn_right()
        move()
        count += 1
    if front_is_clear():
        move()
    else:
        turn_left()