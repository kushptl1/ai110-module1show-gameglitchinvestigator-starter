from logic_utils import parse_guess, update_score


def test_parse_guess_none_or_empty():
    ok, val, err = parse_guess(None)
    assert ok is False
    assert val is None
    assert err == "Enter a guess."

    ok, val, err = parse_guess("")
    assert ok is False
    assert val is None
    assert err == "Enter a guess."


def test_parse_guess_number_and_float():
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42

    ok, val, err = parse_guess("3.0")
    assert ok is True
    assert val == 3


def test_parse_guess_invalid():
    ok, val, err = parse_guess("notanumber")
    assert ok is False
    assert val is None
    assert err == "That is not a number."


def test_update_score_win_and_bounds():
    score = update_score(0, "Win", 1)
    assert score == 80


def test_update_score_too_high_alternates():
    s = update_score(0, "Too High", 2)
    assert s == 5
    s = update_score(5, "Too High", 3)
    assert s == 0


def test_update_score_too_low():
    s = update_score(10, "Too Low", 1)
    assert s == 5
