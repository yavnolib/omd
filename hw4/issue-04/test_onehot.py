from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError("expected at least 1 arguments, got 0")

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f"{{0:0{len(uniq_categories)}b}}"

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (
            int(b) for b in bin_format.format(1 << len(seen_categories))
        )
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


def test_moscow():
    assert fit_transform("I love AAA") == [("I love AAA", [1])]


def test_empty():
    with pytest.raises(TypeError):
        fit_transform()


@pytest.mark.parametrize(
    "what,result",
    [
        ("New York", [("New York", [1])]),
        (
            ["happy", "new", "year", "happy", "ny"],
            [
                ("happy", [0, 0, 0, 1]),
                ("new", [0, 0, 1, 0]),
                ("year", [0, 1, 0, 0]),
                ("happy", [0, 0, 0, 1]),
                ("ny", [1, 0, 0, 0]),
            ],
        ),
    ],
)
def test_ny(what, result):
    assert fit_transform(what) == result


def test_abc():
    assert fit_transform("abc") == [("abc", [1])]
