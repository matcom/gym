from solution import histogram


def run():
    assert histogram(["z"]) == {"z": 1}
    assert histogram([42]) == {42: 1}
