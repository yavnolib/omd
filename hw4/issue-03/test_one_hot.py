from typing import List, Tuple
import unittest


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


class TestOneHotEncoder(unittest.TestCase):
    def test_moscow(self):
        self.assertEqual(fit_transform("I love AAA"), [("I love AAA", [1])])

    def test_ny(self):
        self.assertTrue(
            fit_transform(["Moscow", "New York", "Moscow", "London"])
            == [
                ("Moscow", [0, 0, 1]),
                ("New York", [0, 1, 0]),
                ("Moscow", [0, 0, 1]),
                ("London", [1, 0, 0]),
            ]
        )

    def test_empty(self):
        self.assertRaises(TypeError, fit_transform)

    def test_abc(self):
        self.assertNotIn(fit_transform("abc"), [("abc", 2), 3])


if __name__ == "__main__":
    unittest.main()
