from typing import Generator


def generate_all_substrings(string: str) -> Generator[list[str], None, None]:
    length = len(string)
    for i in range(length):
        i_index_substrings = []
        for j in range(i + 1, length + 1):
            i_index_substrings.append(string[i:j])
        yield i_index_substrings
