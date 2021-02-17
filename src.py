import pygame
import os
import random
import math
import sys
import timeit
import functools

import hlp
import intro
import md5
import sha1
import sha256


# initialise Pygame library, it is necessary in Programs using Pygame
pygame.init()

line_colour = pygame.Color(50, 50, 120)

# initialise window size at 800 * 550 with a caption
display = pygame.display.set_mode((1280, 550), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Hashing Algorithm Comparison Tool")
# frames per second determines how many frames should be refreshed per second
clock = pygame.time.Clock()


#Setting up the background image
background_image = os.path.abspath("resources/desc_bgrnd.jpg")
bg_image = pygame.image.load(background_image)
bg = pygame.transform.scale(bg_image, (1280,550))

# Font
bitterfont = os.path.abspath("resources/bitterfont.otf")

def dspMd5():
    pygame.display.set_caption("MD5 Algorithm")  # adding a caption
    display = pygame.display.set_mode((1280, 550),pygame.FULLSCREEN)
    effc = timeit.Timer(functools.partial(md5.md5,intro.secret))
    efcTime = effc.timeit(15)
    effcsha1 = timeit.Timer(functools.partial(sha1.sha1,intro.secret))
    efcTimesha1 = effc.timeit(15)
    effcSHA2 = timeit.Timer(functools.partial(sha256.sha256,intro.secret))
    efcTimeSHA2 = effc.timeit(15)
    m = max(efcTime,efcTimesha1,efcTimeSHA2)
    efcMD5 = (efcTime / m) * 250
    efcSHA1 = (efcTimesha1 / m) * 250
    efcSHA2 = (efcTimeSHA2 / m) * 250
    while True:  # starting the game loop
        display.fill((0,0,0))  # pygame method to fill the screen, takes colours and a display object
        #display.blit(bg,(0,0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # Here is to tell the computer to recognise if a keybord key is pressed.
                if event.key == pygame.K_ESCAPE: # if that keyboard key is ESC
                    exit() # call for the exit function.
        surface = pygame.display.get_surface()
        w,h = surface.get_size()
        loc1, loc2 = surface.get_size()
        w = (w/2) - 60
        h = (h/2) - 200
        hlp.AddText("Encrypted Text: "+ intro.secret, (w-150, h))
        hlp.AddText("Padded Text: " + str(md5.padding(intro.secret))[0:15]+"...", (w-150,h+40))
        hlp.AddText("MD5 Hashing: "+ md5.md5(intro.secret), (w -150, loc2 - 175))
        hlp.AddText(str(round(float(efcTime),4)) +" seconds passed to execute this algorithm", (w -150, 5*loc2/6))
        hlp.Button("Exit", 350, 5, 100,
                              30, sys.exit)
        back = hlp.ButtonWithReturn("Back", 900, 5, 100, 30, 1)
        if back > 0:  # if back has a value, which means it has been clicked, stop the bigger loop that we started, i.e. the game loop, and break the game loop
            break

        pygame.draw.line(display, line_colour, (400, 250), (400, 500), 2)
        # pygame method, takes display, colour, and positions of where the lines start and end
        pygame.draw.line(display, line_colour, (350, 500), (950, 500), 2)

        hlp.AddText("MD5", (465, 510), hlp.white)
        hlp.AddText("SHA1", (615, 510), hlp.white)
        hlp.AddText("SHA256", (765, 510), hlp.white)

        hlp.AddText("0s",(395,505), hlp.white)
        hlp.AddText(str(round(float(efcTime),5)), (460, 230), hlp.white) 
        hlp.AddText(str(round(float(efcTimesha1),5)), (610, 230), hlp.white) 
        hlp.AddText(str(round(float(efcTimeSHA2),5)), (760, 230), hlp.white) 
        
        bPos = 500
        pygame.draw.rect(display, hlp.button_colour, (465, bPos-efcMD5, 50, efcMD5))
        pygame.draw.rect(display, hlp.button_colour, (615, bPos-efcSHA1, 50, efcSHA1))
        pygame.draw.rect(display, hlp.button_colour, (765, bPos-efcSHA2, 50, efcSHA2))


        pygame.display.flip()
        # will not run more than 30 frames per second
        clock.tick(30)
    intro.Introduction2()

def dspSHA1():
    pygame.display.set_caption("MD5 Algorithm")  # adding a caption
    display = pygame.display.set_mode((1280, 550),pygame.FULLSCREEN)
    effc = timeit.Timer(functools.partial(sha1.sha1,intro.secret))
    efcTime = effc.timeit(15)
    effcMDA = timeit.Timer(functools.partial(md5.md5,intro.secret))
    efcTimeMDA = effc.timeit(15)
    effcSHA2 = timeit.Timer(functools.partial(sha256.sha256,intro.secret))
    efcTimeSHA2 = effc.timeit(15)
    m = max(efcTime,efcTimeMDA,efcTimeSHA2)
    efcMD5 = (efcTimeMDA / m) * 250
    efcSHA1 = (efcTime / m) * 250
    efcSHA2 = (efcTimeSHA2 / m) * 250
    while True:  # starting the game loop
        display.fill((0,0,0))  # pygame method to fill the screen, takes colours and a display object
        #display.blit(bg,(0,0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # Here is to tell the computer to recognise if a keybord key is pressed.
                if event.key == pygame.K_ESCAPE: # if that keyboard key is ESC
                    exit() # call for the exit function.
        surface = pygame.display.get_surface()
        loc1, loc2 = surface.get_size()
        w,h = surface.get_size()
        w = (w/2) - 60
        h = (h/2) - 200
        hlp.AddText("Encrypted Text: "+ intro.secret, (w-150, h))
        hlp.AddText("Padded Text: " + str(md5.padding(intro.secret))[0:15]+"...", (w-150,h+30))
        hlp.AddText("SHA1 Hashing: "+ sha1.sha1(intro.secret), (w -150, loc2 - 175))
        hlp.AddText(str(round(float(efcTime),4)) +" seconds passed to execute this algorithm", (w-150, 5*loc2/6))
        hlp.Button("Exit", 350, 5, 100,
                              30, sys.exit)
        back = hlp.ButtonWithReturn("Back", 900, 5, 100, 30, 1)
        if back > 0:  # if back has a value, which means it has been clicked, stop the bigger loop that we started, i.e. the game loop, and break the game loop
            break

        pygame.draw.line(display, line_colour, (400, 250), (400, 500), 2)
        # pygame method, takes display, colour, and positions of where the lines start and end
        pygame.draw.line(display, line_colour, (350, 500), (950, 500), 2)

        hlp.AddText("0s",(395,505), hlp.white)
        hlp.AddText("SHA1", (465, 510), hlp.white)
        hlp.AddText("MD5", (615, 510), hlp.white)
        hlp.AddText("SHA256", (765, 510), hlp.white)

        hlp.AddText(str(round(float(efcTime),5)), (460, 230), hlp.white) 
        hlp.AddText(str(round(float(efcTimeMDA),5)), (610, 230), hlp.white) 
        hlp.AddText(str(round(float(efcTimeSHA2),5)), (760, 230), hlp.white) 
        
        bPos = 500
        pygame.draw.rect(display, hlp.button_colour, (465, bPos-efcSHA1, 50, efcSHA1))
        pygame.draw.rect(display, hlp.button_colour, (615, bPos-efcMD5, 50, efcMD5))
        pygame.draw.rect(display, hlp.button_colour, (765, bPos-efcSHA2, 50, efcSHA2))
        pygame.display.flip()
        # will not run more than 30 frames per second
        clock.tick(30)
    intro.Introduction2()

def dspSHA256():
    pygame.display.set_caption("MD5 Algorithm")  # adding a caption
    display = pygame.display.set_mode((1280, 550),pygame.FULLSCREEN)
    effc = timeit.Timer(functools.partial(sha256.sha256,intro.secret))
    efcTime = effc.timeit(15)
    effcSHA1 = timeit.Timer(functools.partial(sha1.sha1,intro.secret))
    efcTimeSHA1 = effc.timeit(15)
    effcMDA = timeit.Timer(functools.partial(md5.md5,intro.secret))
    efcTimeMDA = effc.timeit(15)
    m = max(efcTime,efcTimeMDA,efcTimeSHA1)
    efcMD5 = (efcTimeMDA / m) * 250
    efcSHA2 = (efcTime / m) * 250
    efcSHA1 = (efcTimeSHA1 / m) * 250
    while True:  # starting the game loop
        display.fill((0,0,0))  # pygame method to fill the screen, takes colours and a display object
        #display.blit(bg,(0,0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # Here is to tell the computer to recognise if a keybord key is pressed.
                if event.key == pygame.K_ESCAPE: # if that keyboard key is ESC
                    exit() # call for the exit function.
        surface = pygame.display.get_surface()
        loc1, loc2 = surface.get_size()
        w,h = surface.get_size()
        w = (w/2) - 60
        h = (h/2) - 200
        hlp.AddText("Encrypted Text: "+ intro.secret, (w-150, h))
        hlp.AddText("Padded Text: " + str(md5.padding(intro.secret))[0:15]+"...", (w-150,h+30))
        hlp.AddText("SHA256 Hashing: "+ sha256.sha256(intro.secret), (w -150, loc2 - 175))
        hlp.AddText(str(round(float(efcTime),4)) +" seconds passed to execute this algorithm", (w-150, 5*loc2/6))
        hlp.Button("Exit", 350, 5, 100,
                              30, sys.exit)
        back = hlp.ButtonWithReturn("Back", 900, 5, 100, 30, 1)
        if back > 0:  # if back has a value, which means it has been clicked, stop the bigger loop that we started, i.e. the game loop, and break the game loop
            break

        pygame.draw.line(display, line_colour, (400, 250), (400, 500), 2)
        # pygame method, takes display, colour, and positions of where the lines start and end
        pygame.draw.line(display, line_colour, (350, 500), (950, 500), 2)

        hlp.AddText("0s",(395,505), hlp.white)
        hlp.AddText("SHA256", (465, 510), hlp.white)
        hlp.AddText("MD5", (615, 510), hlp.white)
        hlp.AddText("SHA1", (765, 510), hlp.white)

        hlp.AddText(str(round(float(efcTime),5)), (460, 230), hlp.white) 
        hlp.AddText(str(round(float(efcTimeMDA),5)), (610, 230), hlp.white) 
        hlp.AddText(str(round(float(efcTimeSHA1),5)), (760, 230), hlp.white) 
        
        bPos = 500
        pygame.draw.rect(display, hlp.button_colour, (465, bPos-efcSHA2, 50, efcSHA2))
        pygame.draw.rect(display, hlp.button_colour, (615, bPos-efcMD5, 50, efcMD5))
        pygame.draw.rect(display, hlp.button_colour, (765, bPos-efcSHA1, 50, efcSHA1))

        pygame.display.flip()
        # will not run more than 30 frames per second
        clock.tick(30)
    intro.Introduction2()

 