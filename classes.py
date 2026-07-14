from recipes import recipes, recipes_level, craft_recipes, craft_levels, prices, resources, builds_data
from math import erf, ceil
from random import choice
from numpy import random


class World:
    def __init__(self, difficulty: int=5):
        self.teams=[]
        self.difficulty = difficulty
        self.day = 1


    def add_team(self, team):
        self.teams.append(team)

    def remove_team(self):
        for i in range(len(self.teams)):
            print(f'{i+1}. {self.teams[i].title}')
        n = int(input())
        if n<1 or n>len(self.teams):
            print('Неверно указанное значение, попробуйте снова')
            return False
        self.teams.pop(n-1)
        print('Команда успешно удалена!')

    def stats(self):
        pass

    def update_day(self):
        result={}
        self.day+=1
        for team in self.teams:
            res=team.hit(difficulty=self.difficulty)
            if res['success']:
                result[team.title]=res['result']

        for team in self.teams:
            for k, v in team.produce.items():
                if k=='energy':
                    continue
                team.resources[k]=team.resources.get(k, 0)+v
            team.update_drin_res()
        return {'success': True, 'result': result}




class Team:
    def __init__(self, title: str='team'):
        self.title = title
        self.resources = {}
        self.energy = 0
        self.factories = []
        self.is_energy_active = True
        self.produce = {}
        self.factories_names=[]
        self.droids_profit={}
        self.drin = 0
        self.drin_resources = {}
        self.players={}
        self.grabbed_resources = {}
        self.level = 1
        self.rockets=[]
        self.launched_rockets=[]
        self.transport=[]
        self.advanced_transport=[]

    def add_factory(self, factory):
        self.factories.append(factory)

    def hit(self, difficulty: int):
        result={}
        for fac in self.factories:
            res=fac.hit(difficulty)
            if res['success']:
                result[fac.title]=res['result']
        self.update()
        return {'success': True, 'result': result}



    def update_drin_res(self):
        res={}
        for k, v in self.resources.items():
            res[k]=round(v*self.drin/100)
        self.drin_resources = res
        return {'success': True}


    def craft(self, player_id: int):


        player_res={}
        for k, v in self.drin_resources.items():
            player_res[k] = player_res.get(k, 0)+v
        for i in self.players[player_id]['inventory']:
            player_res[i]=player_res.get(i, 0)+1


        print('Крафты:')
        rec=[]
        s=1
        player_recipes = [x  for x in craft_recipes.keys() if x in craft_levels[self.level]]+self.players[player_id]['advanced_recipes']
        for k in player_recipes:
            v = craft_recipes[k]
            print(f'{s}. {v["object"]} ({v["resources"]})')
            rec.append(v)
            s+=1

        n=input('Введите номер крафта: ')
        if not (n.isdigit() and int(n)>0 and int(n)<=len(rec)):
            return {'success': False, 'error': 'Неверный ввод'}
        cur_craft = rec[int(n)-1]

        price = cur_craft['resources']
        f = True
        ost = {}
        for k, v in price.items():
            if player_res.get(k, 0) < v:
                f = False
                ost[k] = v - player_res.get(k, 0)
        if f == False:
            print('Недостаточно ресурсов для крафта:')
            for k, v in ost.items():
                print(f'Не хватает {v} ресурса {k}')
            print()
            return {'success': False, 'error': 'Не хватает ресурсов'}

        else:
            for k, v in price.items():
                if k in self.players[player_id]['inventory']:
                    for i in range(v):
                        self.players[player_id]['inventory'].remove(k)
                elif k in self.drin_resources.keys():
                    self.drin_resources[k]-=v
                    self.resources[k]-=v
            self.players[player_id]['inventory'].append(cur_craft['object'])
            return {'success': True}


    def buy(self, player):
        s=1
        print('Выберите покупку из списка:')
        buys=[]
        for k, v in prices.items():
            print(f'{s}. {k} ({v["price"]} кредИТов)')
            buys.append([k, v])
            s+=1
        n=input('Введите номер: ')
        if (not n.isdigit()) or int(n)<1 or int(n)>len(buys):
            return {'success': False, 'error': 'Неверный ввод'}
        item=buys[int(n)-1]
        if item[1]['price']>player['balance']:
            return {'success': False, 'error': f'Не хватает {item[1]["price"]-player["balance"]} кредИТов'}
        if item[1]['item']==None:
            player['inventory'].append(item[0])
            player['balance']-=item[1]['price']
            return {'success': True}
        else:
            if item[1]['item'] in player['advanced_recipes']:
                return {'success': False, 'error': ' Нельзя купить один и тот же чертёж больше 1 раза!'}
            else:
                player['advanced_recipes'].append(item[1]['item'])
                return {'success': True}



    def remove_factory(self):
        for i in range(len(self.factories)):
            print(f'{i+1}. {self.factories[i].title}')
        n = int(input())
        if n<1 or n>len(self.factories):
            print('Неверно указанное значение, попробуйте снова')
            return False
        self.factories.pop(n-1)
        print('Фабрика успешно удалена!')

    def add_res(self, resource, amount):
        if resource not in resources:
            return {'success': False, 'error': 'Нет такого типа ресурсов'}
        self.resources[resource] = self.resources.get(resource, 0) + amount
        return {'success': True}

    def set_res(self, resource, amount):
        if resource not in resources:
            return {'success': False, 'error': 'Нет такого типа ресурсов'}
        self.resources[resource]=amount
        return {'success': True}

    def res(self):
        for k, v in self.resources.items():
            print(f'{k}: {v}')

    def update_produce(self):
        self.produce = {}
        for fac in self.factories:
            fac.profit = {}
            for b in fac.builds:
                if b.type == 'Хранилище':
                    for k, v in b.out.items():
                        fac.profit[k] = fac.profit.get(k, 0) + v
            for k, v in fac.profit.items():
                self.produce[k] = self.produce.get(k, 0) + v

    def update(self):
        for _ in range(2):
            self.update_produce()
            self.update_droids()
            for fac in self.factories:
                fac.profit={}
                for b in fac.builds:
                    b.set_recipe(b.recipe_id)
                self.update_energy()
                self.update_drin_res()
    def update_droids(self):
        old_profit = self.droids_profit.copy()
        self.droids_profit = {}
        for fac in self.factories:
            for b in fac.builds:
                if b.type == 'Станция дроидов':
                    if b.profit != {}:
                        res = list(b.profit.keys())[0]
                        amount = list(b.profit.values())[0]
                        if b.mode == 'accept':
                            self.droids_profit[res] = self.droids_profit.get(res, 0) + amount*b.is_energy_connected
                        else:
                            self.droids_profit[res] = self.droids_profit.get(res, 0) - amount*b.is_energy_connected
        changes = self.change_profit(old_profit, self.droids_profit)
        for fac in self.factories:
            for b in fac.builds:
                if b.type == 'Станция дроидов':
                    f=False
                    for i in changes:
                        if i in list(b.profit.keys()):
                            f=True
                            break
                    if f:
                        if b.mode=='donor':
                            b.update_res()
    def change_profit(self, old_profit, new_profit):
        changes=[]
        for k, v in new_profit.items():
            if v != old_profit.get(k, 0):
                changes.append(k)
        return changes

    def update_energy(self):
        energy = 0
        for fac in self.factories:
            fac.profit['energy']=0
            for build in fac.builds:
                if build.is_energy_connected:
                    energy += build.current_energy_profit
                    fac.profit['energy']+=build.current_energy_profit

        self.energy = energy
        if energy < 0:
            print('Сбой питания! Стройте генераторы или снизьте нагрузку на электросеть!')
            self.is_energy_active=False
        else:
            if self.is_energy_active==False:
                print('Питание восстановлено!')
            self.is_energy_active=True
    def fix_price(self):
        res={}
        for fac in self.factories:
            for k, v in fac.fix_price().items():
                if v == 0:
                    continue
                res[k] = res.get(k, 0) + v
        return res

    def fix_all(self):
        r=compare_resources(self.fix_price(), self.resources)
        if r['success']:
            for fac in self.factories:
                fac.fix_all()
            return {'success': True}
        else:
            return {'success': False, 'result': f'Не хватает ресурсов: {r["ost"]}'}
    def fix_factory(self, factory):
        r=compare_resources(factory.fix_price(), self.resources)
        if r['success']:
            factory.fix_all()
            return {'success': True}
        else:
            return {'success': False, 'result': f'Не хватает ресурсов: {r["ost"]}'}


    def get_energy(self):
        all_in_all=[]
        waste=[]
        produce=[]
        all_waste=0
        all_produce=0

        for fac in self.factories:
            all_in_all.append([fac.title, fac.profit['energy']])
            fac_waste=0
            fac_produce=0
            for b in fac.builds:
                if b.is_energy_connected*b.current_energy_profit>0:
                    fac_produce+=b.is_energy_connected*b.current_energy_profit
                else:
                    fac_waste+=abs(b.is_energy_connected*b.current_energy_profit)
            waste.append([fac.title, fac_waste])
            produce.append([fac.title, fac_produce])
            all_waste+=fac_waste
            all_produce+=fac_produce
        all_in_all.sort(key=lambda x: -x[1])
        waste.sort(key=lambda x: -x[1])
        produce.sort(key=lambda x: -x[1])
        return {'success': True, 'result':
            {'all': all_in_all,
             'waste': waste,
             'produce': produce,
             'all_waste': all_waste,
             'all_produce': all_produce}}




