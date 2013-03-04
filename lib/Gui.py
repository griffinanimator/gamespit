#!/usr/bin/python
# -*- coding: utf8 -*-

# gamespit
# games platform for kids using Raspberry Pi
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 27/Feb/2013

import pygame
from pygame.locals import *
import time

class Display:
    '''
    Screen graphics and other media are embedded in this class
    '''
    def __init__(self,CONF):

        self.CONF=CONF
        self.width=int(CONF["width"])
        self.height=int(CONF["height"])
        self.centerx=self.width/2
        self.centery=self.height/2
        
# Pygame modules initialization. Avoid general initialization because in some hardware you have no sound'
        pygame.font.init()
        pygame.display.init()
        
        if CONF["full_screen"] == "True":
            self.screen=pygame.display.set_mode((self.width,self.height),pygame.FULLSCREEN)
        else:
            self.screen=pygame.display.set_mode((self.width,self.height))



# Clear the screen
    def clean(self,color):
        self.screen.fill(color)
        pygame.display.flip()

# Fill the screen
    def fill(self,color):
        self.screen.fill(color)

# Show changes in the screen
    def show(self):
        pygame.display.flip()

# Print an image and returns current screen content
    def print_image(self, image, x, y):
        current_content=pygame.Surface((image.get_width(),image.get_height()))
        current_content.blit(self.screen,(0,0),(x,y,image.get_width(),image.get_height()))
        self.screen.blit(image, (x,y))
        return current_content

# Print a text string
    def print_text(self, text, x, y, font, color):
        rtext = font.render(text, 1, color)
        self.screen.blit(rtext, (x,y))
        
# Draw a box with a frame
    def draw_box(self,coords,active):
        rectangle=pygame.Rect(coords)
        if active:
            self.screen.fill(self.decoration_color_active,rectangle)
            rectangle.inflate_ip(-15, -15)
            self.screen.fill(self.front_color_active,rectangle)
        else:
            self.screen.fill(self.decoration_color,rectangle)
            rectangle.inflate_ip(-15, -15)
            self.screen.fill(self.front_color,rectangle)

    
 

