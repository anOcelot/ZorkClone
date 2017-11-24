from GameObjects import *
from Game import Game
import re

#Front end class attaches controls game model
#according to text input from user.
class FrontEnd:

    #game look
    def run(self):
        self.game = Game()
        print ("Welcome to hawkins, Indiana.")
        #print(self.game.message)
        while self.game.player.isDead() == False:

            userInput = input("Give input: \n")
            self.parseInput(userInput)
            if self.game.map.toClear == 0:
                print ("You win")
                break

        if self.game.player.isDead():
            print ("Your life has been claimed by the upside down")

        else:
            print ("You have conquered the armies of the upside-down")

    def parseInput(self, userin):

        #pass move command to game
        if (userin.find("move") >= 0):
            print (self.game.move(userin))

        #attack command
        elif (userin.find("attack") >= 0):

            self.parseAttack()

        #look command
        elif (userin.find("look") >= 0):
            self.look()

        #equip command
        elif (userin.find("equip") >= 0):
            self.parseEquip()

        #print the map
        elif (userin.find("map") >= 0):
            self.map()

        #search command
        elif (userin.find("search") >= 0):
            self.parseSearch()

        #display status command
        elif (userin.find("status") >= 0):
            self.printStatus()

        #handled user error
        else:
            print("Unreadable input, mouth breather")


    #print player health and inventory as well as
    #the number of uncleared locations
    def printStatus(self):
        print ("Health: " + str(self.game.player.health))
        print ("Inventory: ")
        for thing in self.game.player.weapons:
            print(thing.name)
        print (str(self.game.map.toClear) + " locations left to clear")


    #searching a location reveals the available weapons
    def parseSearch(self):
        loc = self.game.map.getLocation(self.game.playerRow, self.game.playerCol)
        i = 0
        w = loc.weapons
        for thing in w:
            print (str(i) + " " + thing.name)
            i += 1
        print ("Do you want to pick anything up?")


        #allow the player to pick up a weapon
        try:
            num = int(input())
            self.game.player.pickup(w[num])
            print ("You picked up the " + w[num].name)
        except ValueError:
            print ("Okay")

    #equip a weapon from player inventory
    def parseEquip(self):
        i = 0
        print ("What do you want to equip?")
        stuff = self.game.player.weapons
        for thing in stuff:
            print (str(i) + " " + thing.name)
            i += 1

        num = int(input())
        self.game.player.equip(stuff[num])


    #target and attack a monster
    def parseAttack(self):
        print ("Which monster do you want to attack?")
        loc = self.game.look()
        i = 0
        m = loc.monsters
        for thing in m:
            print (str(i) + " " + thing.mType + " " + str(thing.health))
            i += 1

        try:
            num = int(input())
            name = m[num].mType
            h = m[num].health
            damageroll = self.game.player.attack(m[num])

            killed = False
            if damageroll >= h:
                killed = True
            print ("You did " + str(damageroll) + " damage to the " + name)

            if killed:
                print ("You killed the " + name)
        except ValueError:
            print ("Okay")

        #killed = False
        for thing in m:
            damageroll = thing.attack(self.game.player)
            print ("The " + thing.mType + " did " + str(damageroll) + " to you!")
            if self.game.player.isDead():
                print ("The Upside-Down devours the incompetent.")
                print ("You are dead.")
                break





        return 1

    def look(self):
        loc = self.game.map.getLocation(self.game.playerRow, self.game.playerCol)
        print ("You are in ", end="")
        print (loc.description)
        print ("You see ")
        for thing in loc.monsters:
            print (thing.mType + " " + str(thing.health))

    def map(self):
        m = self.game.map

        for r in range(0, 5):

            for c in range(0, 5):
                if r==self.game.playerRow and c==self.game.playerCol:
                    print (" [x] ", end="")

                elif self.game.map.getLocation(r, c).isClear() is False:
                    print (" [M] ", end= "")
                else: print (" [ ] ", end="")
            print("\n")



test = FrontEnd()
test.run()
