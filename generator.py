# Password generator that generates passwords of 12 characters, using a real word of at least 8 characters, uppercase, lowercase, number and special character

from random_word import RandomWords
import random

def generate_word():
    r = RandomWords()
    with open('words.txt', 'r') as words:
        lines = words.readlines()
    random_word = ()
    while len(random_word) != 8:
        random_word = random.choice(lines)
    return random_word


def generate_special_characters():
    special_characters = ['!', '"', "'", ',', '@']
    special_character_one = random.choice(special_characters)
    special_character_two = random.choice(special_characters)
    return special_character_one + special_character_two

def generate_numbers():
    random_number = random.randint(10, 99)
    return str(random_number)

def generate_password():
    word = generate_word()
    word = word.title()
    special_char = generate_special_characters()
    number = generate_numbers()
    password = word + number + special_char
    return password.strip().replace('\n', '')


print(generate_password())