class Factory:
    def __init__(self, team, title: str='factory'):
        self.title = title
        self.builds = []
        self.profit = {'energy': 0}
        self.team = team
        self.team.add_factory(self)

    def build(self, build):
        price = build.price
        f=True
        ost={}
        for k,v in price.items():
            if self.team.resources.get(k, 0) < v:
                f=False
                ost[k]=v-self.team.resources.get(k, 0)
        if f == False:
            print('Недостаточно ресурсов для постройки:')
            for k, v in ost.items():
                print(f'Не хватает {v} ресурса {k}')
            print()
            return False
        else:
            for k, v in price.items():
                self.team.resources[k]-=v
            self.builds.append(build)
            build.factory=self
            self.team.update()
            print('Постройка успешно построена!')
            return True

    def destroy(self):
        for i in range(len(self.builds)):
            print(f'{i+1}. {self.builds[i].title}')
        n = int(input())
        if n < 1 or n > len(self.builds):
            print('Неверно указанное значение, попробуйте снова')
            return False
        b=self.builds[n-1]
        self.destroy_build(b, res=True)
        return True

    def hit(self, difficulty):
        damaged_builds=[]
        destroyed_builds=[]
        c=input('Бросьте кубик д6 на количество повреждённых построек: ')
        while not(c.isdigit() and int(c)>0 and int(c)<=6):
            c = input('Бросьте кубик д6 на количество повреждённых построек: ')

        count=round(len(self.builds)*int(c)/6)

        factory_protect=0
        for b in self.builds:
            factory_protect+=b.defence*b.is_energy_connected
        for i in count:
            build=choice(self.builds)
            while (build in [x[0] for x in destroyed_builds]) or (build in [x[0] for x in damaged_builds]):
                build = choice(self.builds)
            local_difficulty=round(random.normal(difficulty**1.5, (difficulty**1.5)/10)*(1-erf(factory_protect/100)))
            build.health=max(build.health-local_difficulty, 0)
            if build.health == 0:
                self.destroy_build(build)
                destroyed_builds.append([build, local_difficulty])
            else:
                damaged_builds.append([build, local_difficulty])

        return {'success': True, 'result': {'damaged_builds': damaged_builds, 'destroyed_builds': destroyed_builds}}
    def destroy_build(self, build, res=False):
        self.builds.remove(build)
        for c in (build.connection_in1, build.connection_in2, build.connection_out1, build.connection_out2):
            if c is not None:
                c.remove_connection()
        if res:
            print('Постройка успешно демонтирована!')
            coff=build.health/build.max_health
            print('Ресурсов получено:')
            for k, v in build.destroy_price.items():
                print(f'Получено {round(v*coff)} ресурса {k})')
                self.team.resources[k]=self.team.resources.get(k, 0)+round(v*coff)
            self.team.update()

        return {'success': True}

    def fix_price(self):
        res={}
        for b in self.builds:
            for k, v in b.fix_price().items():
                if v == 0:
                    continue
                res[k]=res.get(k, 0)+v
        return res

    def fix_all(self):
        all_res={}
        for build in self.builds:
            res=build.fix_price()
            for k, v in res.items():
                all_res[k]=all_res.get(k, 0)+v
        r=compare_resources(all_res, self.team.resources)
        if r['success']:
            for b in self.builds:
                b.fix()
            for k, v in all_res.items():
                self.team.resources[k]-=v
            return {'success': True}
        else:
            return {'success': False, 'result': f'Не хватает ресурсов: {r["ost"]}'}

    def fix_build(self, build):
        r=compare_resources(build.fix_price(), self.team.resources)
        if r['success']:

            for k, v in build.fix_price().items():
                self.team.resources[k] -= v
            build.fix()
            return {'success': True}
        else:
            return {'success': False, 'result': f'Не хватает ресурсов: {r["ost"]}'}






