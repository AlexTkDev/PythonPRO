# 1. Рядки (Strings)
def string_length(string: str) -> str:
    return len(string)


def union_string(string1: str, string2: str) -> str:
    return f"{string1} {string2}"


assert string_length("abc") == 3
assert union_string("Hello", "world!") == "Hello world!"

