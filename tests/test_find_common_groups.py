import numpy as np
import pytest

from common_groups import calculate_exact_regex, find_common_groups, generate_substrings, split_by_common_groups


@pytest.mark.parametrize(
    ("sentences", "expected_regex"),
    [
        (["abcd", "ababcd", "abababcd"], "(ab|abab)?abcd"),
        (["abcd", "ababced", "abababced"], "(ab|abab)?abce?d"),
        (["abcd", "cdcdabcd", "cdabcde"], "(cd|cdcd)?abcde?"),
        (["abc", "adc", "aec"], "a(b|d|e)c"),
        (["abcdef", "adcdef", "xaxcdefx"], "x?a(b|d|x)cdefx?"),
        (["ababa", "acaca", "adada"], "a(b|c|d)a(b|c|d)a"),
        (["ab", "ba"], "b?ab?"),
        (["aab", "aba", "baa"], "b?ab?ab?"),
    ],
)
def test_calculate_exact_regex(sentences: list[str], expected_regex: str) -> None:
    regex = calculate_exact_regex(sentences)
    assert regex == expected_regex


@pytest.mark.parametrize(
    ("sentences", "expected_split_sentences"),
    [
        (["abcd", "ababcd", "abababcd"], [["", ""], ["ab", ""], ["abab", ""]]),
        (["abcd", "cdcdabcd", "cdabcde"], [["", ""], ["cdcd", ""], ["cd", "e"]]),
        (["abc", "adc", "aec"], [["", "b", ""], ["", "d", ""], ["", "e", ""]]),
        (["abcdef", "adcdef", "xaxcdefx"], [["", "b", ""], ["", "d", ""], ["x", "x", "x"]]),
        (["ababa", "acaca", "adada"], [["", "b", "b", ""], ["", "c", "c", ""], ["", "d", "d", ""]]),
        (["ab", "ba"], [["", "b"], ["b", ""]]),
        (["aab", "aba", "baa"], [["", "", "b"], ["", "b", ""], ["b", "", ""]]),
    ],
)
def test_split_by_common_groups(sentences: list[str], expected_split_sentences: list[list[str]]) -> None:
    expected_split_sentences = np.array(expected_split_sentences, dtype=np.dtypes.StrDType)
    split_sentences = split_by_common_groups(sentences)
    assert split_sentences.__eq__(expected_split_sentences).all()
    assert np.array_equal(split_sentences, expected_split_sentences)


@pytest.mark.parametrize(
    ("sentences", "expected_common_groups"),
    [
        (["abcd", "ababcd", "abababcd"], ["abcd"]),
        (["abcd", "ababced", "abababced"], ["abc", "d"]),
        (["abcd", "cdcdabcd", "cdabcde"], ["abcd"]),
        (["abc", "adc", "aec"], ["a", "c"]),
        (["abcdef", "adcdef", "xaxcdefx"], ["a", "cdef"]),
        (["ababa", "acaca", "adada"], ["a", "a", "a"]),
        (["ab", "ba"], ["a"]),
        (["aab", "aba", "baa"], ["a", "a"]),
    ],
)
def test_find_common_groups(sentences: list[str], expected_common_groups: list[str]) -> None:
    common_groups = find_common_groups(sentences)
    assert common_groups == expected_common_groups


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
def test_generate_substrings(string: str, start: int, expected_substrings: list[str]) -> None:
    substrings = list(generate_substrings(string=string, start=start))
    assert substrings == expected_substrings
