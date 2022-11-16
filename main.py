from random import randint

from graphic_arts.start_game_banner import run_screensaver

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанес урон противнику равный {value_attack}'

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} ед. урона'

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (
        ' дерзкий воин ближнего боя. Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (
        ' находчивый воин дальнего боя. Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (
        ' могущественный заклинатель. Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'

# def attack(char_name: str, char_class: str) -> str:
#     """Вычисление нанесенного урона."""
#     if char_class == 'warrior':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(3, 5)}')
#     if char_class == 'mage':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(5, 10)}')
#     if char_class == 'healer':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(-3, -1)}')
#     return f'{char_name} не нанес урон'
#
#
# def defence(char_name: str, char_class: str) -> str:
#     """Вычисление заблокированного урона."""
#     if char_class == 'warrior':
#         return f'{char_name} блокировал {10 + randint(5, 10)} урона'
#     if char_class == 'mage':
#         return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
#     if char_class == 'healer':
#         return f'{char_name} блокировал {10 + randint(2, 5)} урона'
#     return f'{char_name} не блокировал урон'
#
#
# def special(char_name: str, char_class: str) -> str:
#     """Вычисление применения специального умения."""
#     if char_class == 'warrior':
#         return (f'{char_name} применил специальное умение '
#                 f'«Выносливость {80 + 25}»')
#     if char_class == 'mage':
#         return (f'{char_name} применил специальное умение '
#                 f'«Атака {5 + 40}»')
#     if char_class == 'healer':
#         return (f'{char_name} применил специальное умение '
#                 f'«Защита {10 + 30}»')
#     return f'{char_name} не применил специальное умение'
#
#
# def start_training(char_name: str, char_class: str) -> str:
#     """Тренирока управления персонажем."""
#     if char_class == 'warrior':
#         print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
#     if char_class == 'mage':
#         print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
#     if char_class == 'healer':
#         print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
#     print('Потренируйся управлять своими навыками.')
#     print('Введи одну из команд: attack — чтобы атаковать противника, '
#           'defence — чтобы блокировать атаку противника или '
#           'special — чтобы использовать свою суперсилу.')
#     print('Если не хочешь тренироваться, введи команду skip.')
#     cmd: str = None
#     while cmd != 'skip':
#         cmd = input('Введи команду: ')
#         if cmd == 'attack':
#             print(attack(char_name, char_class))
#         if cmd == 'defence':
#             print(defence(char_name, char_class))
#         if cmd == 'special':
#             print(special(char_name, char_class))
#     return 'Тренировка окончена.'
#
#
# def choice_char_class() -> str:
#     """Выбор класса персонажа."""
#     approve_choice: str = None
#     char_class: str = None
#     while approve_choice != 'y':
#         char_class = input(
#             'Введи название персонажа, за которого хочешь играть: '
#             'Воитель — warrior, Маг — mage, Лекарь — healer')
#         if char_class == 'warrior':
#             print('Воитель — дерзкий воин ближнего боя. '
#                   'Сильный, выносливый и отважный.')
#         if char_class == 'mage':
#             print('Маг — находчивый воин дальнего боя. '
#                   'Обладает высоким интеллектом.')
#         if char_class == 'healer':
#             print('Лекарь — могущественный заклинатель. '
#                   'Черпает силы из природы, веры и духов.')
#         approve_choice = input(
#             'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
#             'чтобы выбрать другого персонажа').lower()
#     return char_class
#
#
# if __name__ == '__main__':
#     run_screensaver()
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name: str = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class: str = choice_char_class()
#     print(start_training(char_name, char_class))
