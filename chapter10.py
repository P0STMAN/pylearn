"""
Pygame base template for opening a window, done with functions

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [500, 700]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    # Speed in pixels per frame
    x_speed = 0
    y_speed = 0

    # Current position
    x_coord = 10
    y_coord = 10

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # user pressed a key down
            elif event.type == pygame.KEYDOWN:
                # if it was an arrow key adjust speed
                if event.key == pygame.K_LEFT:
                    x_speed = -4
                elif event.key == pygame.K_RIGHT:
                    x_speed = 4
                elif event.key == pygame.K_UP:
                    y_speed = -4
                elif event.key == pygame.K_DOWN:
                    y_speed = 4

            # user let up on a key
            elif event.type == pygame.KEYUP:
                # if its an arrow key, reset speed to 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        x_coord += x_speed
        y_coord += y_speed

        # check if x_coord is out of screen bounderies
        if x_coord < 0:
            x_coord = 0
        elif x_coord > size[0] - 12:
            x_coord = size[0] - 12

        # check if y_coord is out of screen bounderies
        if y_coord < 0:
            y_coord = 0
        elif y_coord > size[1] - 27:
            y_coord = size[1] - 27

        # pos = pygame.mouse.get_pos()
        # x = pos[0]
        # y = pos[1]

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        draw_stick_figure(screen, x_coord, y_coord)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


if __name__ == "__main__":
    main()