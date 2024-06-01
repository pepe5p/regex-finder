import pytest

from generate_substrings import generate_all_substrings


@pytest.mark.parametrize(
    ("string", "expected_substrings"),
    [
        ("", []),
        ("a", [["a"]]),
        ("ab", [["a", "ab"], ["b"]]),
        ("abc", [["a", "ab", "abc"], ["b", "bc"], ["c"]]),
        ("abcd", [["a", "ab", "abc", "abcd"], ["b", "bc", "bcd"], ["c", "cd"], ["d"]]),
        ("aaaa", [["a", "aa", "aaa", "aaaa"], ["a", "aa", "aaa"], ["a", "aa"], ["a"]]),
    ],
)
def test_generate_all_substrings(string: str, expected_substrings: list[str]) -> None:
    substrings = generate_all_substrings(string)
    assert list(substrings) == expected_substrings
