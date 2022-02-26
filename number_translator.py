from collections import OrderedDict as od


def to_arab_nums(roman_nums: list[str]) -> list[int]:
    rule_add = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    rule_div = {
        ('I', 'V'): 3,
        ('I', 'X'): 8,
        ('X', 'L'): 30,
        ('X', 'C'): 80,
        ('C', 'D'): 300,
        ('C', 'M'): 800,
    }

    results = list()

    for roman_number in roman_nums:
        number = 0
        prev_literal = None
        for literal in roman_number:
            if prev_literal and rule_add[prev_literal] < rule_add[literal]:
                number += rule_div[(prev_literal, literal)]
            else:
                number += rule_add[literal]
            prev_literal = literal
        results.append(number)

    return results


def to_roman_nums(arabic_nums: list[int]) -> list[str]:
    rules = (
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("XXX", 30),
        ("XX", 20),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    )

    results = list()
    for num in arabic_nums:
        result = ""
        for suf, val in rules:
            while num >= val:
                num -= val
                result += suf
        results.append(result)

    return results
