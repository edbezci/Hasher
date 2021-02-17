import pygame
import os
import src

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
button_colour = pygame.Color(75, 0, 130)
hover_colour = pygame.Color(255,105,180)

def Button(name, x, y, w, dist, action=None):
    '''
    this function creates the button on the screen.
    it takes the positions, fonts, colours and sizes and what to do when clicked
    '''

    pos = pygame.mouse.get_pos()  # pygame methods to recognize that the mouse is clicked
    click = pygame.mouse.get_pressed()  # pygame methods to recognize that the mouse is clicked
    if x < pos[0] < x+w and y < pos[1] < y+40:  # it is the x and y positions of the mouse
        # the pygame.draw.rect x,y,w, and 40 are the dimensions.
        pygame.draw.rect(src.display, hover_colour, [x, y, w, 40])  # change the hover colour
        # if someone clicked and there is an action associated with that button
        if click[0] == 1 and action != None:
            action()  # do that action
    else:  # or
        pygame.draw.rect(src.display, button_colour, [x, y, w, 40])  # just draw and hold it
    font = pygame.font.Font(src.bitterfont, 15)  # font object
    # renders the text on the secreen
    text = font.render(name, True, white)
    text_rect = text.get_rect(center=((x+ (x+w)) /2, (y + (y+40))/2))
    src.display.blit(text, text_rect)

def ButtonWithReturn(name, x, y, w, dist, val=None):
    '''
    this function creates the button on the screen but with a return value
    same as the function above essentially
    '''

    pos = pygame.mouse.get_pos()  # pygame method for mouse. it gets the mouse's position (x,y) on the screen
    click = pygame.mouse.get_pressed()  # pygame method to see if it is pressed
    if x < pos[0] < x+w and y < pos[1] < y+40:  # if mouse is on the button
        pygame.draw.rect(src.display, hover_colour, [x, y, w, 40])  # change the hover colour
        if click[0] == 1:  # if clicked while it is on
            return val  # do what the button calls for
    else:  # if not
        pygame.draw.rect(src.display, button_colour, [x, y, w, 40])  # just draw it
    font = pygame.font.Font(src.bitterfont, 14)  # font object
    # renders the text on the secreen
    text = font.render(name, True, white)
    text_rect = text.get_rect(center=((x+ (x+w)) /2, (y + (y+40))/2))
    src.display.blit(text, text_rect)  # shows the text
    return 0  # return 0 from the button function




def AddText(text, pos, color=white):
    '''
    add texts to the screen
    takes text which is a string object as an argument
    '''

    font = pygame.font.Font(src.bitterfont, 16)  # creating font with size
    # creating font pygame text object with size, colour and text
    renderedText = font.render(text, True, color)
    # displaying text on the screen, pos is the position of where it should appear
    src.display.blit(renderedText, pos)

def InsertSecret(text):
    '''
    this function takes an input of string for the algorithm efficieny function.
    '''

    pygame.display.set_caption(text)
    inpText = ""  # empty placeholder
    enter = True  # enable enter
    while enter:  # starting the algorithm
        # pygame method to fill the screen, takes colours and a display object
        src.display.fill(black)
        src.display.blit(src.bg,(0,0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():  # again iterating as an important pygame method to set the features.
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # Here is to tell the computer to recognise if a keybord key is pressed.
                if event.key == pygame.K_ESCAPE: # if that keyboard key is ESC
                    exit() # call for the exit function.
            if event.type == pygame.KEYDOWN:  # if a key is pressed
                if event.key == pygame.K_RETURN:  # and if this key is enter
                    enter = False  # enter changes the status of true to false and ends the loop, you entered what you wanted
                elif event.key == pygame.K_BACKSPACE:  # if backspace is pressed
                    # backspace deletes the last letter of the input. this [:-1] called slicing
                    inpText = inpText[:-1]
                else:  # if none of this happened
                    inpText += event.unicode  # takes care of capslocks and shiftkeys
        AddText("Press \"ENTER\" to continue...!", (128, 270), white)
        AddText(text, (128, 220), white)  # displaying the text
        pygame.draw.rect(src.display, white, (290, 215, 250, 40))  # displaying the text
        AddText(inpText, (295, 225), black)  # displaying the text
        # updates the screen every turn
        pygame.display.flip()
        # will not run more than 15 frames per second
        src.clock.tick(60)  # 15 frames per second
    return inpText
