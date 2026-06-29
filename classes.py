from recipes import recipes

class World:
    def __init__(self, difficulty: int=5):
        self.teams=[]
        self.difficulty = difficulty


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
        pass


class Team:
    def __init__(self, title: str='team'):
        self.title = title
        self.resources = {}
        self.energy = 0
        self.factories = []
        self.is_energy_active = True
        self.produce = {}
        self.factories_names=[]

    def add_factory(self, factory):
        self.factories.append(factory)

    def remove_factory(self):
        for i in range(len(self.factories)):
            print(f'{i+1}. {self.factories[i].title}')
        n = int(input())
        if n<1 or n>len(self.factories):
            print('Неверно указанное значение, попробуйте снова')
            return False
        self.factories.pop(n-1)
        print('Фабрика успешно удалена!')

    def update(self):
        for _ in range(2):
            self.update_energy()
            for fac in self.factories:
                for b in fac.builds:
                    b.set_recipe(b.recipe_id)

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
        p=self.builds[n-1].destroy_price
        for k, v in p.items():
            if k not in self.team.resources.keys():
                self.team.resources[k]=v
            else:
                self.team.resources[k] += v
        b=self.builds.pop(n - 1)
        for c in (b.connection_in1, b.connection_in2, b.connection_out1, b.connection_out2):
            if c is not None:
                c.remove_connection()
        print('Постройка успешно демонтирована!')
        print('Ресурсов получено:')
        for k, v in p.items():
            print(f'Получено {v} ресурса {k}')
        self.team.update()
        return True




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
        print('Рецепт успешно сменён')

    def update_res(self):
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
                print(1)
                continue
            if i.connection_in1==self:
                i.connection_in1=None
                print(2)
            if i.connection_in2==self:
                i.connection_in2=None
                print(3)
            if i.connection_out1==self:
                i.connection_out1=None
                print(4)
            if i.connection_out2==self:
                i.connection_out2=None
                print(5)

        self.res = {}


        self.input_build=None
        self.output_build=None
        if input_build is not None:
            input_build.update_res()
        if output_build is not None:
            output_build.update_res()





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
        self.destroy_price = {}
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






# world=World()
# team1=Team()
#
# world.add_team(team1)
#
# factory=Factory(team=team1)
#
# build1=Build()
# build1.title='build1'
# build1.max_connections_out=1
# build1.default_energy_profit=-10
#
# build2=Build()
# build2.title='build2'
# build2.max_connections_in=1
# build2.max_connections_out=1
# build2.default_energy_profit=50
#
# build3=Build()
# build3.title='build3'
# build3.max_connections_in=1
# build3.max_connections_out=1
# build3.default_energy_profit=-10
#
# build4=Build()
# build4.title='build4'
# build4.max_connections_in=1
# build4.default_energy_profit=-30
#
# factory.build(build1)
# factory.build(build2)
# factory.build(build3)
# factory.build(build4)
#
#
# c1=Connection()
# c2=Connection()
# c3=Connection()
#
# build1.add_connection_out(c1)
# build2.add_connection_in(c1)
#
# build2.add_connection_out(c2)
# build3.add_connection_in(c2)
#
# build3.add_connection_out(c3)
# build4.add_connection_in(c3)
#
# build1.set_recipe(1)
# build2.set_recipe(2)
# build3.set_recipe(3)
# build4.set_recipe(4)
#
# print(c3.res)
# print(team1.energy)










