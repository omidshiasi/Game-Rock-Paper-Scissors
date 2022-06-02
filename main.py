import random


def get_input():
    input_user = input('Choice From s,k,g : ')
    if input_user in 'skg':
        return input_user
    else:
        print('choice from s or k or g .......')
        return get_input()


def win_game(user_in, system_in):
    if user_in == system_in:
        return 'Again Game'
    elif user_in == 's' and system_in == 'k':
        return 'Game Over'
    elif user_in == 'k' and system_in == 'g':
        return 'Game Over'
    elif user_in == 'g' and system_in == 's':
        return 'Game Over'
    else:
        return 'Win'


GAME_LIST = ['s', 'k', 'g']


def game():
    number_win = 0
    number_fail = 0
    try:
        number_game = int(input("Enter Number Game Set ? "))
        while number_game > 0:
            result = set_game()
            if 'Win' == result:
                number_win += 1
            elif 'Again Game' == result:
                number_game += 1
            else:
                number_fail += 1
            number_game -= 1
        if number_win > number_fail:
            print('&@'*10, ' You Win ', '&@'*10)
            print('\t', f"number win : {number_win}")
            print('\t', f'number fail : {number_fail}')
            print('&@'*10, ' You Win ', '&@'*10)
        else:
            print('!%' * 10, ' Game Over ', '!%'*10)
            print('\t', f" number win : {number_win}")
            print('\t', f'number fail : {number_fail}')
            print('!%' * 10, ' Game Over ', '!%'*10)
    except ValueError:
        print('Enter Set Is Number Please Try Again....')
        return game()


def set_game():
    input_user = get_input()
    input_tas = random.choice(GAME_LIST)
    print(f'input_user: {input_user}', f'input_system: {input_tas}\n', win_game(input_user, input_tas))
    return win_game(input_user, input_tas)


if __name__ == '__main__':
    game()
