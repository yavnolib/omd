import json
from keyword import iskeyword


class JsonHandler:
    """ Json to args """

    def __init__(self, data) -> None:
        self.data = dict(data)

        for key, attr in self.data.items():
            if iskeyword(key):
                key = f"{key}_"
            setattr(self, key, self.attr_handler(attr))

    def attr_handler(self, attr):
        """ Method for converting json to attributes """
        if isinstance(attr, list):
            return [self.attr_handler(x) for x in attr]
        elif isinstance(attr, dict):
            return JsonHandler(attr)
        return attr


class ColorizeMixin:
    """Mixin for colorized print"""
    START = "\033[1;{};40"
    END = "\033[0"
    MOD = "m"

    def __init_subclass__(cls):
        cls.output = (
            f"{super(cls, cls).START.format(cls.repr_color_code)}"
            f"{super(cls, cls).MOD}{{}}"
            f"{super(cls, cls).END}{super(cls, cls).MOD}"
        )


class Advert(ColorizeMixin, JsonHandler):
    """ A class that use ColorizeMixin """
    repr_color_code = 32

    def __init__(self, data) -> None:
        self.price: int
        self.output: str

        super().__init__(data)

        if hasattr(self, "price"):
            if int(self.price) < 0:
                raise ValueError("must be >= 0")
        else:
            self.price = 0
        if not hasattr(self, "title"):
            raise ValueError("must be title")

    def __str__(self) -> str:
        text = ""
        for attr in self.__dict__["data"].values():
            if isinstance(attr, (dict, list)):
                text += "| "
                text += f"{str(attr)} "
            elif isinstance(attr, JsonHandler):
                text += "| "
                text += f"{attr.__str__} "
            else:
                if text:
                    text += "| "
                text += f"{attr} "
        return self.output.format(text)


if __name__ == "__main__":
    # создаем экземпляр класса Advert из JSON
    lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    # обращаемся к атрибуту location.address
    print(lesson_ad.location.address)
    # Out: 'город Москва, Лесная, 7'

    dog_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    # обращаемся к атрибуту `dog_ad.class_` вместо `dog_ad.class`
    print(dog_ad.class_)

    iphone_ad = Advert({"title": "iPhone X", "price": 100})
    print(iphone_ad)

    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)
