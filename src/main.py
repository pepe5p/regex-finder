from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

from common_groups import calculate_exact_regex


def calculate_dfa(sentences: list[str]) -> None:
    regex = calculate_exact_regex(sentences=sentences)
    print(f"Regex: {regex}")
    nfa = NFA.from_regex(regex=regex)
    dfa = DFA.from_nfa(target_nfa=nfa)
    dfa = dfa.minify()
    dfa.show_diagram(path="dfa.png")


if __name__ == "__main__":
    calculate_dfa(["abcd", "abcbcd", "abcabcd"])
