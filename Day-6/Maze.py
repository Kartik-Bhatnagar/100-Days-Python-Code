def turn_right():
    turn_left()
    turn_left() 
    turn_left()
while not at_goal():    
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()        
    elif right_is_clear():
        turn_right()
        move()

        
        
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
