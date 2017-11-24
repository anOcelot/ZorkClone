from random import *
from Observe import Observer, Observable


# Character objects
# health - health of the character
# attackVal - damage dealt when character attacks
# mType - type designation (could probably use core python for this)
# inventory - stores weapons
# equipped - currently equipped weapons
class Character(Observable):

    # constructor
    # attack - damage dealt when character attacks
    # health - character base health
    # mType - character type
    def __init__(self, attack=(10, 20), health=100, mType="Uninitialized"):
        Observable.__init__(self)
        self.__health = health

        # a tuple representing the range of damage an attack can do
        self.__attackVal = attack

        # type of character
        self.__mType = mType

        # inventory empty by default
        self.__inventory = []

        # description
        self.__description = "A festering wad of meat"
        # equipped with default weapon
        self.__equipped = Weapon()

    # inventory getter
    @property
    def inventory(self):
        return self.__inventory

    # inventory setter
    @inventory.setter
    def inventory(self, stuff):
        self.__inventory = stuff

    # inventory getter
    @property
    def equipped(self):
        return self.__equipped

    # inventory setter
    @equipped.setter
    def equipped(self, weapon):
        self.__equipped = weapon

    # description getter
    @property
    def description(self):
        return self.__description

    # description setter
    @description.setter
    def description(self, str):
        self.__description = str

    # mType getter
    @property
    def mType(self):
        return self.__mType

    # mType setter
    @mType.setter
    def mType(self, mType):
        self.__mType = mType

    # health getter
    @property
    def health(self):
        return self.__health

    # health setter
    @health.setter
    def health(self, health):
        self.__health = health

    # attackVal getter
    @property
    def attackVal(self):
        return self.__attackVal

    # attackVal setter
    @attackVal.setter
    def attackVal(self, attackVal):
        self.__attackVal = attackVal

    # equip the weapon designated by parameter weapon
    def equip(self, weapon):
        self.equipped = weapon

    # print stats (for debugging use)
    def printStats(self):
        print(self.mType)
        print("Health: %d" % self.health)
        print("Attack: %d" % self.attackVal)
        print("Observers: %s\n" % str(self.observers))

    # attack another character. damage inflicted is withing the range
    # indicated by attackVal
    # target - the character that the attack will damage
    def attack(self, target):
        damageRoll = randint(self.attackVal[0], self.attackVal[1])
        damageRoll = damageRoll * self.equipped.attackMod
        target.damage(damageRoll)
        return damageRoll

    # damage this character
    # damageRoll - the amount of damage done. 0 by default.
    def damage(self, damageRoll=0):
        self.health -= damageRoll
        if self.health <= 0:
            self.notify()

    # check if this character is dead
    def isDead(self):
        if self.health <= 0:
            return True
        else:
            return False

    # kill this character (for debugging)
    def kill(self):
        self.damage(10000)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    # Spawn a random monster. Used to populate neighborhoods/dungeons
    @staticmethod
    def spawnRandom():
        rn = randint(0, 4)
        spawnTable = {
            0: Person,
            1: Person,
            2: DemoDog,
            3: DemoDog,
            4: Beholder,
            5: Beholder,
            6: MindFlayer,
            7: Demogorgon,
        }
        return spawnTable[rn]()


# Person class. Does negative damage to heal player, has 100 health.
class Person(Character):
    def __init__(self):
        Character.__init__(self, (-30, -20), 100)
        self.mType = "Person"


# DemoDog. Does 0-10 damage and has 50-100 health.
class DemoDog(Character):
    def __init__(self):
        Character.__init__(self, (0, 10), randint(50, 100), "Demo-Dog")
        self.description = "A Demo-Dog bares it's thousand fangs"


# Beholder. Does 10-20 damage and has 100-150 health
class Beholder(Character):
    def __init__(self):
        Character.__init__(self, (10, 20), randint(100, 150), "Beholder")
        self.description = "A Beholder turns its eyes toward you"


# MindFlayer. Does 15-30 damage and has 150-200 health
class MindFlayer(Character):
    def __init__(self):
        Character.__init__(self, (15, 25), randint(150, 175), "MindFlayer")


# Demogorgon. Does 20-40 damage and has 200 health
class Demogorgon(Character):
    def __init__(self):
        Character.__init__(self, (20, 40), 200)
        self.mType = "Demogorgon"


# Player character. Does 30-40 damage and has 150 health
class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.health = randint(150, 150)
        self.attackVal = (30, 40)
        self.weapons = []

    # pickup a weapon
    def pickup(self, w):
        self.weapons.append(w)


