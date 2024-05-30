def create_substrings(string: str, start: int) -> list[str]:
    sentence_length = len(string)
    return [string[start:end] for end in range(sentence_length, start, -1)]


def matches_all_sentences(substring: str, sentences: list[str]) -> bool:
    return all(substring in sentence for sentence in sentences)


def find_common_groups(sentences: list[str]) -> list[str]:
    if not sentences:
        return []

    shortest_sentence = min(sentences, key=len)
    shortest_sentence_length = len(shortest_sentence)

    common_groups: list[str] = []

    i = 0
    while i < shortest_sentence_length:
        i_index_substrings = create_substrings(string=shortest_sentence, start=i)

        for substring in i_index_substrings:
            if matches_all_sentences(substring=substring, sentences=sentences):
                common_groups.append(substring)
                i += len(substring)
                break

        i += 1

    return common_groups
