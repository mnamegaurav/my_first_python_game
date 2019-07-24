from random import randint

# player details
player = {'name': '', 'attack': 10, 'heal': 20, 'health': 100}
player['name'] = input('Please enter your name : ')

# monster details
monster = {'name': 'anurag', 'attack_min': 10, 'attack_max': 20, 'health': 100}


def monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


def game_end(winner):
    print(f'{winner} Won The Game')


game_running = True

while game_running:
    if player['health'] <= 0:
        game_end(monster['name'])
        break
    elif monster['health'] <= 0:
        game_end(player['name'])
        break

    # Input choice
    print(player['name'], 'has', player['health'], 'health')
    print(monster['name'], 'has', monster['health'], 'health')
    choice = int(
        input('Please select your choice : \n 1)Attack\n 2)Heal\n 3)Quit\n'))

    # decision taking statements by user/player
    if choice == 1:
        monster['health'] = monster['health'] - player['attack']
        player['health'] = player['health'] - monster_attack()

    elif choice == 2:
        print('Healing the player...')
        player['health'] = player['health'] + player['heal']
        player['health'] = player['health'] - monster_attack()

    elif choice == 3:
        print(player['name'], 'has', player['health'], 'health')
        print(monster['name'], 'has', monster['health'], 'health')
        game_running = False

    else:
        print('Please enter the valid input')