# Map locations. Locations observe characters, the Map observes locations
# monsters - a list of the monsters occupyting a location
# description - a description of the location
# weapons - a list of the items in a location
class Location(Observer, Observable):
    def __init__(self):

        Observable.__init__(self)
        Observer.__init__(self)

        self.__monsters = []
        self.__weapons = Weapon.spawnSet()
        self.__description = Location.__randomDescription()

        # spawn a random number of monsters in the location
        for num in range(0, randint(0, 3)):
            currentSpawn = Character.spawnRandom()
            currentSpawn.attach(self)
            self.monsters.append(currentSpawn)

    # monsters getter
    @property
    def monsters(self):
        return self.__monsters

    # monsters setter
    @property
    def weapons(self):
        return self.__weapons

    # description getter
    @property
    def description(self):
        return self.__description

    # description setter
    @description.setter
    def description(self, description):
        self.__description = description

    # generate a random description
    @staticmethod
    def __randomDescription():
        rn = randint(0, 4)
        descriptionTable = {
            0: "a gaudy white house with fake columns on the porch.",
            1: "a graveyard",
            2: "a small ranch house. The lights are flickering.",
            3: "a musty old farm house, filled with cats. The wallpaper seems to ripple",
            4: "an orange brick school."
        }
        return descriptionTable[rn]

    # monsters will notify the location when they die
    def update(self, monster):
        self.monsters.remove(monster)

        # location notifies its observers when it is clear
        if self.isClear():
            self.notify()

    # notify all observers
    # def notify(self):
    #  for observer in self.observers:
    #        observer.update()

    # remove a weapon to represent it being picked up by the character
    def pickup(self, w):
        self.weapons.remove(w)

    # returns true if location is clear of monsters (no monsters or all dead)
    def isClear(self):

        for thing in self.monsters:

            # People are not considered monsters
            if thing.mType not in ("Person"):
                return False
        return True


# Weapon class
# name - weapon name
# attackmod - attack multiplier
class Weapon():
    def __init__(self, name="Rock", attackMod=1):
        self.__name = name
        self.__attackMod = attackMod

    # attackMod getter
    @property
    def attackMod(self):
        return self.__attackMod

    # attackMod setter
    @attackMod.setter
    def attackMod(self, attackMod):
        self.__attackMod = attackMod

    # attackMod getter
    @property
    def name(self):
        return self.__name

    # attackMod setter
    @name.setter
    def name(self, name):
        self.__name = name

    # print weapon stats - for debugging
    def printStats(self):
        print(self.name)
        print("Attack modifier: %s\n" % self.attackMod)

    # spawn a random weapon. Used to populate locations
    # returns a random weapon
    @staticmethod
    def spawnRandom():
        rn = randint(0, 5)
        spawnTable = {
            0: Bat,
            1: Slingshot,
            2: Hairspray,
            3: Gun,
            4: Chainsaw,
            5: Speargun,
        }

        return spawnTable[rn]()

    # spawn a random list of weapon. Used to populate locations
    # returns a list of random weapons
    @staticmethod
    def spawnSet():
        set = []
        for num in range(0, randint(0, 5)):
            currentSpawn = Weapon.spawnRandom()
            set.append(currentSpawn)
        return (set)


# Bat
class Bat(Weapon):
    def __init__(self):
        Weapon.__init__(self, "bat", 3.5)


# Slingshot
class Slingshot(Weapon):
    def __init__(self):
        Weapon.__init__(self, "slingshot", 2.5)


# Hairspray
class Hairspray(Weapon):
    def __init__(self):
        Weapon.__init__(self, "hairspray flamethrower", 2)

# Gun
class Gun(Weapon):
    def __init__(self):
        Weapon.__init__(self, "revolver", 3)

# Chainsaw
class Chainsaw(Weapon):
    def __init__(self):
        Weapon.__init__(self, "chainsaw", 4.5)

class Speargun(Weapon):
    def __init__(self):
        Weapon.__init__(self, "speargun", 4)



# Map class handles game map.
# Map is a 5x5 grid of locations populated with monsters;
# the 5 x 5 dimensions are hard coded, but could easily be
# determined by parameters.
class Map(Observer):

    def __init__(self):

        self.__grid = []

        #number of houses still containing monsters
        self.__toClear = 25
        for row in range(0, 5):
            currentRow = []
            for col in range(0, 5):
                next = Location()
                currentRow.append(next)
                next.attach(self)
                if next.isClear():

                    #as the map is assembled, each location uses notify
                    #to update the toClear var
                    next.notify()
            self.__grid.append(currentRow)

    #toClear getter
    @property
    def toClear(self):
        return self.__toClear

    #toClear setter
    @toClear.setter
    def toClear(self, val):
        self.__toClear = val

    #grid getter
    @property
    def grid(self):
        return self.__grid

    #grid setter
    @grid.setter
    def grid(self, g):
        self.__grid = g


    #decrement toClear whenever a location is clear
    def update(self):
        self.toClear -= 1

    #return the location at a a designated row and col
    def getLocation(self, row, col):
        return self.__grid[row][col]
