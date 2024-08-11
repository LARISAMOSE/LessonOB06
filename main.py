import random

# Класс Герой
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} на {damage} урона.")

    def is_alive(self):
        return self.health > 0

# Класс Игра
class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютерный враг")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if self.computer.is_alive():
                self.computer.attack(self.player)
            print(f"{self.player.name}: {self.player.health} здоровья осталось.")
            print(f"{self.computer.name}: {self.computer.health} здоровья осталось.")
            print("-" * 40)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден! {self.player.name} выиграл!")
            elif not self.player.is_alive():
                print(f"{self.player.name} побежден! {self.computer.name} выиграл!")
        print("Игра окончена.")

# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()

