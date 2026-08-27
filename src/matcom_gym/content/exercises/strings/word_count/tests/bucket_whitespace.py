from solution import word_count


def run():
    assert word_count("a\tb\nc") == 3
    assert word_count("uno\ndos\ttres") == 3
