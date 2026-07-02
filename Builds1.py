from classes import Build, Node



class HUB(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Хаб'
        self.type='Хаб'
        self.description = 'Хаб'
        self.default_energy_profit = 100
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


class Storage(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory)
        self.title='Хранилище'
        self.type='Хранилище'
        self.description='Это хранилище'
        self.max_connections_in = 1
        self.default_energy_profit =0
        self.recipes=[0]
        self.recipe_id=0
        self.out={}

    def update_res(self):
        if self.connection_in1 is not None:
            self.out=self.connection_in1.res.copy()
        else:
            self.out={}



class Builder_I(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title='Cборщик I'
        self.type='Cборщик I'
        self.description='Сборщик первого уровня'
        self.max_connections_out=1
        self.max
        self.recipes=[-1, 8, 9, 10, 14, 26, 27, 28, 29, 30, 31, 51, 57, 59]
        self.price={'Железная пластина': 5,
                    'Медная проволока': 2,
                    'Шестерни': 2
                    }



class Builder_I(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Сборщик I'
        self.type = 'Сборщик I'
        self.description = 'Сборщик первого уровня'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class Assembler_I(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Ассемблер I'
        self.type = 'Ассемблер I'
        self.description = 'Ассемблер первого уровня'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class Bridge(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Мост'
        self.type = 'Мост'
        self.description = 'Мост для соединения конструкций'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class Wall(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Стена'
        self.type = 'Стена'
        self.description = 'Защитная стена'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class RadioTower_I(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Радиовышка I'
        self.type = 'Радиовышка I'
        self.description = 'Радиовышка первого уровня'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class Workbench(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Верстак'
        self.type = 'Верстак'
        self.description = 'Верстак для крафта'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class AnimalRepeller(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Отпугиватель животных'
        self.type = 'Отпугиватель животных'
        self.description = 'Отпугивает диких животных'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class Sawmill(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Лесорубка'
        self.type = 'Лесорубка'
        self.description = 'Добывает древесину'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class Pier(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Причал'
        self.type = 'Причал'
        self.description = 'Причал для кораблей'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class StorageTerminal(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Терминал хранилища'
        self.type = 'Терминал хранилища'
        self.description = 'Управление хранилищем'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class SolarPanel(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Солнечная панель'
        self.type = 'Солнечная панель'
        self.description = 'Генерирует энергию из солнечного света'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class WindGenerator(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Ветрогенератор'
        self.type = 'Ветрогенератор'
        self.description = 'Генерирует энергию из ветра'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class WaterTurbine(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Водяная турбина'
        self.type = 'Водяная турбина'
        self.description = 'Генерирует энергию из воды'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class CoalGenerator(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Угольный генератор'
        self.type = 'Угольный генератор'
        self.description = 'Генерирует энергию из угля'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class Extractor(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Экстрактор'
        self.type = 'Экстрактор'
        self.description = 'Добывает ресурсы'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class Pump(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Помпа'
        self.type = 'Помпа'
        self.description = 'Перекачивает жидкости'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


class CementMill(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Цементная мельница'
        self.type = 'Цементная мельница'
        self.description = 'Производит цемент'
        self.level = 1
        self.max_connections_out = 1
        self.recipes = [-1]


# ==================== УРОВЕНЬ II ====================

class Builder_II(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Сборщик II'
        self.type = 'Сборщик II'
        self.description = 'Сборщик второго уровня'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class Assembler_II(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Ассемблер II'
        self.type = 'Ассемблер II'
        self.description = 'Ассемблер второго уровня'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class Drill_II(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Бур II'
        self.type = 'Бур II'
        self.description = 'Бур второго уровня'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class MiningRig_I(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Добывающая установка I'
        self.type = 'Добывающая установка I'
        self.description = 'Добывающая установка первого уровня'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class Foundry(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Литейная'
        self.type = 'Литейная'
        self.description = 'Плавит руду в слитки'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class HydrocarbonConverter(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Углеводородный преобразователь'
        self.type = 'Углеводородный преобразователь'
        self.description = 'Преобразует углеводороды'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class Mixer(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Смеситель'
        self.type = 'Смеситель'
        self.description = 'Смешивает компоненты'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class RadioTower_II(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Радиовышка II'
        self.type = 'Радиовышка II'
        self.description = 'Радиовышка второго уровня'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class Turret(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Турель'
        self.type = 'Турель'
        self.description = 'Автоматическая турель'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class Spotlight(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Прожектор'
        self.type = 'Прожектор'
        self.description = 'Освещает большую территорию'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class PlasmaTurret(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Плазменная турель'
        self.type = 'Плазменная турель'
        self.description = 'Турель с плазменным оружием'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class Railgun(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Рельсотронная пушка'
        self.type = 'Рельсотронная пушка'
        self.description = 'Мощное рельсотронное орудие'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class TransportHangar(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Транспортный ангар'
        self.type = 'Транспортный ангар'
        self.description = 'Хранилище транспорта'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class RocketLauncher(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Ракетная установка'
        self.type = 'Ракетная установка'
        self.description = 'Запускает ракеты'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class NuclearReactor(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Ядерный реактор'
        self.type = 'Ядерный реактор'
        self.description = 'Генерирует энергию из ядерного топлива'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class WasteSarcophagus(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Саркофаг отходов'
        self.type = 'Саркофаг отходов'
        self.description = 'Хранилище радиоактивных отходов'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class DieselGenerator(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Дизельный генератор'
        self.type = 'Дизельный генератор'
        self.description = 'Генерирует энергию из дизельного топлива'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class DroneStation(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Станция дроидов'
        self.type = 'Станция дроидов'
        self.description = 'Управление дроидами'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class MolecularSynthesizer(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Молекулярный синтезатор'
        self.type = 'Молекулярный синтезатор'
        self.description = 'Синтезирует молекулы'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class Splitter(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Сплиттер'
        self.type = 'Сплиттер'
        self.description = 'Разделяет потоки ресурсов'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


class GasExtractor(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Газовый экстрактор'
        self.type = 'Газовый экстрактор'
        self.description = 'Добывает газ'
        self.level = 2
        self.max_connections_out = 1
        self.recipes = [-1]


# ==================== УРОВЕНЬ III ====================

class Builder_III(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Сборщик III'
        self.type = 'Сборщик III'
        self.description = 'Сборщик третьего уровня'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class Assembler_III(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Ассемблер III'
        self.type = 'Ассемблер III'
        self.description = 'Ассемблер третьего уровня'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class Drill_III(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Бур III'
        self.type = 'Бур III'
        self.description = 'Бур третьего уровня'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class MiningRig_II(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Добывающая установка II'
        self.type = 'Добывающая установка II'
        self.description = 'Добывающая установка второго уровня'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class RadioStation(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Радиостанция'
        self.type = 'Радиостанция'
        self.description = 'Мощная радиостанция для связи'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class ParticleAccelerator(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Ускоритель частиц'
        self.type = 'Ускоритель частиц'
        self.description = 'Разгоняет элементарные частицы'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class HighTempFurnace(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Высокотемпературная печь'
        self.type = 'Высокотемпературная печь'
        self.description = 'Плавит при экстремально высоких температурах'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class LandingPad(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Посадочная площадка'
        self.type = 'Посадочная площадка'
        self.description = 'Для посадки кораблей'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class ThermonuclearReactor(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Термоядерный реактор'
        self.type = 'Термоядерный реактор'
        self.description = 'Генерирует энергию за счет термоядерной реакции'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class ThermalGenerator(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Термальный генератор'
        self.type = 'Термальный генератор'
        self.description = 'Генерирует энергию из тепла'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class ImprovedRocketLauncher(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Улучшенная ракетная установка'
        self.type = 'Улучшенная ракетная установка'
        self.description = 'Улучшенная ракетная установка'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


class ForceFieldGenerator(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Генератор силового поля'
        self.type = 'Генератор силового поля'
        self.description = 'Создает защитное силовое поле'
        self.level = 3
        self.max_connections_out = 1
        self.recipes = [-1]


builds = [Drill_I, HUB, Smelter, Node, Storage]