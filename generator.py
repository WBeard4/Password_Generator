# Password generator that generates passwords of 12 characters, using a real word of at least 8 characters, uppercase, lowercase, number and special character

import random
import pyperclip
import nltk # This is used to generate the random word

def generate_word():
    nltk.download('words')
    word_list = nltk.corpus.words.words()
    eight_letter_words = [word for word in word_list if len(word) == 8]
    random_word = random.choice(eight_letter_words)
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
    
    # Adding some randomization of the order that the password is formatted in
    password_format = random.randint(1, 3)
    if password_format == 1:
        password = word + number + special_char
    elif password_format == 2:
        password = word + special_char + number
    elif password_format == 3:
        password = number + word + special_char
    elif password_format == 4:
        password = number + special_char + word
    elif password_format == 5:
        password = special_char + word + number
    elif password_format == 6:
        password = special_char + number + word
        
    return password.strip().replace('\n', '')


password = generate_password()
pyperclip.copy(password)