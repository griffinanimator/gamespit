#!/usr/bin/python
# -*- coding: utf8 -*-

# gamespit
# games platform for kids using Raspberry Pi
# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 27/Feb/2013

import pygame
import os

class Game:    
    '''
    This class makes coding easier, as you don't need to read any files to 
    use graphics or sounds. Drop them in your game directory and they will
    be automatically loaded into your game object.

    Just use Game.images["one_of_your_images_without_extension"] whenever you
    need to access one of your pygame images.

    Sounds work in a similar way (Game.sounds["one_name"]).

    Fonts are pre-rendered in many sizes, depending on your game config file.
    Use Game.fonts["one_name-one_size"] whenever you want to print text strings.
    '''
    def __init__(self,CONF,DISPLAY,CONTROLLER):
        self.CONF=CONF
        self.DISPLAY=DISPLAY
        self.CONTROLLER=CONTROLLER
        self.IMAGES={}
        self.SOUNDS={} 
        self.FONTS={} 
        self.COLORS={}

        self.convert_colors(CONF["COLORS"])

# Automagically load files into python objects (inspired on the "on rails" way)
        self.autoload_images(os.path.join(self.CONF["GAME"]["base_path"],"images"))
        self.autoload_sounds(os.path.join(self.CONF["GAME"]["base_path"],"sounds"))
        self.autoload_fonts(os.path.join(self.CONF["GAME"]["base_path"],"fonts"),CONF["GAME"]["font_sizes"])


        if CONF["GAME"]["mouse"] == "True":
            pygame.mouse.set_visible(1)
        else:
            pygame.mouse.set_visible(0)

        self.clean()

# Convert named or numeric colors to pygame colors
    def convert_colors(self, colors):
        for name, value in colors.iteritems():
            print name,value
            if len(value) == 3:
                rgb=map(int,value)
                self.COLORS[name]=pygame.color.Color(rgb[0],rgb[1],rgb[2])
            else:
                self.COLORS[name]=pygame.color.Color(value)

# Load every image in images folder
    def autoload_images(self, dir_name):
        print "Searching for images in", dir_name
        if os.path.isdir(dir_name):
            file_list=os.listdir(dir_name)
            for file in file_list:
                name=os.path.splitext(file)[0]
                print " found", name
                self.IMAGES[name]=pygame.image.load(os.path.join(dir_name,file))
            return

# Load every sound in sounds folder
    def autoload_sounds(self, dir_name):
        if os.path.isdir(dir_name):
            file_list=os.listdir(dir_name)
            for file in file_list:
                name=os.path.splitext(file)[0]
                self.SOUNDS[name]=pygame.mixer.Sound(os.path.join(dir_name,file))
            return

# Load every font in fonts folder 
    def autoload_fonts(self, dir_name, sizes):
        print "Searching for fonts in", dir_name
        if os.path.isdir(dir_name):
            file_list=os.listdir(dir_name)
            for file in file_list:
                name=os.path.splitext(file)[0]
                print " found", name
                for s in sizes:
                  print "  generating", name+s
                  self.FONTS[name+s]=pygame.font.Font(os.path.join(dir_name,file),int(s))
            return


    def clean(self):
      self.DISPLAY.clean(self.COLORS["background"])
      return
    def fill(self):
      self.DISPLAY.fill(self.COLORS["background"])
      return

    def wait(self,ms):
      pygame.time.wait(ms)
      return

