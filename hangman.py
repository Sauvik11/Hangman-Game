import random
from word_list import words
import string

def select_valid_word(words):
    word= random.choice(words)
    while '-' in word or ' ' in word :
        word = random.choice(words)
    return word

def hangman():
    word= select_valid_word(words)
    word_letters = set(word)
    alphabet= set(string.ascii_uppercase)
    print ("alpha", alphabet)
    used_letters= set()
    print("word lettes", word_letters)

    while len(word_letters) > 0 :
        print("Letters used till now " ,str(used_letters))
        word_used_list=[letter if letter in used_letters else "-" for letter in word ]
        print("word used list: ", word_used_list)
        print ("current word:", " ".join(word_used_list) )


        user_letter = input("Guess a letter : ")
        print("used_letters: ", used_letters)
        print("######## ", alphabet - used_letters)
        if user_letter.upper() in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters= word_letters -set(user_letter)

        elif user_letter in used_letters:
            print(" you have already guessed that letter! please try again.")
        else:
            print("Invalid character , please try again")


hangman()






