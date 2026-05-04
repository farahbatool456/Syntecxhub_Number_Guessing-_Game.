# 🎯 Number Guessing Game

A console-based Python game where the computer picks a secret number and you try to guess it with hints.

**Remote Internship — Project 2**

---

## Features

- 4 difficulty levels with different number ranges and attempt limits
- Higher / Lower hints after every wrong guess
- Attempt counter displayed in real time
- Best score (lowest attempts) tracking per difficulty
- Replay option after each round

---

## Difficulty Levels

| Level  | Range      | Max Attempts |
|--------|------------|--------------|
| Easy   | 1 – 50     | 15           |
| Medium | 1 – 100    | 10           |
| Hard   | 1 – 500    | 12           |
| Expert | 1 – 1000   | 10           |

---

## Concepts Covered

- `random` module — `random.randint()` to generate the secret number
- **Loops** — `while` loop for the main game, outer loop for replay
- **Conditionals** — `if / elif / else` for Higher / Lower / Correct logic
- Input validation with `try / except`
- Functions for clean, modular structure

---

## How to Run

**Requirements:** Python 3.6 or higher (no external packages needed)

```bash
# Clone the repo
git clone https://github.com/<your-username>/number-guessing-game.git

# Go into the project folder
cd number-guessing-game

# Run the game
python game.py
```

---

## Project Structure

```
number-guessing-game/
├── game.py          # Main game file — all logic lives here
├── README.md        # Project documentation (this file)
├── .gitignore       # Files Git should ignore
└── LICENSE          # MIT License
```

---

## How to Play

1. Run `python game.py`
2. Choose a difficulty level (1–4)
3. Enter your guess when prompted
4. Follow the Higher / Lower hints
5. Win by guessing correctly before attempts run out
6. Choose to replay or exit after each round

---


