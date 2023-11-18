import random
from words import words_list
from art import stages


counts = 5
number_of_try = 0

chosen_word = random.choice(words_list)


display = []
for i in range(len(chosen_word)):
    display += '-'
print(display)

end_of_game = False
while not end_of_game:
    guess = input('guess a letter: ').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            number_of_try += 1
    print(display)

    if guess not in chosen_word:
        print(f'"{guess}" is not in the word')
        counts -= 1
        print(f'you have {counts} chance')
        if counts == 0:
            end_of_game = True
            print('you lost')
    if '-' not in display:
        end_of_game = True
        print(f'you won after {number_of_try} try')


    print(stages[counts])






