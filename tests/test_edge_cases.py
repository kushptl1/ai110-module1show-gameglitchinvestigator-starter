from logic_utils import parse_guess, check_guess


def test_negative_number_parsing():
    ok, val, err = parse_guess("-5")
    assert ok is True
    assert val == -5
    assert err is None


def test_zero_parsing_and_check():
    ok, val, err = parse_guess("0")
    assert ok is True
    assert val == 0
    outcome, _ = check_guess(val, 1)
    assert outcome == "Too Low"


def test_decimal_input_truncates():
    ok, val, err = parse_guess("3.7")
    assert ok is True
    assert val == 3


def test_commas_are_rejected():
    ok, val, err = parse_guess("1,000")
    assert ok is False
    assert val is None
    assert err == "That is not a number."


def test_scientific_notation_is_rejected():
    ok, val, err = parse_guess("1e3")
    assert ok is False
    assert val is None


def test_leading_trailing_spaces():
    ok, val, err = parse_guess(" 42 ")
    assert ok is True
    assert val == 42


def test_plus_sign_parsing():
    ok, val, err = parse_guess("+7")
    assert ok is True
    assert val == 7


def test_unicode_digit_parsing():
    # Arabic-Indic digit three
    ok, val, err = parse_guess("٣")
    assert ok is True
    assert val == 3


def test_extremely_large_integer():
    big = "9" * 50
    ok, val, err = parse_guess(big)
    assert ok is True
    # value should be an int and compare properly
    outcome, _ = check_guess(val, int(big) - 1)
    assert outcome == "Too High"
