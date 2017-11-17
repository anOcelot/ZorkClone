from random import *
from abc import ABC
from Observe import Observer, Observable
from GameObjects import *


class Location(Observer, Observable):

    def __init__(self):
        self.monsters = []
        self.description = Location.__randomDescription()
        for num in range(0, randint(0, 5)):
            currentSpawn = Character.spawnRandom()
            currentSpawn.attach(self)
            self.monsters.append(currentSpawn)


    @staticmethod
    def __randomDescription():
        rn = randint(0, 4)
        descriptionTable = {
            0: "red house",
            1: "blue house",
            2: "green house",
            3: "yellow house",
            4: "white house"
        }
        return descriptionTable[rn]

    def update(self, monster):
        self.monsters.remove(Character)

class Controllable:

    def __init__(self):
        self.x = 0
        self.y = 0


    def move(self, direction):

        if (direction == "north"):
            self.y += 1
        elif (direction == "south"):
            self.y -= 1
        elif (direction == "east"):
            self.x += 1
        elif (direction == "west"):
            self.x -= 1







class Weapon():
    def __init__(self, name="Trout", attackMod=0):
        self.name = name
        self.attackMod = attackMod

    def printStats(self):
        print (self.name)
        print ("Attack modified: %s\n" % self.attackMod)

    @staticmethod
    def spawnRandom():
        rn = randint(0, 3)
        spawnTable = {
            0: hersheyKiss,
            1: sourStraw,
            2: cholateBar,
            3: nerdBomb
        }

        return spawnTable[rn]()


class hersheyKiss(Weapon):
    def __init__(self):
        Weapon.__init__(self, "HersheyKiss", 1)




