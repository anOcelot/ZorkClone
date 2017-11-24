from GameObjects import *
import Observe

#Game class builds a game from game objects,
#and manages gamestate and control.
class Game(Observer, Observable):


    #constructor
    def __init__(self):
        # print ("=================================================")
        # print ("  ____   _____" )
        # print (" / __ ' '_, ,_'")
        # print ("/ ,       | |")
        # print ("\\ \\")
        #initial message
        self.message = "Welcome to Hawkins, Indiana"

        #player character
        self.__player = Player()

        #player location
        self.__playerRow = 0
        self.__playerCol = 0

        #game map
        self.map = Map()
        #map.attach(self)


    #map getter
    @property
    def map(self):
        return self.__map

    #map setter
    @map.setter
    def map(self, m):
        self.__map = m

    #player getter
    @property
    def player(self):
        return self.__player

    #row getter
    @property
    def playerRow(self):
        return self.__playerRow

    #row setter
    @playerRow.setter
    def playerRow(self, row):
        self.__playerRow = row

    #column getter
    @property
    def playerCol(self):
        return self.__playerCol

    #column setter
    @playerCol.setter
    def playerCol(self, col):
        self.__playerCol = col

    #move functions determines player command from user input
    def move(self, str):

        #determine direction
        n = str.find("north") != -1
        s = str.find("south") != -1
        e = str.find("east") != -1
        w = str.find("west") != -1
        nw = (n and w)
        sw = (s and w)
        ne = (n and e)
        se = (s and e)

        #keep original location around in case it is necessary to revert
        original = (self.playerRow, self.playerCol)

        #move
        if (nw):

            self.playerRow -= 1
            self.playerCol -= 1

            out = "You travel northwest"


        elif (sw):

            self.playerRow += 1
            self.playerCol -= 1

            out = "You travel southwest"


        elif (ne):

            self.playerRow -= 1
            self.playerCol += 1

            out = "You travel northeast"


        elif (se):

            self.playerRow += 1
            self.playerCol += 1

            out = "You travel southeast"

        elif (n):

            self.playerRow -= 1

            out = "You travel north"

        elif (s):

            self.playerRow += 1

            out = "You travel south"

        elif (e):

            self.playerCol += 1

            out = "You travel east"

        elif (w):

            self.playerCol -= 1
            out = "You travel west"

        else:
           out = "Move where, though"

        #if move is invalid, revert to original position
        if (self.checkBorders() == False):
            self.playerRow = original[0]
            self.playerCol = original[1]
            return ("You cannot go that way")

        return out



    #check that the player is within the border of the map
    def checkBorders(self):

        if (self.playerRow > 4):
            self.playerRow -= 1
            return False

        if (self.playerRow < 0):

            self.playerRow += 1
            return  False

        if (self.playerCol > 4):
            self.playerCol -= 1
            return False

        if (self.playerCol < 0):
            self.playerCol += 1
            return False

        return  True


    #pickup a weapon
    def pickup(self, w):
        self.player.pickup(w)


    #look action returns game location
    def look(self):
        loc = self.map.getLocation(self.playerRow, self.playerCol)
        return (loc)


    def update(self, msg):
        self.message = msg