from solution import linear_search


def run():
    assert linear_search([1, 2, 3], 99) == -1
    assert linear_search(["a", "b"], "z") == -1
