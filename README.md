# Shermans-Translator-App

This repository contains a minimal starting point for generating Sherman script patterns based on text input. Each token (a single letter or digraph such as "ch" or "th") is mapped to a base circle type and a modifier (dots or lines). The output is textual, but the mapping matches the structure of the Sherman writing system.

> **Note**
> The current implementation is intentionally simple and acts only as a placeholder. A more complete UI and additional features are planned for future updates.

## Usage

Run `main.py` and enter some text when prompted. The program will output a description of the base shape and modifier for each detected token.

```bash
python3 main.py
```

## Example Output
```
Enter text: thchnd
Generated Patterns:
Token 'th': base=edge_circle, modifier=none
Token 'ch': base=deep_divot, modifier=two_dots
Token 'nd': base=deep_divot, modifier=four_dots
```
