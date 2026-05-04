"""
Number Guessing Game
====================
A console-based number guessing game with:
- Multiple difficulty levels
- Higher/Lower hints
- Attempt tracking
- Best score (lowest attempts) tracking
- Replay option

Author: FARAH BATOOL
Project: Remote Internship - Project 1
"""

import random


# ──────────────────────────────────────────
#  DIFFICULTY SETTINGS
# ──────────────────────────────────────────

DIFFICULTY_LEVELS = {
    "1": {
        "name": "Easy",
        "range_min": 1,
        "range_max": 50,
        "max_attempts": 15,
        "description": "Range: 1 – 50  |  Max attempts: 15",
    },
    "2": {
        "name": "Medium",
        "range_min": 1,
        "range_max": 100,
        "max_attempts": 10,
        "description": "Range: 1 – 100  |  Max attempts: 10",
    },
    "3": {
        "name": "Hard",
        "range_min": 1,
        "range_max": 500,
        "max_attempts": 12,
        "description": "Range: 1 – 500  |  Max attempts: 12",
    },
    "4": {
        "name": "Expert",
        "range_min": 1,
        "range_max": 1000,
        "max_attempts": 10,
        "description": "Range: 1 – 1000  |  Max attempts: 10",
    },
}


# ──────────────────────────────────────────
#  DISPLAY HELPERS
# ──────────────────────────────────────────

def print_banner():
    """Print the game title banner."""
    print("\n" + "=" * 50)
    print("        🎯  NUMBER GUESSING GAME  🎯")
    print("=" * 50)


def print_separator():
    print("-" * 50)


def show_difficulty_menu():
    """Display difficulty level options."""
    print("\n📋  SELECT DIFFICULTY LEVEL:\n")
    for key, level in DIFFICULTY_LEVELS.items():
        print(f"  [{key}] {level['name']:<8}  —  {level['description']}")
    print()


def show_best_scores(best_scores: dict):
    """Display best scores for each difficulty."""
    print("\n🏆  BEST SCORES (Lowest Attempts):\n")
    has_score = False
    for key, level in DIFFICULTY_LEVELS.items():
        name = level["name"]
        if name in best_scores:
            print(f"  {name:<8}: {best_scores[name]} attempt(s)")
            has_score = True
    if not has_score:
        print("  No scores recorded yet.")
    print()


# ──────────────────────────────────────────
#  INPUT VALIDATORS
# ──────────────────────────────────────────

def get_difficulty_choice() -> dict:
    """Prompt user to pick a difficulty. Returns level config dict."""
    while True:
        show_difficulty_menu()
        choice = input("Enter your choice (1/2/3/4): ").strip()
        if choice in DIFFICULTY_LEVELS:
            selected = DIFFICULTY_LEVELS[choice]
            print(f"\n✅  Difficulty set to: {selected['name']}")
            return selected
        print("❌  Invalid choice. Please enter 1, 2, 3, or 4.\n")


def get_player_guess(range_min: int, range_max: int, attempts_left: int) -> int:
    """Prompt user for a valid integer guess within the allowed range."""
    while True:
        try:
            raw = input(
                f"\n🎲  Guess a number ({range_min}–{range_max})  "
                f"[Attempts left: {attempts_left}]: "
            ).strip()
            guess = int(raw)
            if range_min <= guess <= range_max:
                return guess
            print(f"⚠️   Please enter a number between {range_min} and {range_max}.")
        except ValueError:
            print("⚠️   That's not a valid number. Try again.")


def ask_replay() -> bool:
    """Ask user if they want to play again. Returns True/False."""
    while True:
        choice = input("\n🔄  Play again? (yes / no): ").strip().lower()
        if choice in ("yes", "y"):
            return True
        if choice in ("no", "n"):
            return False
        print("⚠️   Please type 'yes' or 'no'.")


# ──────────────────────────────────────────
#  CORE GAME LOGIC
# ──────────────────────────────────────────

def play_round(level: dict, best_scores: dict) -> dict:
    """
    Run a single game round.

    Parameters
    ----------
    level       : difficulty config dict
    best_scores : running best-score tracker (mutated in place)

    Returns
    -------
    Updated best_scores dict.
    """
    range_min    = level["range_min"]
    range_max    = level["range_max"]
    max_attempts = level["max_attempts"]
    level_name   = level["name"]

    # Pick a random secret number using the random module
    secret_number = random.randint(range_min, range_max)

    attempts_used = 0
    won = False

    print_separator()
    print(f"\n🎮  Starting {level_name} mode!")
    print(f"    I've picked a number between {range_min} and {range_max}.")
    print(f"    You have {max_attempts} attempts. Good luck!\n")

    # ── Main guessing loop ──
    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used
        guess = get_player_guess(range_min, range_max, attempts_left)
        attempts_used += 1

        # ── Conditional: evaluate the guess ──
        if guess == secret_number:
            won = True
            break
        elif guess < secret_number:
            remaining = max_attempts - attempts_used
            print(f"  📈  Too LOW!  Go higher.  ({remaining} attempt(s) left)")
        else:
            remaining = max_attempts - attempts_used
            print(f"  📉  Too HIGH! Go lower.   ({remaining} attempt(s) left)")

    # ── Round result ──
    print_separator()
    if won:
        print(f"\n🎉  CORRECT! The number was {secret_number}.")
        print(f"    You guessed it in {attempts_used} attempt(s).\n")

        # Update best score if this round is better (fewer attempts)
        if level_name not in best_scores or attempts_used < best_scores[level_name]:
            best_scores[level_name] = attempts_used
            print("⭐  New best score for this difficulty!\n")
    else:
        print(f"\n💀  Out of attempts! The number was {secret_number}.")
        print("    Better luck next time!\n")

    return best_scores


# ──────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────

def main():
    """Main function — controls game flow and replay loop."""
    print_banner()
    print("\nWelcome! Guess the secret number within the allowed attempts.")

    best_scores = {}   # Stores best (lowest) attempt count per difficulty

    # ── Outer replay loop ──
    while True:
        level = get_difficulty_choice()
        best_scores = play_round(level, best_scores)
        show_best_scores(best_scores)

        if not ask_replay():
            print("\n👋  Thanks for playing! Goodbye.\n")
            break

    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
