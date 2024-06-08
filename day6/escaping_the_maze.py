## DAY 6: FINAL PROJECT ##

# Go to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world2.json&url=user_world%3Aproblem_world2.json for accessing the challenge

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    else:
        turn_left()