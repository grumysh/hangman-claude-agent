MAKE_GUESS = {
    "name": "make_guess",
    "description": "Make your move in the hangman game: guess one letter or the whole word.",
    "strict": True,
    "input_schema": {
        "type": "object",
        "properties": {
            "reasoning": {
                "type": "string",
                "description": "One short sentence explaining why you chose this move.",
            },
            "guess": {
                "type": "string",
                "description": "One letter or the whole word.",
            },
        },
        "required": ["reasoning", "guess"],
        "additionalProperties": False,
    },
}
