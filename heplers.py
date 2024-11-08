from random import randint
from time import sleep
from data import *

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit = randint(1, 100)
            if crit < player['luck']:
                enemy_hp -= player['attack'] * 3
            else:
                enemy_hp -= player['attack']
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack'] * player['armor']
            sleep(1)
        print(f'''{player['name']}: {player['hp']}
{enemy['name']}: {enemy_hp}''')
        print()
        sleep(1)
        round += 1

    if player['hp'] > 0:
        player['money'] += current_enemy * randint(50, 150)
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player['hp'] = 100
    return current_enemy


def training(training_type):
    if 'Пропуск тренировки' in player['inventory']:
        player['inventory'].remove('Пропуск тренировки')
    else:
        for i in range(0, 101, 20):
            print(f'Тренировка завершена на {i}%')
            sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type == '2':
        player['armor'] -= .09
        print(f'Тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100}% урона')
    print()



def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Веилична атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')


def shop():
    print(f"Привет, {player['name']}! Добро пожаловать в мою скромную лавку!\nВыбери то, что хочешь купить:")
    for item in items:
        print(f"{item} - {items[item]['name']} ({items[item]['price']})")
    user_item = input("Выбери что хочешь купить: ")
    if user_item in items:
        if player['money'] >= items[user_item]['price']:
            player['inventory'].append(items[user_item]['name'])
            player['money'] -= items[user_item]['price']
            print(f"Вы купили {items[user_item]['name']}")
        else:
            print('У вас недостаточно монет!')
    else:
        print('Такого предмета нет!')
    print('Спасибо, что заглянул, приходи снова!')
    print()

    def inventory():
        print("Ваш инвентарь:")
    for item in player['inventory']:
        print(item)
    if 'Зелье удачи' in player['inventory']:
        ans = input('У вас есть Зелье удачи, желаете использовать?')
        if ans.lower() == 'да':
            player['luck'] += 5
            player['inventory'].remove('Зелье удачи')
            print(f"Теперь ваша удача повысилась! Шанс крит урона - {player['luck'] * 100}%")
    print()

