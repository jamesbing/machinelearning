#!/usr/bin/env python
# coding=utf-8
# this code block is used to practice the object and class concept in python.
from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
'''
class Engine(object):

    def __init__(self,scene_map):
        
    def play(self):
'''
class CentralCorridor(Scene):
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge , and blow the ship up after getting into an"
        print "escape pod."
        print "\n"

        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is floing and moving around his body, which throws"
            print "off you aim. Your laser hits his costume but misses him entirely. This"
            print "completely reins his brand new costume his mother bought him, which"
            print "makes him fly into a rage and blast you repeatedly in the face until"
            print "you are dead. Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "He eats you."
            return 'death'

        elif action == "tell a joke":
            print "You lucky guy!"
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print "you enterd laser room"
        print "you need to try to enter a digit number as password to get it."
        print "the password is 3 digits. you got 10 chances."
        code = "%d%d%d" % (randint(1,9),randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "you grab the neutron bomb and run as fast as you can to the "
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "you sucks. you decide to sit there and finally Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print "your burst onto the Bridge with the netron destruct bomb"
        print "what will you do now?"
        
        action = raw_input("> ")
        
        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Tothons"
            print "both of you been died"
            return 'death'

        elif action == 'slowly place the bomb':
            print "good job, Now that the bomb is placed you run to the escape pod to get off this tin can."
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print "You rush through the ship desperately trying to make it out."
        print "Now  there's 5 pods, which one do you take?"
        
        good_pod = randint(1,5)
        guess = raw_input("pod #> ")

        if int(guess) != good_pod:
            print "bad luck, you chosen a bad one."
            print "you die."
            return 'death'
        else:
            print "OK, you saved the world and you win!"

            return 'finished'

class Death():
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class Map(object):
    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death()
    }
    
    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Engine(object):
    
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n---------------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
