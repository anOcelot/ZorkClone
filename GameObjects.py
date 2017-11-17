from random import *
from Observe import Observer, Observable

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


class Character(Observable):

    def __init__(self, attack=10, health=100, mType="Uninitialized"):
        Observable.__init__(self)
        self.__health = health
        self.__attackVal = attack
        self.__mType = mType
        self.__inventory = []
        self.equipped = 0


    @property
    def mType(self):
        return self.__mType

    @mType.setter
    def mType(self, mType):
        self.__mType = mType

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def attackVal(self):
        return self.__attackVal

    @attackVal.setter
    def attackVal(self, attackVal):
        self.__attackVal = attackVal


    def equip(self, weapon):
        self.equipped = weapon

    def printStats(self):
        print (self.mType)
        print ("Health: %d" % self.health)
        print ("Attack: %d" % self.attackVal)
        print("Observers: %s\n" % str(self.observers))


    def attack(self, target):
        target.damage(self.attackVal)

    def damage(self, damageRoll=-1000):
        self.health -= damageRoll

    def isDead(self):
        if self.health <= 0:
            return True
        else: return False

    def kill(self):
        self.health -= 1000
        
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

class Location(Observer, Observable):

    def __init__(self):
        Observable.__init__(self)
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

class Weapon():

    def __init__(self, name="Trout", attackMod=0):
        self.__name = name
        self.__attackMod = attackMod


    @property
    def attackMod(self):
        return self.__attackMod

    @attackMod.setter
    def attackMod(self, attackMod):
        self.__attackMod = attackMod

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def printStats(self):
        print (self.name)
        print ("Attack modifier: %s\n" % self.attackMod)

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



class Person(Character):
    def __init__(self):
        Character.__init__(self, -20, 100)
        self.mType = "Person"


class Zombie(Character):
    def __init__(self):
        Character.__init__(self, randint(0, 10), randint(50, 100), "Zombie")



class Vampire(Character):
    def __init__(self):
        Character.__init__(self, randint(10, 20), randint(100, 200))
        self.mType = "Vampire"


class Ghoul(Character):
    def __init__(self):
        Character.__init__(self, randint(15, 30), randint(40, 80))
        self.mType = "Ghoul"


class Werewolf(Character):
    def __init__(self):
        Character.__init__(self, randint(0, 40), 200)
        self.mType = "Werewolf"


class Party(Character, Controllable):
    def __init__(self):
        Character.__init__(self)
        self.x = 0
        self.y = 0
        self.health = randint(100, 125)
        self.attack = randint(10, 20)
        self.weapons = []


class hersheyKiss(Weapon):
    def __init__(self):
        Weapon.__init__(self, "HersheyKiss", 1)


class Map(Observer):

    def __init__(self):
        self.grid = []
        self.toClear = 25
        for row in range(0, 4):
            currentRow = []
            for col in range(0, 4):
                next = Location()
                currentRow.append(next)
                next.attach(self)
            self.grid.append(currentRow)

    def update(self, location):
        self.toClear -= 1







