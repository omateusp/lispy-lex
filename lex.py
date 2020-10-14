import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """
    tokens = [
        ("LPAR", r"\("),
        ("RPAR", r"\)"),
        ("STRING", r"\".*\""),
        ("QUOTE", r"\'"),
        ("CHAR", r"#\\[A-Za-z]*"),
    ]

    clean_code = re.sub(r";;.*", "", code)

    regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)

    for token in re.finditer(regex, clean_code):
        yield Token(token.lastgroup, token.group())

    return [Token('INVALIDA', 'valor inválido')]