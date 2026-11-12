import streamlit as st

from agent.player import ask_move, load_skill
from config import ATTEMPTS, SKILL
from game.hangman import Hangman
from interface.console import show_separator, show_turn
from interface.drawing import hangman_svg


def show_board(board, game):
    color = "white" if st.context.theme.type == "dark" else "black"
    with board.container():
        st.markdown(f"## `{game.board()}`\nIntentos restantes: {game.attempts}")
        st.image(hangman_svg(ATTEMPTS - game.attempts, color))


st.title("Ahorcado con Claude")

word = st.text_input("Escribe la palabra a adivinar")

if st.button("Jugar", disabled=not word):
    game = Hangman(word, ATTEMPTS)
    system = load_skill(SKILL)

    board = st.empty()
    show_board(board, game)

    turn = 0
    while not game.won() and not game.lost():
        turn += 1
        with st.spinner(f"Claude está pensando el turno {turn}..."):
            move = ask_move(system, game)
        correct = game.guess(move["guess"])

        show_board(board, game)
        show_turn(turn, move, correct, game)

    show_separator()

    if game.won():
        st.success(f"Claude adivinó la palabra '{game.word}' en {turn} turnos.")
    else:
        st.error(f"Claude perdió. La palabra era '{game.word}'.")
