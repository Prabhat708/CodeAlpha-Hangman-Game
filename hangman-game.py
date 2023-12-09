import random
import tkinter as tk

# List of words for the game
words = [
    "apple", "banana", "orange", "grape", "strawberry", "watermelon",
    "pineapple", "mango", "blueberry", "kiwi", "pear", "peach",
    "plum", "apricot", "cherry", "raspberry", "blackberry", "cranberry",
    "coconut", "fig", "lemon", "lime", "pomegranate", "avocado",
    "grapefruit", "cantaloupe", "honeydew", "nectarine", "papaya", "passionfruit",
    "guava", "lychee", "dragonfruit", "persimmon", "tangerine", "jackfruit",
    "kiwano", "starfruit", "breadfruit", "quince", "elderberry", "gooseberry",
    "mulberry", "boysenberry", "loganberry", "carambola", "rhubarb", "ugli fruit",
    "horned melon", "salmonberry", "soursop", "longan", "kumquat", "durian",
    "plantain", "custardapple", "feijoa", "rambutan", "pawpaw", "tamarillo"
    
]
# Game variables
word_to_guess = ""
guessed_letters = []
attempts = 6
root = None  

def choose_word(words_list):
    return random.choice(words_list).lower()

def display_word(word, guessed):
    displayed_word = ""
    for letter in word:
        if letter in guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def check_guess():
    global attempts
    global word_to_guess
    global guessed_letters

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        info_label.config(text="Please enter a single letter.")
        return

    if guess in guessed_letters:
        info_label.config(text="You've already guessed that letter.")
        return

    guessed_letters.append(guess)

    if guess not in word_to_guess:
        attempts -= 1
        info_label.config(text=f"Wrong guess! Attempts left: {attempts}")
        update_hangman_image(attempts)
        if attempts == 0:
            info_label.config(text=f"Sorry, you've run out of attempts. The word was: {word_to_guess}")
            end_game()
            return
    else:
        info_label.config(text="Correct guess!")

    displayed = display_word(word_to_guess, guessed_letters)
    word_label.config(text=displayed)

    if "_" not in displayed:
        info_label.config(text=f"Congratulations! You guessed the word: {word_to_guess}")
        end_game()

def update_hangman_image(attempts_left):
    image_path = f"hangman_images/{6 - attempts_left}.png"
    hangman_image.config(file=image_path)

def end_game():
    entry.config(state=tk.DISABLED)
    guess_button.config(state=tk.DISABLED)
    play_again_button = tk.Button(root, text="Play Again", command=reset_game)
    play_again_button.pack()
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack()

def reset_game():
    global word_to_guess
    global guessed_letters
    global attempts

    entry.config(state=tk.NORMAL)
    guess_button.config(state=tk.NORMAL)
    hangman_image.config(file="hangman_images/0.png")
    word_to_guess = choose_word(words)
    guessed_letters = []
    attempts = 6
    word_label.config(text=display_word(word_to_guess, guessed_letters))
    info_label.config(text="Welcome to Hangman! \nGuess a fruit name in which words are equal to the given spaces")

def hangman_ui():
    global word_to_guess
    global guessed_letters
    global attempts
    global entry
    global word_label
    global info_label
    global hangman_image
    global guess_button
    global root  

    root = tk.Tk()
    root.title("Hangman")
    root.geometry("600x500")

    word_to_guess = choose_word(words)
    guessed_letters = []
    attempts = 6

    hangman_image = tk.PhotoImage(file="hangman_images/0.png")
    hangman_image_label = tk.Label(root, image=hangman_image)
    hangman_image_label.pack()

    word_label = tk.Label(root, text=display_word(word_to_guess, guessed_letters), font=("Arial", 18))
    word_label.pack()

    info_label = tk.Label(root, text="Welcome to Hangman!\n Guess a fruit name in which words are equal to the given spaces", font=("Arial", 12))
    info_label.pack()

    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack()

    guess_button = tk.Button(root, text="Guess", command=check_guess)
    guess_button.pack()

    root.mainloop()

if __name__ == "__main__":
    hangman_ui()
