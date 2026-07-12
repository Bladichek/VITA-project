from classes import Build, Node, Team, compare_resources
from recipes import rocket_level, rockets, transport, transport_levels, builds_data


class HUB(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.title = 'Хаб'
        self.type='Хаб'
        self.description = builds_data[self.type]['description']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.max_health=float('inf')
        self.health=self.max_health
        self.recipes = builds_data[self.type]['recipes']
        self.recipe_id=0

class Builder_I(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Сборщик I'
        self.type = 'Сборщик I'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence=builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Assembler(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ассемблер'
        self.type = 'Ассемблер'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Drill_I(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Бур I'
        self.type = 'Бур I'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Smelter_I(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Плавильня I'
        self.type = 'Плавильня I'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Bridge(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Мост'
        self.type = 'Мост'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Wall(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Стена'
        self.type = 'Стена'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class RadioTower_I(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Радиовышка I'
        self.type = 'Радиовышка I'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Workbench(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Верстак'
        self.type = 'Верстак'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.recipes = [-1]
        self.price = {'Железная пластина': 2, 'Древесина': 2}
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class AnimalRepeller(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Отпугиватель животных'
        self.type = 'Отпугиватель животных'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level=2
        self.recipe_id=0

class Lumberjack(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Лесорубка'
        self.type = 'Лесорубка'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Pier(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Причал'
        self.type = 'Причал'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Storage(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory)
        self.title='Хранилище'
        self.type='Хранилище'
        self.max_connections_in = 1
        self.recipe_id=0
        self.out={}
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.recipe_id=0

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
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class WindTurbine(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ветрогенератор'
        self.type = 'Ветрогенератор'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class WaterTurbine(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Водяная турбина'
        self.type = 'Водяная турбина'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class CoalGenerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Угольный генератор'
        self.type = 'Угольный генератор'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Extractor(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Экстрактор'
        self.type = 'Экстрактор'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2

class Pump(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Помпа'
        self.type = 'Помпа'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level=2

class CementMill(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Цементная мельница'
        self.type = 'Цементная мельница'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']

class Builder_II(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Сборщик II'
        self.type = 'Сборщик II'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2

class Drill_II(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Бур II'
        self.type = 'Бур II'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2

class Foundry(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Литейная'
        self.type = 'Литейная'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2

class HydrocarbonConverter(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Углеводородный преобразователь'
        self.type = 'Углеводородный преобразователь'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2

class RadioTower_II(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Радиовышка II'
        self.type = 'Радиовышка II'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2
        self.recipe_id=0

class Turret(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Турель'
        self.type = 'Турель'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2
        self.recipe_id=0

class Spotlight(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Прожектор'
        self.type = 'Прожектор'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2
        self.recipe_id=0

class PlasmaTurret(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Плазменная турель'
        self.type = 'Плазменная турель'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2
        self.recipe_id=0

class Railgun(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Рельсотронная пушка'
        self.type = 'Рельсотронная пушка'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2
        self.recipe_id=0

class TransportHangar(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Транспортный ангар'
        self.type = 'Транспортный ангар'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2
        self.recipe_id=0

    def craft_transport(self):
        if self.is_energy_connected==False:
            return {'success': False, 'error': 'Постройка обесточена'}
        print('Доступный транспорт для производства:')
        prices = []
        for index, n in enumerate(transport_levels[self.factory.team.level]+self.factory.team.advanced_transport, start=1):
            print(f'{index}. {transport[n]["title"]} ({transport[n]["price"]})')
            prices.append(transport[n])
        n = input('Введите номер: ')
        if n.isdigit() and int(n) > 0 and int(n) <= len(prices):
            price = prices[int(n) - 1]
            res = compare_resources(price["price"], self.factory.team.resources)
            if res['success']:
                for k, v in price["price"].items():
                    self.factory.team.resources[k] = self.factory.team.resources.get(k, 0) - v
                self.factory.team.transport.append(prices[int(n) - 1])
                return {'success': True}
            else:
                return {'success': False, 'error': f'Не хватает ресурсов: {res["ost"]}'}
        else:
            return {'success': False, 'error': 'Неверный ввод'}

    def add_advanced_transport(self):
        print('Доступный для добавления транспорт:')
        keys=[]
        for i in transport_levels['advanced']:
            if i not in self.factory.team.advanced_transport:
                keys.append(i)

        for i, v in enumerate(keys, start=1):
            print(f'{i}. {transport[v]["title"]}')
        print('Введите номер:')
        n=input('Номер: ')
        if n.isdigit() and int(n)>0 and int(n)<=len(keys):
            self.factory.team.advanced_transport.append(keys[int(n)-1])
            return {'success': True}
        else:
            return {'success': False, 'error': 'Неверный ввод'}


class RocketLauncher(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ракетная установка'
        self.type = 'Ракетная установка'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2
        self.recipe_id=0

    def craft_rocket(self):
        if self.is_energy_connected==False:
            return {'success': False, 'error': 'Постройка обесточена'}
        print('Доступные ракеты для производства:')
        prices=[]
        for index, n in enumerate(rocket_level[1], start=1):
            print(f'{index}. {rockets[n]["name"]} ({rockets[n]["price"]})')
            prices.append(rockets[n])
        n=input('Введите номер: ')
        if n.isdigit() and int(n)>0 and int(n)<=len(prices):
            price=prices[int(n)-1]
            res= compare_resources(price["price"], self.factory.team.resources)
            if res['success']:
                for k, v in price["price"].items():
                    self.factory.team.resources[k]=self.factory.team.resources.get(k, 0)-v
                self.factory.team.rockets.append(price["name"])
                return {'success': True}
            else:
                return {'success': False, 'error': f'Не хватает ресурсов: {res["ost"]}'}
        else:
            return {'success': False, 'error': 'Неверный ввод'}

    def launch_rocket(self):
        if self.is_energy_connected==False:
            return {'success': False, 'error': 'Постройка обесточена'}
        print('Доступные ракеты:')
        for index, rocket in enumerate(self.factory.team.rockets, start=1):
            print(f'{index}. {rocket}')
        n=input('Введите номер: ')
        if n.isdigit() and int(n)>0 and int(n)<=len(self.factory.team.rockets):
            rocket=self.factory.team.rockets[int(n)-1]
            cargo={}
            if rocket in ['Грузовая ракета', 'Грузовая ракета дальнего действия', 'Грузовая ракета сверхдальнего действия']:
                print('Это грузовая ракета. В неё можно положить ресурсы.')
                ans = input('Положить? (Y/n): ')
                if ans.lower()=='y':
                    print('Доступные ресурсы (выберите номер и количество):')
                    resources=[]
                    s=1
                    for k, v in self.factory.team.resources.items():
                        print(f'{s}. {k} - {v}')
                        resources.append([k, v])
                        s+=1
                    pick=[]
                    n=input('Введите номер (0 для выхода): ')
                    while n != '0':
                        if n.isdigit() and int(n)>0 and int(n)<=len(resources):
                            if n not in pick:
                                resource=resources[int(n)-1]
                                print(f'Введите колтчество ресурса {resource[0]} (всего - {resource[1]})')
                                r=input()
                                if r.isdigit() and int(r)>=0 and int(r)<=resource[1]:
                                    cargo[resource[0]]=int(r)
                                    self.factory.team.resources[resource[0]]-=int(r)
                                    pick.append(n)
                                else:
                                    print('Неверный ввод')
                            else:
                                print('Этот ресурс уже погружен!')
                        else:
                            print('Неверный ввод')
                        n = input('Введите номер (0 для выхода): ')


            coords=input('Введите координаты целевой точки: ')
            self.factory.team.rockets.remove(rocket)
            self.factory.team.launched_rockets.append({'rocket': rocket, 'cargo': cargo, 'coords': coords})
            return {'success': True}



        else:
            return {'success': False, 'error': 'Неверный ввод'}


class NuclearReactor(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ядерный реактор'
        self.type = 'Ядерный реактор'
        self.max_connections_in = 2  # ядерная ячейка + вода
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2



class DieselGenerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Дизельный генератор'
        self.type = 'Дизельный генератор'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2

class DroidStation(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Станция дроидов'
        self.type = 'Станция дроидов'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.mode = 'accept'
        self.recipe_id=0
        self.profit={}
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
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 2


class RadioStation(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Радиостанция'
        self.type = 'Радиостанция'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 3
        self.recipe_id=0

class ParticleAccelerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Ускоритель частиц'
        self.type = 'Ускоритель частиц'
        self.max_connections_in = 2
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 3

class HighTempFurnace(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Высокотемпературная печь'
        self.type = 'Высокотемпературная печь'
        self.max_connections_in = 1
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 3
class LandingPad(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Посадочная площадка'
        self.type = 'Посадочная площадка'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 3
        self.recipe_id=0

class FusionReactor(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Термоядерный реактор'
        self.type = 'Термоядерный реактор'
        self.max_connections_in = 2  # тритий + вода
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 3

class ThermalGenerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Термальный генератор'
        self.type = 'Термальный генератор'
        self.max_connections_in = 0
        self.max_connections_out = 1
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 3

class AdvancedRocketLauncher(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Улучшенная ракетная установка'
        self.type = 'Улучшенная ракетная установка'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 3
        self.recipe_id=0

    def craft_rocket(self):
        if self.is_energy_connected==False:
            return {'success': False, 'error': 'Постройка обесточена'}
        print('Доступные ракеты для производства:')
        prices=[]
        for index, n in enumerate(rocket_level[2], start=1):
            print(f'{index}. {rockets[n]["name"]} ({rockets[n]["price"]})')
            prices.append(rockets[n])
        n=input('Введите номер: ')
        if n.isdigit() and int(n)>0 and int(n)<=len(prices):
            price=prices[int(n)-1]
            res= compare_resources(price["price"], self.factory.team.resources)
            if res['success']:
                for k, v in price["price"].items():
                    self.factory.team.resources[k]=self.factory.team.resources.get(k, 0)-v
                self.factory.team.rockets.append(price["name"])
                return {'success': True}
            else:
                return {'success': False, 'error': f'Не хватает ресурсов: {res["ost"]}'}
        else:
            return {'success': False, 'error': 'Неверный ввод'}

    def launch_rocket(self):
        if self.is_energy_connected==False:
            return {'success': False, 'error': 'Постройка обесточена'}
        print('Доступные ракеты:')
        for index, rocket in enumerate(self.factory.team.rockets, start=1):
            print(f'{index}. {rocket}')
        n=input('Введите номер: ')
        if n.isdigit() and int(n)>0 and int(n)<=len(self.factory.team.rockets):
            rocket=self.factory.team.rockets[int(n)-1]
            cargo={}
            if rocket in ['Грузовая ракета', 'Грузовая ракета дальнего действия', 'Грузовая ракета сверхдальнего действия']:
                print('Это грузовая ракета. В неё можно положить ресурсы.')
                ans = input('Положить? (Y/n): ')
                if ans.lower()=='y':
                    print('Доступные ресурсы (выберите номер и количество):')
                    resources=[]
                    s=1
                    for k, v in self.factory.team.resources.items():
                        print(f'{s}. {k} - {v}')
                        resources.append([k, v])
                        s+=1
                    pick=[]
                    n=input('Введите номер (0 для выхода): ')
                    while n != '0':
                        if n.isdigit() and int(n)>0 and int(n)<=len(resources):
                            if n not in pick:
                                resource=resources[int(n)-1]
                                print(f'Введите колтчество ресурса {resource[0]} (всего - {resource[1]})')
                                r=input()
                                if r.isdigit() and int(r)>=0 and int(r)<=resource[1]:
                                    cargo[resource[0]]=int(r)
                                    self.factory.team.resources[resource[0]]-=int(r)
                                    pick.append(n)
                                else:
                                    print('Неверный ввод')
                            else:
                                print('Этот ресурс уже погружен!')
                        else:
                            print('Неверный ввод')
                        n = input('Введите номер (0 для выхода): ')


            coords=input('Введите координаты целевой точки: ')
            self.factory.team.rockets.remove(rocket)
            self.factory.team.launched_rockets.append({'rocket': rocket, 'cargo': cargo, 'coords': coords})
            return {'success': True}

class ForceFieldGenerator(Build):
    def __init__(self, factory=None):
        super().__init__(factory)
        self.title = 'Генератор силового поля'
        self.type = 'Генератор силового поля'
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        self.level = 3
        self.recipe_id=0


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