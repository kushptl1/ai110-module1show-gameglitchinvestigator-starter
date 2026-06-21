def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

#FIX: Refactored logic into logic_utils.py using agent mode 
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using agent mode and AI fixed the logic
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Try numeric comparison first (secret may be an int or a numeric string)
    try:
        secret_int = int(secret)
    except Exception:
        secret_int = None

    if secret_int is not None:
        if guess == secret_int:
            return "Win", "🎉 Correct!"
        if guess > secret_int:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

    # Fallback to string comparison if secret isn't numeric
    g_str = str(guess)
    s_str = str(secret)
    if g_str == s_str:
        return "Win", "🎉 Correct!"
    if g_str > s_str:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

#FIX: Refactored logic into logic_utils.py using agent mode
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
