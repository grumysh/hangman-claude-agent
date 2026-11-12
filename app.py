import streamlit as st

from agent.player import ask_move, load_skill
from config import ATTEMPTS, SKILL
from game.hangman import Hangman

st.title("Ahorcado con Claude")

word = st.text_input("Escribe la palabra a adivinar", type="password")

if st.button("Jugar", disabled=not word):
    game = Hangman(word, ATTEMPTS)
    system = load_skill(SKILL)

    board = st.empty()
    board.markdown(f"## `{game.board()}`\nIntentos restantes: {game.attempts}")

    turn = 0
    while not game.won() and not game.lost():
        turn += 1
        with st.spinner(f"Claude está pensando el turno {turn}..."):
            move = ask_move(system, game)
        correct = game.guess(move["guess"])

        board.markdown(f"## `{game.board()}`\nIntentos restantes: {game.attempts}")
        result = ":green[acierto]" if correct else ":red[fallo]"
        st.markdown(f"**Turno {turn}:** `{move['guess']}` → {result}")
        st.caption(move["reasoning"])

    if game.won():
        st.success(f"Claude adivinó la palabra '{game.word}' en {turn} turnos.")
    else:
        st.error(f"Claude perdió. La palabra era '{game.word}'.")
