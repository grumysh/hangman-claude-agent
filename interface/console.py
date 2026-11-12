def show_turn(turn, move, correct, game):
    result = "acierto" if correct else "fallo"
    print(f"Turno {turn}: {move['guess']} -> {result}")
    print(f"  Razonamiento: {move['reasoning']}")
    print(f"  {game.board()}   intentos restantes: {game.attempts}\n")


def show_result(game, turns):
    if game.won():
        print(f"Claude adivinó la palabra '{game.word}' en {turns} turnos.")
    else:
        print(f"Claude perdió. La palabra era '{game.word}'.")
