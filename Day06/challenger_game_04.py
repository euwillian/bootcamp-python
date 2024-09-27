"""
Challenger game link:

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def looping():
    turn_left()
    while wall_on_right():  # Enquanto houver parede na direita ande
        move()
    if not wall_on_right():  # Se não houver para na direita então
        turn_right()
        move()
        turn_right()
        move()
        while wall_on_right() and not wall_in_front():  # Enquanto houver paredes na direita (estará olhando para baixo) e não houver parede em frente, ande
            move()
        turn_left()


while not at_goal():
    if wall_in_front():
        looping()
    else:
        move()
