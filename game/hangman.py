ACCENTS = str.maketrans("áéíóúü", "aeiouu")


def clean(text):
    return text.strip().lower().translate(ACCENTS)


class Hangman:
    def __init__(self, word, attempts):
        self.word = clean(word)
        self.attempts = attempts
        self.guessed_letters = []

    def board(self):
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.word
        )

    def guess(self, move):
        move = clean(move)

        if len(move) == 1:
            self.guessed_letters.append(move)
            if move in self.word:
                return True
            self.attempts -= 1
            return False

        if move == self.word:
            self.guessed_letters.extend(self.word)
            return True
        self.attempts -= 1
        return False

    def won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def lost(self):
        return self.attempts == 0
