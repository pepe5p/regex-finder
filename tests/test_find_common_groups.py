import pytest

from main import create_substrings, find_common_groups


@pytest.mark.parametrize(
    ("string", "start", "expected_substrings"),
    [
        ("abcd", 0, ["abcd", "abc", "ab", "a"]),
        ("abcd", 1, ["bcd", "bc", "b"]),
        ("abcd", 2, ["cd", "c"]),
        ("abcd", 3, ["d"]),
        ("abcd", 4, []),
    ],
)
def test_create_substrings(string: str, start: int, expected_substrings: list[str]) -> None:
    substrings = create_substrings(string=string, start=start)
    assert substrings == expected_substrings


@pytest.mark.parametrize(
    ("sentences", "expected_common_groups"),
    [
        (["abcd", "ababcd", "abababcd"], ["abcd"]),
        (["abcd", "cdcdabcd", "cdabcde"], ["abcd"]),
        (["abc", "adc", "aec"], ["a", "c"]),
        (["abcdef", "adcdef", "xaxcdefx"], ["a", "cdef"]),
        (["ababa", "acaca", "adada"], ["a", "a", "a"]),
    ],
)
def test_find_common_groups(sentences: list[str], expected_common_groups: list[str]) -> None:
    common_groups = find_common_groups(sentences)
    assert common_groups == expected_common_groups
