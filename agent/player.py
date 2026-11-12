from pathlib import Path

from agent.client import send
from agent.tool import MAKE_GUESS

SKILLS_DIR = Path(__file__).parent / "skills"


def load_skill(name):
    return (SKILLS_DIR / f"{name}.md").read_text()


def ask_move(system, game):
    message = (
        f"Board: {game.board()}\n"
        f"Letters tried: {', '.join(game.guessed_letters) or 'none'}\n"
        f"Attempts left: {game.attempts}\n"
        "Use the make_guess tool to make your move."
    )

    response = send(system, [{"role": "user", "content": message}], tools=[MAKE_GUESS])

    for block in response.content:
        if block.type == "tool_use":
            return block.input
