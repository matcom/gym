from solution import is_palindrome


def run():
    assert is_palindrome("aba")
    assert is_palindrome("abba")
    assert not is_palindrome("hola")
    assert not is_palindrome("python")
