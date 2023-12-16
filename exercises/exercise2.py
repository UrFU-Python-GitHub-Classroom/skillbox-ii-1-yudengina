"""Любимый палиндром"""


def is_palindrome(s: str) -> bool:
    """Реализовать функцию, возвращающую True, 
    если строка палиндром, иначе false"""
    s = s.replace(' ', '').lower()
    return s == s[::-1]
