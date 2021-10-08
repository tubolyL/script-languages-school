import string
import random


def get_random_pwd(length, use_digit, use_punctuation):
    #password = ""
    available_characters = string.ascii_letters
    if use_digit:
        available_characters = available_characters + string.digits
    if use_punctuation:
        available_characters += string.punctuation

    #item_count = len(available_characters)

    #for _ in range(length):
        #index = random.randint(0, item_count - 1)
            ##VAGY
        #password = password + available_characters[index]
        #password += random.choice(available_characters)

    for _ in range(length):
        password = "".join(random.choice(available_characters) for _ in range(1, length))

    return password


if __name__ == "__main__":
    print(f"generated password: {get_random_pwd(6, True, True)}")
