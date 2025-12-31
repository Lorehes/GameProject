# Hangman Game Logic

# Game Setup
word = "man".upper()
word_show = "_" * len(word)
try_num = 0
ok_list = []
no_list = []
MAX_TRIES = 7

print(f"Word to guess: {word_show}")

# Game Loop
while True:
    ans = input("Guess a letter: ").upper()
    
    if ans in word:
        print("Letter found!")
        ok_list.append(ans)
        for i in range(len(word)):
            if word[i] == ans:
                word_show = word_show[:i] + ans + word_show[i+1:]
        print(f"Current: {word_show}")
    else:
        print("Letter not found.")
        try_num += 1
        no_list.append(ans)
        print(f"Tries left: {MAX_TRIES - try_num}")

    # Check win/lose conditions
    if try_num == MAX_TRIES:
        print(f"Game Over! The word was: {word}")
        break
    
    if "_" not in word_show:
        print("Congratulations! You won!")
        break