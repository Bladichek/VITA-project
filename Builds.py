from classes import Build, Node, Team


class HUB(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Хаб'
        self.type='Хаб'
        self.description = 'Хаб'
        self.default_energy_profit = 100
        self.max_health=float('inf')
        self.health=self.max_health
        self.recipes = [0]
        self.recipe_id=0

class Builder_I(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Сборщик I'
        self.type = 'Сборщик I'
        self.description = 'Сборщик первого уровня'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.recipes = [-1, 8, 9, 10, 14, 26, 27, 28, 29, 30, 31, 51, 57, 59]
        self.price = {'Железная пластина': 5}

class Assembler(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ассемблер'
        self.type = 'Ассемблер'
        self.description = 'Ассемблер'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.recipes = [-1, 15, 17, 18, 19, 32, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 48, 49, 50, 52, 53, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74]
        self.price = {'Железная пластина': 10}

class Drill_I(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Бур I'
        self.type = 'Бур I'
        self.description = 'Бур первого уровня'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 77, 78, 81, 90, 91, 92]
        self.price = {'Железная пластина': 3, 'Медная проволока': 1}

class Smelter_I(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Плавильня I'
        self.type = 'Плавильня I'
        self.description = 'Плавильня первого уровня'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.recipes = [-1, 5, 6, 11, 16, 55, 56]
        self.price = {'Железный корпус': 5, 'Цемент': 5}

class Bridge(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Мост'
        self.type = 'Мост'
        self.description = 'Мост'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Железная пластина': 5, 'Бетон': 5}

class Wall(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Стена'
        self.type = 'Стена'
        self.description = 'Стена'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Бетон': 10}

class RadioTower_I(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Радиовышка I'
        self.type = 'Радиовышка I'
        self.description = 'Радиовышка первого уровня'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Железная пластина': 3, 'Медная проволока': 1}

class Workbench(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Верстак'
        self.type = 'Верстак'
        self.description = 'Верстак первого уровня'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.recipes = [-1]
        self.price = {'Железная пластина': 2, 'Древесина': 2}

class AnimalRepeller(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Отпугиватель животных'
        self.type = 'Отпугиватель животных'
        self.description = 'Отпугиватель животных'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Железная пластина': 2, 'ЭМ катушка': 1}
        self.level=2

class Lumberjack(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Лесорубка'
        self.type = 'Лесорубка'
        self.description = 'Лесорубка первого уровня'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 82]
        self.price = {'Железная пластина': 2, 'Шестерни': 1}

class Pier(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Причал'
        self.type = 'Причал'
        self.description = 'Причал'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Древесина': 5, 'Железный корпус': 2}

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
        self.price = {'Железная пластина': 2}

    def update_res(self):
        if self.connection_in1 is not None:
            self.out=self.connection_in1.res.copy()
        else:
            self.out={}
        self.factory.team.update_produce()


class SolarPanel(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Солнечная панель'
        self.type = 'Солнечная панель'
        self.description = 'Солнечная панель'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 94]
        self.price = {'Стекло': 5, 'Железная пластина': 1}

class WindTurbine(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ветрогенератор'
        self.type = 'Ветрогенератор'
        self.description = 'Ветрогенератор'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 95]
        self.price = {'Железная пластина': 10, 'Шестерни': 5}

class WaterTurbine(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Водяная турбина'
        self.type = 'Водяная турбина'
        self.description = 'Водяная турбина'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 96]
        self.price = {'Железный корпус': 5, 'Шестерни': 5}

class CoalGenerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Угольный генератор'
        self.type = 'Угольный генератор'
        self.description = 'Угольный генератор'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.recipes = [-1, 97, 98]
        self.price = {'Железный корпус': 8, 'Шестерни': 4}

class Extractor(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Экстрактор'
        self.type = 'Экстрактор'
        self.description = 'Экстрактор'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 84, 89]
        self.price = {'Железный корпус': 5, 'Набор труб': 2, 'Мотор': 1}
        self.level = 2

class Pump(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Помпа'
        self.type = 'Помпа'
        self.description = 'Помпа'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 83]
        self.price = {'Железный корпус': 3, 'Мотор': 1}
        self.level=2

class CementMill(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Цементная мельница'
        self.type = 'Цементная мельница'
        self.description = 'Цементная мельница'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.recipes = [-1, 13]
        self.price = {'Железный корпус': 8, 'Шестерни': 4}

class Builder_II(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Сборщик II'
        self.type = 'Сборщик II'
        self.description = 'Сборщик второго уровня'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.recipes = [-1, 1, 2, 4, 7, 33, 34, 44, 47, 58, 8, 9, 10, 14, 26, 27, 28, 29, 30, 31, 51, 57, 59]
        self.price = {'Железная пластина': 10, 'Медная проволока': 5, 'Алюминий': 3}
        self.level = 2

class Drill_II(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Бур II'
        self.type = 'Бур II'
        self.description = 'Бур второго уровня'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 79, 80, 86, 88, 93]
        self.price = {'Железная пластина': 5, 'Медная проволока': 2, 'Шестерни': 2, 'Железный корпус': 1}
        self.level = 2

class Foundry(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Литейная'
        self.type = 'Литейная'
        self.description = 'Литейная'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.recipes = [-1, 3, 12, 54]
        self.price = {'Железный корпус': 12, 'Цемент': 6}
        self.level = 2

class HydrocarbonConverter(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Углеводородный преобразователь'
        self.type = 'Углеводородный преобразователь'
        self.description = 'Углеводородный преобразователь'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.recipes = [-1, 21, 22, 23, 24, 25]
        self.price = {'Железный корпус': 10, 'Мотор': 3}
        self.level = 2

class RadioTower_II(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Радиовышка II'
        self.type = 'Радиовышка II'
        self.description = 'Радиовышка второго уровня'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Железная пластина': 5, 'Медная проволока': 3, 'Процессор': 1}
        self.level = 2

class Turret(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Турель'
        self.type = 'Турель'
        self.description = 'Турель'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Железный корпус': 10, 'Болты': 5, 'Мотор': 2}
        self.level = 2

class Spotlight(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Прожектор'
        self.type = 'Прожектор'
        self.description = 'Прожектор'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Стекло': 2, 'Железный корпус': 1}
        self.level = 2

class PlasmaTurret(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Плазменная турель'
        self.type = 'Плазменная турель'
        self.description = 'Плазменная турель'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Высокотехнологичная обшивка': 10, 'ЭМ стабилизатор плазмы': 2, 'Аккумулятор': 5}
        self.level = 2

class Railgun(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Рельсотронная пушка'
        self.type = 'Рельсотронная пушка'
        self.description = 'Рельсотронная пушка'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Титановый корпус': 5, 'Магнит': 3, 'ЭМ катушка': 2}
        self.level = 2

class TransportHangar(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Транспортный ангар'
        self.type = 'Транспортный ангар'
        self.description = 'Транспортный ангар'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Железный корпус': 20, 'Алюминиевый корпус': 5}
        self.level = 2

class RocketLauncher(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ракетная установка'
        self.type = 'Ракетная установка'
        self.description = 'Ракетная установка'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Железный корпус': 15, 'Двигатель': 5, 'Радиопередатчик': 3}
        self.level = 2

class NuclearReactor(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ядерный реактор'
        self.type = 'Ядерный реактор'
        self.description = 'Ядерный реактор'
        self.max_connections_in = 2  # ядерная ячейка + вода
        self.max_connections_out = 1
        self.recipes = [-1, 100]
        self.price = {'Железный корпус': 20, 'Бетон': 10, 'Ядерная ячейка': 5, 'Модуль контроля температуры': 5}
        self.level = 2



class DieselGenerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Дизельный генератор'
        self.type = 'Дизельный генератор'
        self.description = 'Дизельный генератор'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.recipes = [-1, 99]
        self.price = {'Железный корпус': 10, 'Мотор': 5, 'Бочка': 3}
        self.level = 2

class DroidStation(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Станция дроидов'
        self.type = 'Станция дроидов'
        self.description = 'Станция дроидов'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.recipes = [-1]
        self.price = {'Пластмассовый корпус': 5, 'Аккумулятор': 2}
        self.mode = 'accept'
        self.profit={}
        self.current_energy_profit=-10
        self.level = 2

    def update_res(self):
        if self.mode=='accept':
            if self.connection_in1 is not None:
                self.profit=self.connection_in1.res
            else:
                self.profit={}
        else:
            if self.profit != {}:
                k = list(self.profit.keys())[0]
                if self.is_energy_connected:

                    if self.factory.team.droids_profit[k]>=0:
                        self.out={'output1': self.profit, 'output2': {}}
                    else:
                        print(f'Недостаточно ресурсов на станции дроидов {self.title} фабрики {self.factory.title}! Производство остановлено')
                        self.is_energy_connected=False
                        return self.update_res()
                else:
                    if self.factory.team.droids_profit[k]-self.profit[k]>=0:
                        print('Подача ресурсов восстановлена!')
                        self.is_energy_connected=True
                        return self.update_res()
                    else:
                        self.out={'output1': {}, 'output2': {} }

            if self.connection_out1 is not None:
                self.connection_out1.add_res()
                self.connection_out1.output_build.update_res()
        self.factory.team.update_droids()

    def set_recipe(self, recipe_id):
        self.recipe_id=-1
        self.update_res()


    def set_profit(self):
        print('Доступные ресурсы:')
        s=1
        r=[]
        for k, v in self.factory.team.droids_profit.items():
            print(f'{s}. {k} - {v}')
            r.append([k,v])
            s+=1
        n=input('Введите номер ресурса: ')
        if not (n.isdigit() and int(n)<=len(r)):
            return {'success': False, 'error': 'Неверный ввод'}
        n1=input('Введите количество ресурса: ')
        if not (n1.isdigit() and int(n1)>0 and int(n1)<=r[int(n)-1][1]):
            return {'success': False, 'error': 'Неверный ввод'}
        self.profit={r[int(n)-1][0]: int(n1)}
        self.update_res()
        self.factory.team.update_droids()
        return {'success': True}




class GasExtractor(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Газовый экстрактор'
        self.type = 'Газовый экстрактор'
        self.description = 'Газовый экстрактор'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 85, 87]
        self.price = {'Железный корпус': 5, 'Набор труб': 3, 'Мотор': 1}
        self.level = 2


class RadioStation(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Радиостанция'
        self.type = 'Радиостанция'
        self.description = 'Радиостанция третьего уровня'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Железная пластина': 10, 'Медная проволока': 5, 'Процессор': 2, 'Радиопередатчик': 1}
        self.level = 3

class ParticleAccelerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ускоритель частиц'
        self.type = 'Ускоритель частиц'
        self.description = 'Ускоритель частиц'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.recipes = [-1, 69, 70, 75, 76]
        self.price = {'Высокотехнологичная обшивка': 30, 'Сверхпроводящий сплав': 10,
                      'Ядро ИИ': 5, 'ЭМ стабилизатор плазмы': 5}
        self.level = 3

class HighTempFurnace(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Высокотемпературная печь'
        self.type = 'Высокотемпературная печь'
        self.description = 'Высокотемпературная печь'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.recipes = [-1, 20]
        self.price = {'Железный корпус': 20, 'Цемент': 10, 'Иридий': 5}
        self.level = 3
class LandingPad(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Посадочная площадка'
        self.type = 'Посадочная площадка'
        self.description = 'Посадочная площадка'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Бетон': 25, 'Алюминиевый корпус': 10}
        self.level = 3

class FusionReactor(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Термоядерный реактор'
        self.type = 'Термоядерный реактор'
        self.description = 'Термоядерный реактор'
        self.max_connections_in = 2  # тритий + вода
        self.max_connections_out = 1
        self.recipes = [-1, 101]
        self.price = {'Высокотехнологичная обшивка': 40, 'Сверхпроводящий сплав': 10,
                     'Квантовый чип': 5, 'Тритий': 10}
        self.level = 3

class ThermalGenerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Термальный генератор'
        self.type = 'Термальный генератор'
        self.description = 'Термальный генератор'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.recipes = [-1, 102]
        self.price = {'Железный корпус': 15, 'Бетон': 10, 'Модуль контроля температуры': 1}
        self.level = 3

class AdvancedRocketLauncher(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Улучшенная ракетная установка'
        self.type = 'Улучшенная ракетная установка'
        self.description = 'Улучшенная ракетная установка'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Титановый корпус': 20, 'Реактивный двигатель': 8, 'Контроллер ИИ роя': 5}
        self.level = 3

class ForceFieldGenerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Генератор силового поля'
        self.type = 'Генератор силового поля'
        self.description = 'Генератор силового поля'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.recipes = [-1]
        self.price = {'Высокотехнологичная обшивка': 25, 'ЭМ стабилизатор плазмы': 10, 'Аккумулятор': 5}
        self.level = 3


builds = [
    Node,
    HUB,
    Builder_I,
    Assembler,
    Drill_I,
    Smelter_I,
    Bridge,
    Wall,
    RadioTower_I,
    Workbench,
    AnimalRepeller,
    Lumberjack,
    Pier,
    Storage,
    SolarPanel,
    WindTurbine,
    WaterTurbine,
    CoalGenerator,
    Extractor,
    Pump,
    CementMill,
    Builder_II,
    Drill_II,
    Foundry,
    HydrocarbonConverter,
    RadioTower_II,
    Turret,
    Spotlight,
    PlasmaTurret,
    Railgun,
    TransportHangar,
    RocketLauncher,
    NuclearReactor,
    DieselGenerator,
    DroidStation,
    GasExtractor,
    RadioStation,
    ParticleAccelerator,
    HighTempFurnace,
    LandingPad,
    FusionReactor,
    ThermalGenerator,
    AdvancedRocketLauncher,
    ForceFieldGenerator,
]