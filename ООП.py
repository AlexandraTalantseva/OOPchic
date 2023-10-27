class Pizza:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def base_size(self):
        if self.size == 'Big':
            return 15
        if self.size == 'Middle':
            return 10
        if self.size == 'Small':
            return 5


class Ingredient:
    def __init__(self, name, cost):
        self.names = name
        self.cost = cost

    def get_description(self):
        return self.names


class TypeOfPizza(Pizza, Ingredient):
    def __init__(self, name, names):
        super().__init__(name, names)

    def Type(self):
        if self.name == 'Pepperoni':
            return cheese.cost + pepperoni.cost * 2
        if self.name == 'Mushroom Pizza':
            return cheese.cost + mushrooms.cost
        if self.name == 'Cheese':
            return cheese.cost * 4
        if self.name == 'Margarita':
            return cheese.cost * 2 + tomato.cost


class Topping(TypeOfPizza):
    def __init__(self, name):
        super().__init__(name)
        self.ingredient_costs = ingredient_costs

    def get_description(self):
        return self.name


def get_cost(self):
    total_cost = self.base_cost
    for ingredient_cost in self.ingredient_costs:
        total_cost += ingredient_cost
    return total_cost


# Пример использования классов

# Создаем ингредиенты
cheese = Ingredient("Cheese", 2)
tomato = Ingredient("Tomato", 1)
mushrooms = Ingredient("Mushrooms", 1.5)
pepperoni = Ingredient("Pepperoni", 2)

# Создаем топпинги, используя ингредиенты
vegetarian_topping = Topping("Vegetarian Topping", 5, [cheese.cost, tomato.cost, mushrooms.cost])
pepperoni_topping = Topping("Pepperoni Topping", 6, [cheese.cost, tomato.cost, mushrooms.cost, pepperoni.cost])

pizza2 = Topping("Custom Pizza", 8, [mushrooms.cost, cheese.cost])  # создаем пиццу со своими ингредиентами

# Выводим описание и стоимость пиццы

print(f"{pizza2.get_description()}: {pizza2.get_cost()}$")  # Output: Custom Pizza: 11.5$
