import random

while True:
    user_answer = input('How many pencils would you like to use:')
    if not user_answer.isnumeric():
        print('The number of pencils should be numeric')
    elif user_answer == '0':
        print('The number of pencils should be positive')
    else:
        break
user_answer = int(user_answer)
first_move = input('Who will be the first (Danil, Flea):')
names = {'Danil', 'Flea'}
while first_move not in names:
    print('Choose between Danil and Flea')
    first_move = input('Who will be the first (Danil, Flea):')
if first_move == 'Danil':
    second_move = 'Flea'
    count = 1
elif first_move == 'Flea':
    first_move = 'Danil'
    second_move = 'Flea'
    count = 0
num_pencils = {'1', '2', '3'}
while user_answer > 0:
    print('|' * user_answer)
    if count % 2 == 1:
        move = input(f"{first_move}'s turn:")
        if move not in num_pencils:
            print("Possible values: '1', '2' or '3'")
        elif move in num_pencils:
            if int(move) > user_answer:
                print('Too many pencils were taken')
            else:
                user_answer = user_answer - int(move)
                count += 1
                if user_answer == 0:
                    print(f'{second_move} won!')
    else:
        if user_answer % 4 == 0:
            move = 3
        elif user_answer % 4 == 3:
            move = 2
        elif user_answer % 4 == 2 or user_answer < 2:
            move = 1
        else:
            move = random.randint(1, 3)
        print(f"{second_move}'s turn:\n{move}")
        user_answer = user_answer - int(move)
        count += 1
        if user_answer == 0:
            print(f'{first_move} won!')
