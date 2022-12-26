class Fruit:
    sex = 'fruit'
    pass


class Apple(Fruit):
    def __init__(self):
        self.name = 'apple'
        self.caloric = 100


class Orange(Fruit):
    def __init__(self):
        self.name = 'orange'
        self.caloric = 200


class Banana(Fruit):
    def __init__(self):
        self.name = 'banana'
        self.caloric = 300


b = Banana
print(b.sex, b.__name__)