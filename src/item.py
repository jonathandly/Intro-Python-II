class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'\n{self.name} -> {self.description}\n'

    def inspect(self):
        return f'The item: {self.name} is -> {self.description}'


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories

    def __str__(self):
        super().__str__() + f'contains {self.calories} calories'


class Gold(Item):
    def __init__(self, value):
        super().__init__('Gold', 'A shiny coin')
        self.value = value

    def __str__(self):
        return f'This {self.name} is worth {self.value}'
