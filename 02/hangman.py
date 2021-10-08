import logging
from typing import List


def get_all_index(text: str, word: str) -> List[int]:
    if type(text) != str:
        raise TypeError
    if len(text) != 1:
        raise ValueError
    #return [i for i, ltr in enumerate(word) if letter == text]
    found_index = []
    for i in range(len(word)):
        if word[i] == text:
            found_index.append(i)
    return found_index


def get_new_masked_word(masked_word: str, word: str, indexes: List[int]) -> str:
    new_masked_word_list = list(masked_word)

    for step in range(len(word)):
        if step in indexes:
            new_masked_word_list[step] = word[step]

    return "".join(new_masked_word_list)


def lost() -> None:
    print("sorry, u lost")
    exit(1)


def won() -> None:
    print("u won")
    exit(0)


def new_guess(guess: str, word: str, masked_word: str) -> str:
    index_list = get_all_index(guess, word)
    masked_word = get_new_masked_word(masked_word, word, index_list)

    return masked_word


def handle_final_guess(text: str, word: str) -> None:
    if text == word:
        if text == word:
            won()
        else:
            lost()


if __name__ == "__main__":
    logging.basicConfig(filename='hangman.log', filemode='w', level=logging.DEBUG)
    LOGGER = logging.getLogger()
    LOGGER.debug('Debug')
    LOGGER.info('Info')
    LOGGER.warning('Warning')

    MAX_GUESS = 3
    print(f"Hangman Application{MAX_GUESS}")
    word = "hello"

    masked_word = len(word)*"x"

    #print(get_new_masked_word(masked_word, word, get_all_index("l", word=word)))

    for guess in range(MAX_GUESS):
        print(f"{guess+1}. chance, give me letter:")
        text = input()

        is_new_guess = len(text) == 1
        if is_new_guess:
            masked_word = new_guess(text, word, masked_word)
            print(masked_word)
            if masked_word == word:
                won()
        else:
            handle_final_guess(text, word)
    lost()
