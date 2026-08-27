from solution import word_count


def run():
    assert word_count("hola mundo") == 2
    assert word_count("uno dos tres") == 3
    assert word_count("solo") == 1
