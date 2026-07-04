from random import randint


class Inventory:
    """
    Stores character items.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def __str__(self):
        return f"Inventory: {', '.join(self.items)}"


class Character:
    """
    Base Character Class
    """

    total_characters_created = 0

    def __init__(self, name, health, attack_power, defense):

        if not self.validate_number(health):
            raise ValueError("Invalid health")

        if not self.validate_number(attack_power):
            raise ValueError("Invalid attack")

        if not self.validate_number(defense):
            raise ValueError("Invalid defense")

        self._name = name
        self._health = health
        self._attack_power = attack_power
        self._defense = defense
        self._level = 1
        self._xp = 0

        self.inventory = Inventory()

        Character.total_characters_created += 1

    @staticmethod
    def validate_number(value):
        return value > 0

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    def attack(self, target):

        damage = max(
            self._attack_power - target._defense,
            1
        )

        target.take_damage(damage)

        print(
            f"{self._name} attacks "
            f"{target.name} "
            f"for {damage} damage!"
        )

    def take_damage(self, damage):

        self._health -= damage

        if self._health < 0:
            self._health = 0

    def is_alive(self):
        return self._health > 0

    def gain_xp(self, amount):

        self._xp += amount

        print(
            f"{self._name} gained "
            f"{amount} XP!"
        )

        while self._xp >= 100:

            self._xp -= 100
            self.level_up()

    def level_up(self):

        self._level += 1
        self._health += 20
        self._attack_power += 5
        self._defense += 3

        print(
            f"{self._name} reached "
            f"Level {self._level}!"
        )

    def __str__(self):

        return (
            f"{self.__class__.__name__}"
            f" | Name: {self._name}"
            f" | HP: {self._health}"
            f" | ATK: {self._attack_power}"
            f" | DEF: {self._defense}"
            f" | LVL: {self._level}"
        )

    def __repr__(self):

        return (
            f"{self.__class__.__name__}"
            f"('{self._name}', "
            f"{self._health}, "
            f"{self._attack_power}, "
            f"{self._defense})"
        )


class Warrior(Character):

    def shield_bash(self, target):

        damage = self._attack_power * 2

        target.take_damage(damage)

        print(
            f"{self._name} used "
            f"Shield Bash!"
        )

    def attack(self, target):

        damage = max(
            self._attack_power + 5
            - target._defense,
            1
        )

        target.take_damage(damage)

        print(
            f"{self._name} swings "
            f"a sword for "
            f"{damage} damage!"
        )


class Mage(Character):

    def __init__(
            self,
            name,
            health,
            attack_power,
            defense
    ):

        super().__init__(
            name,
            health,
            attack_power,
            defense
        )

        self.mana = 100

    def cast_spell(self, target):

        if self.mana < 20:

            print(
                "Not enough mana!"
            )

            return

        damage = self._attack_power * 3

        self.mana -= 20

        target.take_damage(damage)

        print(
            f"{self._name} casts "
            f"a spell for "
            f"{damage} damage!"
        )

    def attack(self, target):

        damage = max(
            self._attack_power + 2
            - target._defense,
            1
        )

        target.take_damage(damage)

        print(
            f"{self._name} uses "
            f"magic bolt!"
        )


class Archer(Character):

    def double_shot(self, target):

        damage = self._attack_power * 2

        target.take_damage(damage)

        print(
            f"{self._name} used "
            f"Double Shot!"
        )

    def attack(self, target):

        damage = max(
            self._attack_power + 3
            - target._defense,
            1
        )

        target.take_damage(damage)

        print(
            f"{self._name} shoots "
            f"an arrow!"
        )


class Monster:

    def __init__(
            self,
            name,
            health,
            attack_power,
            defense
    ):

        self._name = name
        self._health = health
        self._attack_power = attack_power
        self._defense = defense

    @property
    def name(self):
        return self._name

    def take_damage(self, damage):

        self._health -= damage

        if self._health < 0:
            self._health = 0

    def attack(self, target):

        damage = max(
            self._attack_power
            - target._defense,
            1
        )

        target.take_damage(damage)

        print(
            f"{self._name} attacks "
            f"for {damage} damage!"
        )

    def is_alive(self):
        return self._health > 0

    def __str__(self):

        return (
            f"Monster: "
            f"{self._name}"
            f" | HP: {self._health}"
        )


class BattleManager:

    @staticmethod
    def start_battle(
            hero,
            monster
    ):

        print("\nBattle Started!")

        while (
                hero.is_alive()
                and
                monster.is_alive()
        ):

            hero.attack(monster)

            if not monster.is_alive():

                print(
                    f"{monster.name} "
                    f"defeated!"
                )

                hero.gain_xp(100)

                return

            monster.attack(hero)

            print(
                f"{hero.name} HP:"
                f" {hero.health}"
            )

        print("Battle Ended")


heroes = []

while True:

    print("\n=== RPG MENU ===")
    print("1. Create Warrior")
    print("2. Create Mage")
    print("3. Create Archer")
    print("4. Show Characters")
    print("5. Add Inventory Item")
    print("6. Show Inventory")
    print("7. Start Battle")
    print("8. Statistics")
    print("0. Exit")

    choice = input("Choose: ")

    try:

        if choice == "1":

            name = input(
                "Name: "
            )

            hero = Warrior(
                name,
                120,
                20,
                10
            )

            heroes.append(hero)

            print(
                "Warrior Created!"
            )

        elif choice == "2":

            name = input(
                "Name: "
            )

            hero = Mage(
                name,
                80,
                25,
                5
            )

            heroes.append(hero)

            print(
                "Mage Created!"
            )

        elif choice == "3":

            name = input(
                "Name: "
            )

            hero = Archer(
                name,
                90,
                22,
                7
            )

            heroes.append(hero)

            print(
                "Archer Created!"
            )

        elif choice == "4":

            if not heroes:

                print(
                    "No characters."
                )

            else:

                for hero in heroes:
                    print(hero)

        elif choice == "5":

            name = input(
                "Character Name: "
            )

            item = input(
                "Item: "
            )

            for hero in heroes:

                if hero.name == name:

                    hero.inventory.add_item(
                        item
                    )

                    print(
                        "Item Added!"
                    )

        elif choice == "6":

            name = input(
                "Character Name: "
            )

            for hero in heroes:

                if hero.name == name:

                    print(
                        hero.inventory
                    )

        elif choice == "7":

            name = input(
                "Hero Name: "
            )

            hero = None

            for h in heroes:

                if h.name == name:
                    hero = h
                    break

            if not hero:

                print(
                    "Hero not found."
                )

                continue

            monster = Monster(
                "Goblin",
                randint(50, 100),
                randint(10, 20),
                randint(2, 5)
            )

            BattleManager.start_battle(
                hero,
                monster
            )

        elif choice == "8":

            print(
                "Total Characters:",
                Character.total_characters_created
            )

        elif choice == "0":

            print(
                "Goodbye!"
            )

            break

        else:

            print(
                "Invalid Option"
            )

    except ValueError as e:

        print(
            "Input Error:",
            e
        )

    except Exception as e:

        print(
            "Unexpected Error:",
            e
        )
