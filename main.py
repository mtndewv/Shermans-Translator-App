"""Command line interface for generating circular patterns based on text input."""
from pattern_generator import describe_patterns


def main() -> None:
    text = input("Enter text: ")
    print("Generated Patterns:")
    print(describe_patterns(text))


if __name__ == "__main__":
    main()
