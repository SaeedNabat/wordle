import contextlib

from wyrdl import guess_word,get_random_word, show_guesses, refresh_page, game_over
import pathlib

NUM_LETTERS = 5
NUM_GUESSES = 6
WORD_PATH = pathlib.Path(__file__).parent / 'wordlist.txt'


def main():
    word = get_random_word(WORD_PATH.read_text(encoding='utf-8').split('\n'))
    guesses = ['_' * NUM_LETTERS] * NUM_GUESSES
    with contextlib.suppress(KeyboardInterrupt):
        for idx in range(NUM_GUESSES):
            refresh_page(headline=f'Guess {idx + 1}')
            show_guesses(guesses, word)

            guesses[idx] = guess_word(previous_guesses=guesses[:idx])
            if guesses[idx] == word:
                break
        game_over(guesses, word, guessed_correctly=guesses[idx] == word)


if __name__ == '__main__':
    main()
