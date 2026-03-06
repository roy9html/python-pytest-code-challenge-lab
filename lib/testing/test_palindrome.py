import pytest

from lib.palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("cbbd", "bb"),
        ("a", "a"),
        ("", ""),
        ("racecar", "racecar"),
        ("forgeeksskeegfor", "geeksskeeg"),
        ("a" * 50, "a" * 50),
    ],
)
def test_returns_expected_palindrome_for_exact_cases(text, expected):
    assert longest_palindromic_substring(text) == expected


@pytest.mark.parametrize(
    ("text", "expected_options"),
    [
        ("babad", {"bab", "aba"}),
        ("ac", {"a", "c"}),
    ],
)
def test_allows_multiple_valid_longest_palindromes(text, expected_options):
    result = longest_palindromic_substring(text)

    assert result in expected_options


def test_returns_single_character_when_no_longer_palindrome_exists():
    result = longest_palindromic_substring("abcde")

    assert len(result) == 1
    assert result in set("abcde")


def test_prefers_the_longest_palindrome_inside_a_larger_string():
    assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"