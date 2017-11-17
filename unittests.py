import unittest
from GameObjects import *

class TestStringMethods(unittest.TestCase):

    def test_monsters(self):
        character = Character()
        zombie = Zombie()
        person = Person()
        vampire = Vampire()
        werewolf = Werewolf()
        self.assertEqual(character.mType, "Uninitialized")
        self.assertEqual(zombie.mType, "Zombie")
        self.assertEqual(person.mType, "Person")
        self.assertEqual(vampire.mType, "Vampire")
        self.assertEqual(werewolf.mType, "Werewolf")

    def test_combat(self):

        character = Character()
        zombie = Zombie()

        print(zombie.health)
        a = zombie.health
        b = character.health

        character.damage(20)
        zombie.damage(20)

        self.assertTrue(self, character.health < b)
        self.assertTrue(self, zombie.health < a)

        character = Character()
        zombie = Zombie()

        zombie.attack(character)
        character.attack(zombie)

        self.assertTrue(self, character.health < b)
        self.assertTrue(self, zombie.health < a)

        zombie.kill()
        character.kill()
        self.assertTrue(self, zombie.isDead() == True)
        self.assertTrue(self, character.isDead() == True)

    def test_locations(self):

        place = Location()

        self.assertTrue(len(place.monsters) in range(0, 6))

    def test_weapons(self):

        weapon = Weapon()
        self.assertTrue(self, weapon.attackMod == 0)
        self.assertTrue(self, weapon.name == "Trout")

        character = Character()
        character.equip(weapon)

        self.assertTrue(self, character.equipped.attackMod == 0)
        self.assertTrue(self, character.equipped.name == "Trout")

    def test_listening(self):

        house = Location()
        for m in house.monsters:
            self.assertTrue(self, len(m.observers) == 1)



    def test_gamestate(self):

        map = Map()

        for row in map.grid:

            for location in row:
                self.assertTrue(self, len(location.monsters) in range(0, 5))
                #print (location.description, location.monsters)






if __name__ == '__main__':
    unittest.main()