from vex import *
brain=Brain()

brain.screen.draw_rectangle((0 + ((i * (479/x)) * (((i * 2) - 1)/(i * 2)))), (0 + ((q * (239/y)) * (((q * 2) - 1)/(q * 2)))), (i * 479/x), 239, (i in color_list))









































def draw_buttons(x, color1, color2, color3, color4, color5, y):
    # Clear the screen
    brain.screen.clear_screen()
    color_list = [color1, color2, color3, color4, color5]
    for i in range(x):
        if x <= 6:
            brain.screen.set_fill_color(Color.WHITE)
            brain.screen.draw_rectangle(((0) + ((i * 479/x))/((i * 2) / (i * 2 - 1))), (i * 479/x), 239, (i in color_list))
            brain.screen.set_cursor(8 + (i * 479/x), 5)
            brain.screen.print("Port: " + str(i+1))
        if x >= 6:
            brain.screen.set_fill_color(Color.BLUE)
            # brain.screen.draw_rectangle(((0) + (((i * 479/x)/((i * 2) / (i * 2 - 1)))), (0 + (i * 239/y)), (i * 479/x), 239, (i in color_list))
            brain.screen.set_cursor(8, 28)
            brain.screen.print("Port: " + str(i+1))
    '''
    brain.screen.set_fill_color(Color.RED)
    brain.screen.draw_rectangle(240, 0, 240, 272)
    brain.screen.set_cursor(8, 28)
    brain.screen.print("RIGHT")
    '''
    
def main():
    draw_buttons(5, Color.BLUE, Color.RED, Color.GREEN, Color.YELLOW, Color.ORANGE, 0)
    while True:
        if brain.screen.pressing():
            # Get the coordinates of the touch
            x = brain.screen.x_position()
            # y = brain.screen.y_position() # Not needed for left/right
            if x < 96:
                # Left side pressed
                brain.screen.print_at(10, 20, "1")
            elif x > 96 and x < 96*2:
                # Right side pressed
                brain.screen.print_at(10, 20, "2")
            elif x > 96*2 and x < 96*3:
                # Right side pressed
                brain.screen.print_at(10, 20, "3")
            elif x > 96*3 and x < 96*4:
                # Right side pressed
                brain.screen.print_at(10, 20, "4")
            elif x > 96*4 and x < 96*5:
                # Right side pressed
                brain.screen.print_at(10, 20, "5")
            else:
                brain.screen.print_at(10, 20, "Invalid Press")
            # Wait for the user to release the screen to prevent repeated presses
            while brain.screen.pressing():
                wait(5, MSEC)
            # Clear status message
            brain.screen.clear_screen()
            draw_buttons(5)
        wait(5, MSEC)



















'''











                            (((0) + (((i * 479/x)/((i * 2) / (i * 2 - 1)))), (0 + (i * 239/y)), (i * 479/x), 239, (i in color_list))
                             

                            (0 + ((i * (479/x)) * (((i * 2) - 1)/(i * 2))))

                            '''