SUBMIT = True

#lo hice con un ciclo y varios casos de prueba pero en phyton se puede usar algo que segun investigue
#se llama string.split que t genera una lista con cada palabra ...luego solo usarias el len
def word_count(s: str) -> int:
    if not s: 
        return 0
    elif ' ' not in s: 
        return 1
    
    count = 0
    for i in range(len(s)):
        if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
            count += 1
    return count

def test() -> None:
    """Simple self-test for Word Count."""
    cases = [
        ("Hello world", 2),
        ("This is a test", 4),
        ("", 0),
        ("  leading and trailing spaces  ", 4),
        ("multiple   spaces", 2),
    ]
    for text, expected in cases:
        try:
            res = word_count(text)
            assert res == expected, (
                f"Failed for text='{text}': expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