class Build:
    def __init__(self, factory=None):
        self.price={}
        self.destroy_price={}
        self.title = ''
        self.type=''
        self.description = ''
        self.recipe_id = -1
        self.connection_in1 = None
        self.connection_in2 = None
        self.connection_out1 = None
        self.connection_out2 = None
        self.max_connections_in = 0
        self.max_connections_out = 0
        self.max_health = 100
        self.health = self.max_health
        self.default_energy_profit = -10
        self.current_energy_profit = 0
        self.is_energy_connected = True
        self.factory=factory
        self.efficiency = 1
        self.out={'output1': {}, 'output2': {}}
        self.recipes=[-1]
        self.level=1
        self.defence = 0

    def add_connection_in(self, connection, number: int=1):
        if number==1:
            if self.connection_in1!=None:
                print('Порт уже занят')
                return False
            else:
                self.connection_in1=connection
        elif number==2:
            if self.connection_in2!=None:
                print('Порт уже занят')
                return False
            else:
                self.connection_in2=connection
        else:
            print('Неверный аргумент (порты 1 или 2)')
            return False
        connection.output_build = self
        self.update_res()
        print('Соединение успешно создано')
        return True

    def add_connection_out(self, connection, number: int=1):
        if number == 1:
            if self.connection_out1 != None:
                print('Порт уже занят')
                return False
            else:
                self.connection_out1 = connection
        elif number == 2:
            if self.connection_out2 != None:
                print('Порт уже занят')
                return False
            else:
                self.connection_out2 = connection
        else:
            print('Неверный аргумент (порты 1 или 2)')
            return False
        connection.input_build = self
        print('Соединение успешно создано')
        connection.add_res()
        if connection.output_build != None:
            connection.output_build.update_res()
        return True

    def remove_connection(self):
        s=1
        connections_in=[x  for x in [self.connection_in1, self.connection_in2] if x!= None]
        connections_out=[x  for x in [self.connection_out1, self.connection_out2] if x!= None]
        connections = connections_in+connections_out
        if connections_in:
            print('Входы:')
            for i in connections_in:
                #print(i)
                print(f'{s}. {i.info()}')
                s+=1

        if connections_out:
            print('Выходы')
            for i in connections_out:
                print(f'{s}. {i.info()}')
        n=int(input('Введите номер для удаления: '))
        if n>len(connections) or n<1:
            print('Неверно введённый номер')
            return False
        connections[n-1].remove_connection()
        print('Соединение успешно удалено')
        return connections[n-1]

    def set_recipe(self, recipe_id):
        if recipe_id not in self.recipes:
            print('У этой постройки нет такого рецепта')
            return None
        if self.recipe_id==-1 and recipe_id!=-1:
            self.is_energy_connected=True
        self.recipe_id=recipe_id
        self.update_res()

    def update_res(self):
        self.description = builds_data[self.type]['description']
        self.recipes = builds_data[self.type]['recipes']
        self.price = builds_data[self.type]['price']
        self.destroy_price = builds_data[self.type]['destroy_price']
        self.defence = builds_data[self.type]['defence']
        self.default_energy_profit = builds_data[self.type]['default_energy_profit']
        coff = [1]
        if self.recipe_id==-1:
            self.is_energy_connected=False

        necessary_resources1 = recipes[self.recipe_id]['input1']
        if necessary_resources1 != {}:
            for k, v in necessary_resources1.items():
                cur_res = 0
                if self.connection_in1 != None:
                    cur_res += self.connection_in1.res.get(k, 0)
                if cur_res == 0:
                    print('Недостаточно ресурсов. Постройка неактивна')
                    self.current_energy_profit = 0
                    self.out['output1'] = {}
                    self.out['output2'] = {}
                    self.factory.team.update_energy()
                    for con in (self.connection_out1, self.connection_out2):
                        if con is not None:
                            con.add_res()
                            if con.output_build is not None:
                                con.output_build.update_res()
                    return False
                elif cur_res < v:
                    coff.append(cur_res / v)
        necessary_resources2 = recipes[self.recipe_id]['input2']
        if necessary_resources2 != {}:
            for k, v in necessary_resources2.items():
                cur_res = 0
                if self.connection_in2 != None:
                    cur_res += self.connection_in2.res.get(k, 0)
                if cur_res == 0:
                    print('Недостаточно ресурсов. Постройка неактивна')
                    self.current_energy_profit = 0
                    self.out['output1'] = {}
                    self.out['output2'] = {}
                    self.factory.team.update_energy()
                    for con in (self.connection_out1, self.connection_out2):
                        if con is not None:
                            con.add_res()
                            if con.output_build is not None:
                                con.output_build.update_res()
                    return False
                elif cur_res < v:
                    coff.append(cur_res / v)

        if self.efficiency != min(coff):
            print('Эффективность производства снижена из-за нехватки ресурсов')
            self.efficiency = min(coff)

        self.current_energy_profit=self.default_energy_profit*min(coff)
        out1 = {}
        out2 = {}
        for k, v in recipes[self.recipe_id]['output1'].items():
            out1[k] = v * self.efficiency * self.is_energy_connected * self.factory.team.is_energy_active
        for k, v in recipes[self.recipe_id]['output2'].items():
            out2[k] = v * self.efficiency * self.is_energy_connected * self.factory.team.is_energy_active
        if recipes[self.recipe_id]['output3']!={}:
            self.current_energy_profit=recipes[self.recipe_id]['output3']['Энергия']*self.efficiency
        self.out['output1'] = out1
        self.out['output2'] = out2
        self.factory.team.update_energy()
        for con in [self.connection_in1, self.connection_in2, self.connection_out2, self.connection_out1]:
            if con is not None:
                con.add_res()


        if self.connection_out1 is not None:
            self.connection_out1.output_build.update_res()
        if self.connection_out2 is not None:
            self.connection_out2.output_build.update_res()


    def fix_price(self):
        res={}
        if self.health==float('inf'):
            return res
        coff=1-self.health/self.max_health
        for k, v in self.price.items():
            res[k]=ceil(v*coff)
        return res

    def fix(self):
        self.health=self.max_health
        return {'success': True}

