from enum import Enum
from blessed import Terminal
import random

term = Terminal()

class BattleResult(Enum):
    HIT = 1
    MISS = 2
    BLOCK = 3
    DODGE = 4

class Stats:
    def __init__(self, attack, defense, dexterity, evasion):
        self.attack = attack
        self.defense = defense
        self.dexterity = dexterity
        self.evasion = evasion

class Item:
    def __init__(self, name, stats, health = 0):
        self.name = name
        self.health = health
        self.stats = stats

class Entity:
    def __init__(self, name, level, health, stats):
        self.name = name
        self.level = level
        self.health = health
        self.stats = stats        
        self.is_guarding = False

    def load(self, entity):
        self.name = entity.name
        self.level = entity.level
        self.health = entity.health
        self.stats = entity.stats

    def attack(self, other):
        # Attacking compares self's dexterity vs other's evasion
        print(term.green(f"{self.name} is attempting to attack {other.name}"))
        total_dex_evasion = self.stats.dexterity + other.stats.evasion

        # If random() returns a value within the attack range we attack. Otherwise it's a miss.
        if random.random() <= self.stats.dexterity / total_dex_evasion:
            damage = self.stats.attack
            # A target that is guarding only takes the amount of incoming damage minus their defense
            if (other.is_guarding):
                print(term.green(f"{other.name} is guarding."))
                damage = max(0, damage - other.stats.defense)
            other.add_health(-damage)
            print(term.green(f"{self.name} hit {other.name} for {damage} damage."))
            print(term.green(f"{other.name} has {other.health} HP left."))
            return BattleResult.HIT
        else:
            print(f"{self.name} missed.")
            return BattleResult.MISS 

    def guard(self):
        self.is_guarding = True
        print(term.green(f"{self.name} braces for impact."))
    
    def flee(self, other):
        print(term.green(f"{self.name} is attempting to flee."))
        total_evasion = self.stats.evasion + other.stats.evasion
        if random.random() <= self.stats.evasion / total_evasion:
            return True
        else:
            return False

    # Might remove this since guarding is passive
    def defend(self, other):
        total_dex_evasion = self.stats.evasion + other.stats.dexterity
        if random.random() <= self.stats.evasion / total_dex_evasion:
            return BattleResult.DODGE
        else:
            return BattleResult.HIT 

    def add_health(self, amount):
        self.health = max(0, self.health + amount)

class Player(Entity):
    def __init__(self, name = "Protag", level = 1, health = 10, stats = Stats(5, 5, 5, 5)):
        super().__init__(name, level, health, stats)
        self.equipped = {"weapon": None, "armor": None, "shield": None}
        self.inventory = [(Item("Potion", Stats(0,0,0,0), 10))]

    def load(self, player):
        super().load(player)
        self.equipped = player.equipped
        self.inventory = player.inventory