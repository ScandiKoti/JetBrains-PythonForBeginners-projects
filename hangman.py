import random
import string

print('H A N G M A N')
win_result = 0
lost_result = 0
while True:
    game_words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(game_words)
    output_word = '-' * (len(word))
    word_letters = set(word)
    input_letters = set()
    count = 0
    main_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if main_input == "results":
        print(f'You won: {win_result} times.\nYou lost: {lost_result} times.')
    elif main_input == "exit":
        exit()
    else:
        while count < 8:
            print(f'\n{output_word}')
            user_input = input('Input a letter:')
            if len(user_input) != 1:
                print('Please, input a single letter.')
            elif user_input not in set(string.ascii_lowercase):
                print('Please, enter a lowercase letter from the English alphabet.')
            elif user_input in input_letters:
                print("You've already guessed this letter.")
            else:
                if user_input in word_letters:
                    input_letters.add(user_input)
                    output_word = ''.join([char if char in input_letters else '-' for char in word])
                    if output_word == word:
                        win_result += 1
                        print(f'You guessed the word {word}!\nYou survived!')
                        break
                elif user_input not in word_letters:
                    input_letters.add(user_input)
                    count += 1
                    print("That letter doesn't appear in the word.")
        if count == 8:
            lost_result += 1
            print('\nYou lost!')
