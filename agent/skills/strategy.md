# Hangman

You are playing hangman. Your goal is to guess a secret word. The word is in Spanish.

## Rules

- At the start you only know how many letters the word has. Each hidden letter is shown as `_`.
- Each turn you can guess one letter or guess the whole word.
- If the letter is in the word, all of its positions are revealed.
- If the letter is not in the word, you lose one attempt.
- If you guess the whole word and you are wrong, you also lose one attempt.
- Do not repeat letters you already tried.
- You win if you reveal the whole word before running out of attempts. You lose if you run out of attempts.

## Strategy

1. Start with the vowels, in this order: E, A, O, I, U.
2. Then try the most common Spanish consonants, in this order: S, R, N, D, L, C, T.
3. Guess the whole word when:
   - about 60% of the letters are revealed, or
   - the pattern of revealed letters leaves only a few possible words.
