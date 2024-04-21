from typing import Union


# 1. Рядки (Strings) ===============================================
def string_length(string: str) -> str:
    """
    Функція приймає рядок і повертає його довжину.
    """
    return len(string)


def union_string(string1: str, string2: str) -> str:
    """
    Функція приймає два рядки і повертає об'єднаний рядок.
    """
    return f"{string1} {string2}"


# 2. Числа (Int/float) ===============================================
def square(number) -> Union[int, float]:
    """
    Функція приймає число і повертає його квадрат.
    """
    return number ** 2


def sum_of_numbers(number1: int, number2: int) -> Union[int, float]:
    """
    Функція приймає два числа і повертає їхню суму.
    """
    return number1 + number2


def division(number1: int, number2: int) -> Union[int, float]:
    """
    Функція приймає 2 числа типу int, виконує операцію ділення
    та повертає цілу частину і залишок.
    """
    return divmod(number1, number2)


# 3. Списки (Lists) ===============================================
def average_value(user_list: list) -> Union[int, float]:
    """
    Обчислення середнього значення списку чисел.
    """
    return sum(user_list) / len(user_list)


def get_common_elements(list_1: list, list_2: list) -> list:
    """
    Функція приймає два списки і повертає список, який містить спільні елементи обох списків.
    """
    return list(set(list_1) & set(list_2))


# 4. Словники (Dictionaries) ===============================================
def all_keys(dictionary: dict) -> list:
    """
    Функція приймає словник і виводить всі ключі цього словника.
    """
    return list(dictionary.keys())


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Функція приймає два словники та повертає новий словник, який є об'єднанням обох словників.
    """
    dict1.update(dict2)
    return dict1


# 5. Множини (Sets) ===============================================
def union_set(set1: set, set2: set) -> set:
    """
    Функція приймає дві множини та повертає їхнє об'єднання.
    """
    return set.union(set1, set2)


def is_subset(set1: set, set2: set) -> bool:
    """
    Функція перевіряє, чи є одна множина підмножиною іншої.
    """
    return set.issubset(set1, set2)


# 6. Умовні вирази та цикли ===============================================
def is_even(number: int) -> str:
    """
    Функція приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.
    """
    return "Парне" if number % 2 == 0 else "Непарне"


def only_even(number: int) -> list:
    """
    Функцію приймає список чисел та повертає новий список, що містить тільки парні числа.
    """
    return list(filter(lambda digit: digit % 2 == 0, number))


if __name__ == "__main__":
    # 1
    assert string_length("abc") == 3
    assert union_string("Hello", "world!") == "Hello world!"
    # 2
    assert square(5) == 25
    assert sum_of_numbers(1, 2) == 3
    assert division(5, 2) == (2, 1)
    # 3
    assert average_value([1, 3, 5, 10]) == 4.75
    assert get_common_elements([1, 2, 4, 5], [2, 3, 4, 5]) == [2, 4, 5]
    # 4
    assert all_keys({"a": 1, "b": 2, "c": 3}) == ["a", "b", "c"]
    assert merge_dicts({"a": 1, "b": 2, "c": 3},
                       {"d": 5, "e": 7, "f": 8}
                       ) == {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 7, 'f': 8}
    # 5
    assert union_set({1, 2, 3}, {3, 4, 5}) == {1, 2, 3, 4, 5}
    assert is_subset({1, 2, 3}, {1, 2, 3, 4, 5}) == True
    assert is_subset({1, 2, 3}, {1, 2, 8, 4, 5}) == False
    # 6
    assert is_even(4) == "Парне"
    assert is_even(9) == "Непарне"
    assert only_even([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]
