# CHRIS NELSON
# EMYRS OBJECT DB
# NHC 2018
# CLASS MODULE

import functions as f
import persistent

#########################################################################
### !!!! CHANGES TO THIS FILE REQUIRE INITIALISE DB TO BE RE_RUN !!!! ###
### !!!!          THIS WILL DELETE ANY EXISTING DATABASE         !!!! ###
#########################################################################

#################
#### classes ####
##### lvl 0 #####

class Organiser(persistent.Persistent):
    def __init__(self):
        self.latest_key = 0 # database starts empty - increase this otherwise

class Root(persistent.Persistent):
    level = 0
    def __init__(self):
        self.___________________GENERAL___________________ = ""
        self.name = ""
        self.links = ""
        self.magic = False
        self.notes = ""
        self.location = ""
        self.group = f.gclass_info(0, self)
        self.parent = f.gclass_info(1, self)

##### lvl 1 #####

class Actor(Root):
    level = 1
    def __init__(self):
        super().__init__()
        #personal
        self.__________________PERSONAL__________________ = ""
        self.race = ""
        self.age = 0
        self.classtype = ""
        self.lvl = 0
        self.background = ""
        self.allignment = "neutral"
        #mainattributes
        self._____________MAIN_ATTRIBUTES______________ = ""
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.____________________HEALTH___________________ = ""
        self.hp = 0
        self.hp_max = 0
        self.hp_tmp = 0
        self.armourclass = 0
        self.speed = 0
        self.initiative = 0
        self.resistance = ""
        self.immunity = ""
        self.savingthrows = 0
        self._____________________ABILITY___________________ = ""
        self.actions = ""
        self.skills = ""
        self.senses = ""
        self.passive_perception = 0
        self.language = ""
        self.challenge = 0
        self.proficiencies = ""
        self._________________CONDITIONS__________________ = ""
        self.blinded = False
        self.charmed = False
        self.deafened = False
        self.frightened = False
        self.grappled = False
        self.incapacitated = False
        self.invisible = False
        self.paralyzed = False
        self.pretrified = False
        self.poisoned = False
        self.prone = False
        self.restrained = False
        self.stunned = False
        self.unconscious = False

class Item(Root):
    level = 1
    def __init__(self):
        super().__init__()
        self.description = ""
        self.tally = 0
        self.cost = 0
        self.weight = 0
        self.broken = False

class Action(Root):
    level = 1
    def __init__(self):
        super().__init__()
        self.aggressive = False

class Place(Root):
    level = 1
    def __init__(self):
        super().__init__()
        self.terrain = ""

##### lvl 2 #####

class Building(Place):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

class Location(Place):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

class Lodging(Place):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

class Player(Actor):
    level = 2
    def __init__(self):
        super().__init__()
        #skills
        self.______________________SKILLS____________________ = ""
        self.acrobatics = 0
        self.animalhandling = 0
        self.arcana = 0
        self.athletics = 0
        self.deception = 0
        self.history = 0
        self.insight = 0
        self.intimidation = 0
        self.invesitgation = 0
        self.medicine = 0
        self.nature = 0
        self.perception = 0
        self.performance = 0
        self.persuasion = 0
        self.religion = 0
        self.sleightofhand = 0
        self.stealth = 0
        self.survival = 0
        self.spellslots = 0
        self.spellbook = ""
        self.spellprepared = ""
        #social
        self.____________________SOCIAL____________________ = ""
        self.traits = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""
        #inventory
        self.__________________INVENTORY__________________ = ""
        self.equipment = ""
        self.armour = ""
        self.shields = ""
        self.weapons = ""
        #dice
        self.______________________DICE_____________________ = ""
        self.hitdice = 0
        self.inspiration = 0
        self.prof_bonus = 0
        self.deathsaves = 0
        #additional
        self.___________________ADDITIONAL__________________ = ""


class NonPlayer(Actor):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

class Monster(Actor):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

class Animal(Actor):
    level = 2
    def __init__(self):
        super().__init__()
        self.pet = False
        self.mount = False
        self.___________________ADDITIONAL__________________ = ""


class Armour(Item):
    level = 2
    def __init__(self):
        super().__init__()
        self.armourclass = 0
        self.___________________ADDITIONAL__________________ = ""

class Weapon(Item):
    level = 2
    def __init__(self):
        super().__init__()
        self.damage = 0
        self.___________________ADDITIONAL__________________ = ""

class Gear(Item):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

class Food(Item):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

class Magic(Item):
    level = 2
    def __init__(self):
        super().__init__()
        self.magic = True
        self.___________________ADDITIONAL__________________ = ""

class Spell(Action):
    level = 2
    def __init__(self):
        super().__init__()
        self.cast_time = 0
        self.range = 0
        self.components = ""
        self.duration = 0
        self.effect = ""
        self.___________________ADDITIONAL__________________ = ""

class Skill(Action):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

class Quest(Action):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

class Encounter(Action):
    level = 2
    def __init__(self):
        super().__init__()
        self.___________________ADDITIONAL__________________ = ""

#### end of classes ####
########################
