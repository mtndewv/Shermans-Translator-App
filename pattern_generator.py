# Pattern generator for Sherman Translator App
# Maps text to Sherman script base shapes and modifiers

from dataclasses import dataclass
from typing import Dict, List

@dataclass
class PatternInfo:
    """Information about a Sherman script character."""

    base_shape: str
    modifier: str

# Names for the four base circle types (rows)
BASE_SHAPES = (
    "deep_divot",       # row 1
    "inner_circle",     # row 2
    "shallow_divot",    # row 3
    "edge_circle",      # row 4
)

# Names for the eight modifiers (columns)
MODIFIERS = (
    "none",         # no dots or lines
    "one_dot",
    "two_dots",
    "three_dots",
    "four_dots",
    "three_lines",
    "two_lines",
    "one_line",
)

# Mapping of tokens (letters or digraphs) to (row, column) indices
# Each row corresponds to a base shape and each column to a modifier
_TOKEN_MAP: Dict[str, tuple[int, int]] = {
    # Row 1 - deep divot
    "b": (0, 0),
    "a": (0, 1),  # "blank" position often used for the letter A
    "ch": (0, 2),
    "d": (0, 3),
    "nd": (0, 4),
    "f": (0, 5),
    "h": (0, 6),
    "g": (0, 7),

    # Row 2 - inner circle
    "j": (1, 0),
    "ph": (1, 1),
    "k": (1, 2),
    "l": (1, 3),
    "c": (1, 4),
    "m": (1, 5),
    "p": (1, 6),
    "n": (1, 7),

    # Row 3 - shallow divot
    "t": (2, 0),
    "wh": (2, 1),
    "sh": (2, 2),
    "r": (2, 3),
    "nt": (2, 4),
    "s": (2, 5),
    "w": (2, 6),
    "v": (2, 7),

    # Row 4 - edge circle
    "th": (3, 0),
    "gh": (3, 1),
    "y": (3, 2),
    "z": (3, 3),
    "q": (3, 4),
    "ng": (3, 5),
    "x": (3, 6),
    "qu": (3, 7),
}

# Default pattern when a character is not recognized
_DEFAULT_PATTERN = PatternInfo(BASE_SHAPES[0], MODIFIERS[0])


def _tokenize(text: str) -> List[str]:
    """Split text into Sherman script tokens (letters or digraphs)."""
    text = text.lower()
    tokens: List[str] = []
    i = 0
    while i < len(text):
        # Check for two-letter tokens first
        if i + 1 < len(text) and text[i : i + 2] in _TOKEN_MAP:
            tokens.append(text[i : i + 2])
            i += 2
        elif text[i] in _TOKEN_MAP:
            tokens.append(text[i])
            i += 1
        else:
            # Skip characters that are not part of the alphabet
            i += 1
    return tokens


def get_pattern_for_token(token: str) -> PatternInfo:
    """Return the PatternInfo associated with a token."""
    mapping = _TOKEN_MAP.get(token)
    if mapping is None:
        return _DEFAULT_PATTERN
    row, col = mapping
    return PatternInfo(BASE_SHAPES[row], MODIFIERS[col])


def generate_patterns(text: str) -> List[PatternInfo]:
    """Generate a list of PatternInfo objects for the given text."""
    tokens = _tokenize(text)
    return [get_pattern_for_token(tok) for tok in tokens]


def describe_patterns(text: str) -> str:
    """Return a human readable description of the patterns for the text."""
    tokens = _tokenize(text)
    descriptions = []
    for tok in tokens:
        info = get_pattern_for_token(tok)
        descriptions.append(
            f"Token '{tok}': base={info.base_shape}, modifier={info.modifier}"
        )
    return "\n".join(descriptions)
