from random import *


class Monster:
    def __init__(self, attack=0, health=0, mType="Demogorgon"):
        self.health = health
        self.attack = attack
        self.mType = mType

    def printStats(self):
        print (self.mType)
        print ("Health: %d" % self.health)
        print ("Attack: %d\n" % self.attack)

    @staticmethod
    def spawnRandom():
        rn = randint(0, 4)
        spawnTable = {
            0: Person,
            1: Zombie,
            2: Vampire,
            3: Ghoul,
            4: Werewolf,
        }
        return spawnTable[rn]()


class Person(Monster):
    def __init__(self):
        Monster.__init__(self, -20, 100)
        self.mType = "Person"


class Zombie(Monster):
    def __init__(self):
        Monster.__init__(self, randint(0, 10), randint(50, 100))
        self.mType = "Zombie"


class Vampire(Monster):
    def __init__(self):
        Monster.__init__(self, randint(10, 20), randint(100, 200))
        self.mType = "Vampire"


class Ghoul(Monster):
    def __init__(self):
        Monster.__init__(self, randint(15, 30), randint(40, 80))
        self.mType = "Ghoul"


class Werewolf(Monster):
    def __init__(self):
        Monster.__init__(self, randint(0, 40), 200)
        self.mType = "Werewolf"


class Location():
    def __init__(self):
        self.Monsters = []
        self.description = Location.__randomDescription()
        for num in range(0, 5):
            self.Monsters.append(Monster.spawnRandom())

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


class player():
    def __init__(self):
        self.health = 100
        self.weapons = []


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


# class sourStraw(Weapon):

# class chocolateBar(Weapon):

# class nerdBomb(Weapon):

gameMap = []
for num in range(0, 5):
    row = []
    print ("")
    for num in range(0, 5):
        row.append(Location())

    gameMap.append(row)

for thing in gameMap:
    print ("")
    for house in thing:
        print (" ", house.description, end="")
        # print (house.Monsters)

        for num in range(0, 5):
            current = Monster.spawnRandom()
            # current.printStats()
