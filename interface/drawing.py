GALLOWS = [
    '<line x1="20" y1="200" x2="110" y2="200" />',
    '<line x1="50" y1="200" x2="50" y2="20" />',
    '<line x1="50" y1="20" x2="140" y2="20" />',
    '<line x1="140" y1="20" x2="140" y2="40" />',
]

BODY_PARTS = [
    '<circle cx="140" cy="58" r="18" />',
    '<line x1="140" y1="76" x2="140" y2="135" />',
    '<line x1="140" y1="95" x2="112" y2="95" />',
    '<line x1="140" y1="95" x2="168" y2="95" />',
    '<line x1="140" y1="135" x2="118" y2="170" />',
    '<line x1="140" y1="135" x2="162" y2="170" />',
]


def hangman_svg(errors, color):
    shapes = "".join(GALLOWS + BODY_PARTS[:errors])
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="215" '
        f'viewBox="0 0 200 215" fill="none" stroke="{color}" '
        'stroke-width="6" stroke-linecap="round">'
        f"{shapes}</svg>"
    )