class Connection:
    def __init__(self):
        self.res = {}
        self.input_build = None
        self.output_build = None
        self.speed = 10

    def info(self):
        return f'{self.input_build.title} ---{self.res}---> {self.output_build.title}'

    def remove_connection(self):
        input_build=self.input_build
        output_build=self.output_build
        for i in [self.input_build, self.output_build]:
            if i is None:

                continue
            if i.connection_in1==self:
                i.connection_in1=None

            if i.connection_in2==self:
                i.connection_in2=None

            if i.connection_out1==self:
                i.connection_out1=None

            if i.connection_out2==self:
                i.connection_out2=None


        self.res = {}



        if input_build is not None:
            input_build.update_res()
        if output_build is not None:
            output_build.update_res()
        self.input_build = None
        self.output_build = None





    def add_res(self):
        if self.input_build.connection_out1 == self:
            res = self.input_build.out['output1']
        else:
            res = self.input_build.out['output2']

        cur_res={}
        for k, v in res.items():
            cur_res[k] = min(v, self.speed)
        self.res=cur_res

class Node(Build):
    def __init__(self, factory=None):
        Build.__init__(self, factory=factory)
        self.price = {}
        self.destroy_price = {'Железная пластина': 2}
        self.title = ''
        self.type='Node'
        self.description = 'Узел позволяет создавать разветвления и объединения соединений'
        self.connection_in1 = None
        self.connection_in2 = None
        self.connection_out1 = None
        self.connection_out2 = None
        self.max_connections_in = 2
        self.max_connections_out = 2
        self.max_health = 100
        self.health = self.max_health
        self.default_energy_profit = 0
        self.current_energy_profit = 0
        self.is_energy_connected = True
        self.factory = factory
        self.out = {'output1': {}, 'output2': {}}
        self.recipe_id=-1
        self.recipes=[-1]

    def update_res(self):
        input_res={}
        if self.connection_in1 is not None:
            input_res = self.connection_in1.res.copy()
        if self.connection_in2 is not None:
            for k, v in self.connection_in2.res.items():
                input_res[k] = input_res.get(k,0)+v

        out1={}
        out2={}

        if input_res:
            if len(input_res.keys())>1:
                print('На вход подаются разные типы ресурсов!')
                return False
            key, amount = list(input_res.keys())[0], list(input_res.values())[0]

            if self.connection_out1 is not None and self.connection_out2 is not None:
                out1 = {key: amount / 2}
                out2 = {key: amount / 2}
            elif self.connection_out1 is not None:
                out1 = {key: amount}
            elif self.connection_out2 is not None:
                out2 = {key: amount}

        self.out['output1'] = out1
        self.out['output2'] = out2
        for con in [self.connection_in1, self.connection_in2, self.connection_out2, self.connection_out1]:
            if con is not None:
                con.add_res()

        if self.connection_out1 is not None:
            self.connection_out1.output_build.update_res()
        if self.connection_out2 is not None:
            self.connection_out2.output_build.update_res()

    def set_recipe(self, recepie_id):
        self.update_res()

    def add_connection_in(self, connection, number: int=1):
        if number==1:
            if self.connection_in1!=None:
                print('Порт уже занят')
                return False
            else:
                self.connection_in1=connection
        elif number==2:
            if self.connection_in2!=None:
                print('Порт уже занят')
                return False
            else:
                self.connection_in2=connection
        else:
            print('Неверный аргумент (порты 1 или 2)')
            return False
        connection.output_build = self
        self.update_res()
        print('Соединение успешно создано')
        return True

    def add_connection_out(self, connection, number: int=1):
        if number == 1:
            if self.connection_out1 != None:
                print('Порт уже занят')
                return False
            else:
                self.connection_out1 = connection
        elif number == 2:
            if self.connection_out2 != None:
                print('Порт уже занят')
                return False
            else:
                self.connection_out2 = connection
        else:
            print('Неверный аргумент (порты 1 или 2)')
            return False
        connection.input_build = self
        print('Соединение успешно создано')
        connection.add_res()
        if connection.output_build != None:
            connection.output_build.update_res()
        return True








def compare_resources(price, current):
    f = True
    ost = {}
    for k, v in price.items():
        if current.get(k, 0) < v:
            f = False
            ost[k] = v - current.get(k, 0)
    if f == False:
        return {'success': False, 'ost': ost}
    else:
        return {'success': True}






