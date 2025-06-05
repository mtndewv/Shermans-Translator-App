# Pattern generator for Sherman Translator App
# Provides functions to map letters to circular pattern types and modifiers

from dataclasses import dataclass
from typing import Tuple, Dict

@dataclass
class PatternInfo:
    """Information about a pattern for a specific letter."""
    pattern_type: str
    modifier: str

# Basic example mapping for letters to pattern info
LETTER_PATTERN_MAP: Dict[str, PatternInfo] = {
    'a': PatternInfo('solid', 'small'),
    'b': PatternInfo('solid', 'medium'),
    'c': PatternInfo('solid', 'large'),
    'd': PatternInfo('dashed', 'small'),
    'e': PatternInfo('dashed', 'medium'),
    'f': PatternInfo('dashed', 'large'),
    # Add more mappings as needed
}

def get_pattern_for_letter(letter: str) -> PatternInfo:
    """Return the pattern information for a given letter."""
    letter = letter.lower()
    return LETTER_PATTERN_MAP.get(letter, PatternInfo('solid', 'small'))

def generate_patterns(text: str) -> Tuple[PatternInfo, ...]:
    """Generate a sequence of PatternInfo objects for the given text."""
    return tuple(get_pattern_for_letter(ch) for ch in text if ch.isalpha())


def describe_patterns(text: str) -> str:
    """Return a human readable description of the patterns for the text."""
    descriptions = []
    for ch in text:
        if ch.isalpha():
            info = get_pattern_for_letter(ch)
            descriptions.append(
                f"Letter '{ch}': pattern={info.pattern_type}, modifier={info.modifier}"
            )
    return '\n'.join(descriptions)
