from typing import Generator

import numpy as np
import numpy.typing as npt


def calculate_exact_regex(sentences: list[str]) -> str:
    common_groups = find_common_groups(sentences=sentences)
    split_sentences = split_by_common_groups(
        sentences=sentences,
        common_groups=common_groups,
    )

    regex = ""
    for i, common_group in enumerate(common_groups):
        alternatives_string = create_alternatives_string(alternatives=split_sentences[:, i])
        regex += alternatives_string
        regex += common_group

    alternatives_string = create_alternatives_string(alternatives=split_sentences[:, -1])
    regex += alternatives_string
    return regex


def create_alternatives_string(alternatives: npt.NDArray[np.str_]) -> str:
    empties = alternatives.__eq__("")
    alternatives = alternatives[alternatives != ""]
    alternatives = np.unique(alternatives)

    if empties.all():
        return ""

    optional_mark = "?" if empties.any() else ""

    if alternatives.size == 1:
        el = alternatives[0]
        if len(el) == 1:
            return alternatives[0] + optional_mark

    return f"({'|'.join(alternatives)}){optional_mark}"


def split_by_common_groups(
    sentences: list[str],
    common_groups: list[str] | None = None,
) -> npt.NDArray[np.str_]:
    if not common_groups:
        common_groups = find_common_groups(sentences=sentences)

    sentences_split = np.empty((len(sentences), len(common_groups) + 1), dtype=np.dtypes.StrDType)

    if not common_groups:
        return sentences_split

    for sentence_index, sentence in enumerate(sentences):
        for i, common_group in enumerate(common_groups):
            occurrence_index = sentence.find(common_group)
            segment = sentence[:occurrence_index]
            sentence = sentence[occurrence_index + len(common_group) :]
            sentences_split[sentence_index][i] = segment

        sentences_split[sentence_index][-1] = sentence

    return sentences_split


def find_common_groups(sentences: list[str]) -> list[str]:
    if not sentences:
        return []

    shortest_sentence = min(sentences, key=len)
    shortest_sentence_length = len(shortest_sentence)

    common_groups: list[str] = []

    i = 0
    while i < shortest_sentence_length:
        for substring in generate_substrings(string=shortest_sentence, start=i):
            if matches_all_sentences(substring=substring, sentences=sentences):
                common_groups.append(substring)
                i += len(substring)
                break
        else:
            i += 1

    return common_groups


def generate_substrings(string: str, start: int) -> Generator[str, None, None]:
    sentence_length = len(string)
    for end in range(sentence_length, start, -1):
        yield string[start:end]


def matches_all_sentences(substring: str, sentences: list[str]) -> bool:
    return all(substring in sentence for sentence in sentences)
