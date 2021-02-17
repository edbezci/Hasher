
import pygame
import pygame_menu

import src # our source module with the algorithms
import sys # another python library, here enables us to 
import hlp # module with the helper functions



# activate flag for algorithm list menu
intro2 = False
# introduction menu
#clk = pygame.time.Clock()
pygame.init()

secret = ""

def StartIntro2():
    global intro2  # access the global variable
    intro2 = True  # turn it true, these are all helper functions

def Introduction():
    '''
    setting the intro menu
    '''
    global intro2, secret # accessing global variable
    pygame.display.set_caption("Hashing Algorithms Visualization Tool")
    while intro2 == False:  # initial loop and setting the exit
        src.display.fill((0,0,0))  # setting the display colour
        src.display.blit(src.bg,(0,0))  ## this is a pygame method allowing us to paste objects into the screen. it takes pixel location and the object as arguments.
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # Here is to tell the computer to recognise if a keybord key is pressed.
                if event.key == pygame.K_ESCAPE: # if that keyboard key is ESC
                    exit() # call for the exit function.
            if event.type == pygame.MOUSEBUTTONDOWN:  # starting the initial loop with first game events, i.e. quit and mouse button
                if event.button == 1:  # pygame method defining the button in the GUI
                    pos = pygame.mouse.get_pos()  # displays the mouse position on the screen
                    # starting the initial loop with first game events, ie. quit and mouse button
                    if xwidth < pos[0] < xwidth+120 and 350 < pos[1] < 350+30:
                        srctTxt = hlp.InsertSecret("Text for Encription:")  # getting the number of lines
                        if srctTxt != "":  # if the string is not empty
                            try:
                                # input gives string so this one turns it into an integer
                                secret = srctTxt
                                StartIntro2()
                            except:  # if that is not happening
                                secret = "N/A"
                                
        font = pygame.font.Font(src.bitterfont, 21)  # creating font with size
    # creating font pygame text object with size, colour and text
        renderedText = font.render("Welcome to the Hashing Algorithms Comparison Tool", True, (255,255,255))

    # displaying text on the screen, pos is the position of where it should appear
        surface = pygame.display.get_surface()
        xwidth = (surface.get_width()/2) - 60
        twidth = surface.get_width() /2 - renderedText.get_width()/2
        src.display.blit(renderedText, (twidth,140))

        hlp.Button("Insert Message", xwidth, 350, 120, 30, None)
        hlp.Button("Continue", xwidth, 400, 120, 30, StartIntro2)  # continue button
        hlp.Button("Exit", xwidth, 450, 120,
                              30, sys.exit)
        # updates the screen every turn
        pygame.display.flip()
        # will not run more than 10 frames per second
        src.clock.tick(60)
    Introduction2()  # calls back the introduction function

# algorithm list menu


def Introduction2():
    '''
    Setting the algorithms menu
    '''
    display = pygame.display.set_mode((1280, 550),pygame.FULLSCREEN | pygame.DOUBLEBUF)  # seting the display
    # pygame method for captioning
    pygame.display.set_caption("Hashing Comparison Tool")
    #src.ChangeColour()  # calling change colour function
    while True:  # stating the loop
        display.fill((0,0,0))  # setting the display colour
        src.display.blit(src.bg,(0,0)) # this is a pygame method allowing us to paste objects into the screen. it takes pixel location and the object as arguments.
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # Here is to tell the computer to recognise if a keybord key is pressed.
                if event.key == pygame.K_ESCAPE: # if that keyboard key is ESC
                    exit() # call for the exit function.
        surface = pygame.display.get_surface()
        xwidth = (surface.get_width()/2) - 125
        pygame.draw.rect(display, hlp.button_colour, (xwidth-7, 85, 264, 395), 3)
    
        v1 = hlp.ButtonWithReturn("MD5 Algorithm", xwidth, 90, 250,
                              30, 1)  # positioning function buttons
        v2 = hlp.ButtonWithReturn("SHA1 Algorithm", xwidth, 190,
                              250, 30, 2)  # positioning function buttons
        v3 = hlp.ButtonWithReturn("SHA256 Algorithm", xwidth, 290, 250,
                              30, 3)  # positioning function buttons
        #v4 = hlp.ButtonWithReturn("Efficiency Comparison",xwidth, 390, 250,
                              #30, 4)  # positioning function buttons
        hlp.Button("Exit to Desktop", xwidth, 390, 250,
                              30, sys.exit)  # adding an exit button
        if v1 > 0 or v2 > 0 or v3 > 0:  # if any is chosen, break the loop and go to the choice
            break
        pygame.display.flip()  # updates the screen every turn
        src.clock.tick(60)  # will not run more than 10 frames per second
    if v1 > 0:  # calling for choice functions to go for
        src.dspMd5() # calling for choice functions to go for
    elif v2 > 0:  # calling for choice functions to go for
        src.dspSHA1()  # calling for choice functions to go for
    elif v3 > 0:  # calling for choice functions to go for
       src.dspSHA256()  # calling for choice functions to go for
    