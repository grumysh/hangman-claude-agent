from agent.player import ask_move, load_skill
from config import ATTEMPTS, SKILL
from game.hangman import Hangman
from interface.console import show_result, show_turn

word = input("Escribe la palabra a adivinar: ").strip().lower()
game = Hangman(word, ATTEMPTS)
system = load_skill(SKILL)

print(f"\n{game.board()}   intentos: {game.attempts}\n")

turn = 0
while not game.won() and not game.lost():
    turn += 1
    move = ask_move(system, game)
    correct = game.guess(move["guess"])
    show_turn(turn, move, correct, game)

show_result(game, turn)
