from classes import Build

class Build1(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title='Тестовая постройка 1'
        self.type='Тестовая постройка 1'
        self.description='Описание первой тестовой постройки'
        self.max_connections_in=0
        self.max_connections_out=0
        self.default_energy_profit=10
        self.price={'iron_ore':1}


class HUB(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Хаб'
        self.type='Хаб'
        self.description = 'Хаб'
        self.default_energy_profit = 10
        self.max_health=float('inf')
        self.recipes = [0]
        self.recipe_id=0



class Drill_I(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title='Буровая установка I'
        self.type='Буровая установка I'
        self.description='Буровая установка первого уровня'
        self.max_connections_out=1
        self.recipes=[-1, 26]


class Smelter(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title='Плавильня'
        self.type='Плавильня'
        self.description='Плавильня'
        self.max_connections_out=1
        self.max_connections_in=1
        self.default_energy_profit = -10
        self.recipes=[-1, 5, 6]


