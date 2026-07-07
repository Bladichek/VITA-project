from classes import *
from Builds import *
import json
world=World()
from matplotlib.pyplot import show
from networkx import DiGraph, draw
import datetime


cons=[]
team_names=[]
current_team=None
current_factory=None
current_player=None

data={'difficulty': world.difficulty, 'teams': {}}

def load_data():
    global data, current_team, current_factory, current_player
    try:
        with open('datas/data.json', 'r') as f:
            data=json.load(f)
            f.close()
            world.difficulty=data['difficulty']
            world.day=data['day']
            for team_name, value in data['teams'].items():
                team_names.append(team_name)
                team = Team(title=team_name)
                team.energy=value['energy']
                team.resources=value['resources']
                team.is_energy_active=value['is_energy_active']
                team.produce=value['produce']
                team.factories_names=value['factories_names']
                team.drin=value['drin']
                team.drin_resources=value['drin_resources']
                team.players=value['players']
                team.grabbed_resources=value['grabbed_resources']
                team.level=value['level']
                cur_players={}
                for k, v in value['players'].items():
                    cur_players[int(k)]=v
                team.players=cur_players
                for factories_name, value1 in value['factories'].items():
                    factory = Factory(title=factories_name, team=team)
                    factory.profit=value1['profit']
                    factory.builds=[]

                    for build_name, value3 in value1['builds'].items():
                        if value3['max_health']==-1:
                            h=float('inf')
                        else:
                            h=value3['max_health']
                        if value3['health']==-1:
                            h1=float('inf')
                        else:
                            h1=value3['health']
                        b=builds[value3['build_type']](factory)
                        b.price=value3['price']
                        b.destroy_price=value3['destroy_price']
                        b.title=build_name
                        b.type=value3['type']
                        b.description=value3['description']
                        b.max_connections_in=value3['max_connections_in']
                        b.max_connections_out=value3['max_connections_out']
                        b.max_health=h
                        b.health=h1
                        b.default_energy_profit=value3['default_energy_profit']
                        b.current_energy_profit=value3['current_energy_profit']
                        b.is_energy_connected=value3['is_energy_connected']
                        b.efficiency=value3['efficiency']
                        b.out=value3['out']
                        b.recipes=value3['recipes']
                        b.recipe_id=value3['recipe_id']
                        b.level=value3['level']
                        b.defence=value3['defence']
                        if b.type=='Станция дроидов':
                            b.profit=value3['profit']
                            b.mode=value3['mode']
                        b.update_res()
                        factory.builds.append(b)
                    print(value1)
                    for connection_name, value2 in value1['connections'].items():
                        c=Connection()
                        c.res= value2['res']
                        c.speed=value2['speed']
                        if value2['port1'] == 'A':
                            port1=1
                        else:
                            port1=2
                        if value2['port2'] == 'A':
                            port2=1
                        else:
                            port2=2
                        input_build_name = value2['input_build']
                        output_build_name = value2['output_build']
                        cons.append(c)
                        #пройтись по постройкам, получить входные и выходные, подключить
                        for b in factory.builds:
                            if b.title==input_build_name:
                                b.add_connection_out(c, port2)
                            elif b.title==output_build_name:
                                b.add_connection_in(c, port1)
                    team.update()
                    cur_team = data.get('current_team')
                    cur_factory = data.get('current_factory')
                    if cur_factory and cur_team and factory.title==cur_factory and team.title==cur_team:
                        current_factory=factory
                if team.title==data['current_team']:
                    current_team=team




                world.teams.append(team)


        print('Данные успешно загружены!')
    except Exception as e:
        with open('datas/data.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.close()
        print('Файл с данными не обнаружен или повреждён', e)

def _health_for_save(value):
    if value == float('inf'):
        return -1
    return value


def _build_to_dict(b):
    try:
        build_type = builds.index(type(b))
    except ValueError:
        build_type = 0
    if b.type=='Станция дроидов':
        return {
            'build_type': build_type,
            'price': b.price,
            'destroy_price': b.destroy_price,
            'type': b.type,
            'description': b.description,
            'recipe_id': b.recipe_id,
            'max_connections_in': b.max_connections_in,
            'max_connections_out': b.max_connections_out,
            'max_health': _health_for_save(b.max_health),
            'health': _health_for_save(b.health),
            'default_energy_profit': b.default_energy_profit,
            'current_energy_profit': b.current_energy_profit,
            'is_energy_connected': b.is_energy_connected,
            'efficiency': b.efficiency,
            'out': b.out,
            'recipes': b.recipes,
            'mode': b.mode,
            'profit': b.profit,
            'level': b.level,
            'defence': b.defence,
        }
    return {
        'build_type': build_type,
        'price': b.price,
        'destroy_price': b.destroy_price,
        'type': b.type,
        'description': b.description,
        'recipe_id': b.recipe_id,
        'max_connections_in': b.max_connections_in,
        'max_connections_out': b.max_connections_out,
        'max_health': _health_for_save(b.max_health),
        'health': _health_for_save(b.health),
        'default_energy_profit': b.default_energy_profit,
        'current_energy_profit': b.current_energy_profit,
        'is_energy_connected': b.is_energy_connected,
        'efficiency': b.efficiency,
        'out': b.out,
        'recipes': b.recipes,
        'level': b.level,
        'defence': b.defence,
    }


def _connection_to_dict(c):
    in_title = c.input_build.title if c.input_build is not None else None
    out_title = c.output_build.title if c.output_build is not None else None

    if c.output_build.connection_in2 is c:
        port1 = 'B'
    elif c.output_build.connection_in1 is c:
        port1 = 'A'

    if c.input_build.connection_out2 is c:
        port2 = 'B'
    elif c.input_build.connection_out1 is c:
        port2 = 'A'
    return {
        'res': c.res,
        'input_build': in_title,
        'output_build': out_title,
        'speed': c.speed,
        'port1': port1,
        'port2': port2
    }



def _factory_to_dict(factory):
    builds_dict = {b.title: _build_to_dict(b) for b in factory.builds}


    seen = set()
    connections_dict = {}
    for b in factory.builds:
        for con in (b.connection_in1, b.connection_in2,
                    b.connection_out1, b.connection_out2):
            if con is None or id(con) in seen:
                continue
            if not (con.input_build in factory.builds
                    and con.output_build in factory.builds):
                continue
            seen.add(id(con))
            in_title = con.input_build.title if con.input_build else 'None'
            out_title = con.output_build.title if con.output_build else 'None'
            key = f'{out_title}-{in_title}'
            connections_dict[key] = _connection_to_dict(con)

    return {
        'builds': builds_dict,
        'connections': connections_dict,
        'profit': factory.profit,
    }


def _team_to_dict(team):
    factories_dict = {f.title: _factory_to_dict(f) for f in team.factories}
    return {
        'factories': factories_dict,
        'resources': team.resources,
        'energy': team.energy,
        'is_energy_active': team.is_energy_active,
        'produce': team.produce,
        'factories_names': team.factories_names,
        'droids_profit': team.droids_profit,
        'players': team.players,
        'drin': team.drin,
        'drin_resources': team.drin_resources,
        'grabbed_resources': team.grabbed_resources,
        'level': team.level,
    }


def update_data(current_team='', current_factory=''):
    global data
    if current_team == '':
        current_team = data['current_team']
    if current_factory == '':
        current_factory = data['current_factory']
    data = {
        'difficulty': world.difficulty,
        'teams': {team.title: _team_to_dict(team) for team in world.teams},
        'current_team': current_team,
        'current_factory': current_factory,
        'day': world.day,
    }
    with open(f'datas/data{datetime.datetime.now()}.json.back', 'w') as f:
        json.dump(data, f, indent=4)
    f.close()
    with open('datas/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_team(title):
    try:
        if title in ['difficulty', 'teams', '/add_team']:
            raise Exception('Недопустимое название!')
        elif title in team_names:
            raise Exception('Команда с таким названием уже есть!')
        team_names.append(title)
        team=Team(title=title)
        world.add_team(team)
        print('Команда успешно добавлена!')
        update_data(current_team=team.title, current_factory='no')

        return {'success': True, 'result': team}
    except Exception as e:
        return {'success': False, 'error': e}

def add_factory(title, current_team: Team):
    if current_team==None:
        print('Нет команд')
        return {'success': False, 'error': 'Нет команд!'}
    try:
        if title in ['resources', 'energy', 'factories', 'is_energy_active', 'produce', '/add_factory']:
            raise Exception('Недопустимое название фабрики!')
        if title in current_team.factories_names:
            raise Exception('Фабрика с таким названием уже есть!')
        factory=Factory(title=title,  team=current_team)
        print('Фабрика успешно добавлена!')
        #data['teams'][current_team.title]['factories'][title]={'builds': {}, 'connections': {}, 'profit': factory.profit}
        current_team.factories_names.append(title)
        update_data(current_factory=factory.title)

        return {'success': True, 'result': factory}
    except Exception as e:
        return {'success': False, 'error': e}

def set_current_team():
    teams=[]
    n=1
    print('Выберите команду:')
    for team in world.teams:
        teams.append(team)
        print(f'{n}. {team.title}')
        n+=1
    try:
        t = int(input('Введите номер команды: '))
        tm=teams[t-1]
        update_data(current_team=tm.title)
        print('Команда успешно выбрана!')
        return {'success': True, 'result': tm}
    except Exception as e:
        print('Введён неверный номер')
        return {'success': False, 'error': e}

def set_current_factory(current_team: Team):
    if current_team==None:
        print('Нет команд')
        return {'success': False, 'error': 'Нет команд!'}
    factories=[]
    n=1
    print('Выберите фабрику:')
    for factory in current_team.factories:
        factories.append(factory)
        print(f'{n}. {factory.title}')
        n+=1
    try:
        f=int(input('Введите номер фабрики: '))
        fc=factories[f-1]
        print('Фабрика успешно выбрана')
        update_data(current_factory=fc.title)
        return {'success': True, 'result': fc}
    except Exception as e:
        print('Введён неверный номер')
        return {'success': False, 'error': e}


def remove_team():
    print('Выберите команду для удаления из списка:')
    n=1
    for team in world.teams:
        print(f'{n}. {team.title}')
        n+=1
    try:
        t=int(input('Введите номер команды: '))
        if world.teams[t-1].factories != []:
            raise Exception('Нельзя удалить команду, пока у неё имеются фабрики!')
        team_names.remove(world.teams[t-1].title)
        world.teams.pop(t-1)
        print('Команда успешно удалена!')
        update_data()

        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': e}



def remove_factory(current_team: Team):
    print('Выберите фабрику для удаления из списка:')
    n=1
    for factory in current_team.factories:
        print(f'{n}. {factory.title}')
        n+=1
    try:
        f=int(input())
        if current_team.factories[f-1].builds != []:
            ans=input('У фабрики есть постройки, которые будут безвозвратно удалены. Вы уверены? (Y/n): ')
            if ans.lower()=='n':
                return {'success': True}
            elif ans.lower()=='y':
                pass
            else:
                print('Неверно введён ответ!')
                return {'success': True}
        current_team.factories_names.remove(current_team.factories[f-1].title)
        current_team.factories.pop(f - 1)
        print('Фабрика успешно удалена!')
        update_data()
        return {'success': True}

    except Exception as e:
        return {'success': False, 'error': e}




def build(current_factory: Factory, current_team: Team):
    n=1
    try:
        print('Выберите постройку из списка:')
        build_names=[]

        for b in current_factory.builds:

            build_names.append(b.title)

        bs=[]
        for build in builds:
            b=build()
            if b.level<=current_factory.team.level:
                print(f'{n}. {b.type}')
                n+=1
                bs.append(build)

        k=int(input('Введите номер постройки: '))
        b=bs[k-1](current_factory)
        title=input('Введите название постройки (необязательно): ')
        if title=='':
            title=b.type

        if title not in build_names:
            b.title=title
        else:
            counter = 1
            while True:
                new_title = f"{title} ({counter})"
                if new_title not in build_names:
                    b.title=new_title
                    break
                counter += 1

        r=current_factory.build(build=b)
        if not r:
            raise Exception('Произошла ошибка')
        if len(b.recipes)>1:
            n=input('Начальный рецепт (необязательно): ')
            if n.isdigit():
                b.set_recipe(int(n))
        update_data()
        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': e}

def info(current_team: Team):
    tabs=0
    print('Currrent team')
    print(f'title: {current_team.title}')
    print(f'resources: {current_team.resources}')
    print(f'energy: {current_team.energy}')
    print(f'is_energy_active: {current_team.is_energy_active}')
    print(f'produce: {current_team.produce}')
    print(f'factories_names: {current_team.factories_names}')
    print(f'droids_profit: {current_team.droids_profit}')
    print(f'drin: {current_team.drin}')
    print(f'drin_resources: {current_team.drin_resources}')
    print(f'grabbed_resources: {current_team.grabbed_resources}')
    print(f'players: {current_team.players}')
    print()



    tabs+=1
    print('Factories')
    for fac in current_team.factories:
        print(f'\t'*tabs+f'title: {fac.title}')
        print(f'\t' * tabs + f'profit: {fac.profit}')
        print(f'\t' * tabs + f'Builds:')
        tabs+=1
        for build in fac.builds:
            print(f'\t' * tabs + f'title: {build.title}')
            print(f'\t' * tabs + f'description: {build.description}')
            print(f'\t' * tabs + f'price: {build.price}')
            print(f'\t' * tabs + f'destroy_price: {build.destroy_price}')
            print(f'\t' * tabs + f'recipe_id: {build.recipe_id}')
            print(f'\t' * tabs + f'connection_in1: {build.connection_in1}')
            print(f'\t' * tabs + f'connection_in2: {build.connection_in2}')
            print(f'\t' * tabs + f'connection_out1: {build.connection_out1}')
            print(f'\t' * tabs + f'connection_out2: {build.connection_out2}')
            print(f'\t' * tabs + f'max_connections_in: {build.max_connections_in}')
            print(f'\t' * tabs + f'max_connections_out: {build.max_connections_out}')
            print(f'\t' * tabs + f'max_health: {build.max_health}')
            print(f'\t' * tabs + f'health: {build.health}')
            print(f'\t' * tabs + f'default_energy_profit: {build.default_energy_profit}')
            print(f'\t' * tabs + f'current_energy_profit: {build.current_energy_profit}')
            print(f'\t' * tabs + f'is_energy_connected: {build.is_energy_connected}')
            print(f'\t' * tabs + f'efficiency: {build.efficiency}')
            print(f'\t' * tabs + f'out: {build.out}')
            print(f'\t' * tabs + f'recipes: {build.recipes}')
            print(f'\t' * tabs + f'level: {build.level}')
            if build.type=='Станция дроидов':
                print(f'\t' * tabs + f'profit: {build.profit}')
                print(f'\t' * tabs + f'mode: {build.mode}')
            print()
        tabs-=1
    for c in cons:
        if c.input_build.factory.title==current_factory.title and c.input_build.factory.team.title==current_team.title:
            print(c.info())

def set_recipe(current_factory: Factory):
    n = 1
    try:
        print('Выберите постройку из списка:')
        for b in current_factory.builds:

            print(f'{n}. {b.title} ({b.type}), текущий рецепт: {b.recipe_id}')
            n += 1

        k = int(input('Введите номер постройки: '))
        b=current_factory.builds[k-1]

        if len(b.recipes) == 1:
            raise Exception('У постройки нет рецептов')

        print('Доступные рецепты:')
        for i in b.recipes:
            if i == -1: continue
            if i not in recipes_level[current_factory.team.level]:
                continue
            recipe=recipes[i]
            in_a=''
            in_b=''
            out_a=''
            out_b=''
            if recipe['input1'] != {}:
                in_a=f'Вход А: {list(recipe["input1"].keys())[0]} - {list(recipe["input1"].values())[0]} '
            if recipe['input2'] != {}:
                in_b=f'Вход B: {list(recipe["input2"].keys())[0]} - {list(recipe["input2"].values())[0]} '
            if recipe['output1'] != {}:
                out_a=f'Выход А: {list(recipe["output1"].keys())[0]} - {list(recipe["output1"].values())[0]} '
            if recipe['output2'] != {}:
                out_b=f'Выход B: {list(recipe["output2"].keys())[0]} - {list(recipe["output2"].values())[0]}'
            print(f'{i}. {in_a}{in_b}--> {out_a}{out_b}')
        recipe_id = int(input('Введите номер рецепта: '))
        b.set_recipe(recipe_id)
        update_data()

        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': e}

def add_connection(current_factory):
        global cons
        c=Connection()
        n=1
    # try:
        print('Выберите постройку из списка, выход которой будет подключён:')
        for b in current_factory.builds:

            print(f'{n}. {b.title} ({b.type})')
            n += 1

        k = int(input('Введите номер постройки: '))
        build_in=current_factory.builds[k - 1]
        r=None
        port1='A'
        if build_in.max_connections_out==0:
            raise Exception('У этой постройки нет портов для подключений')
        elif build_in.max_connections_out==2:
            port = input('Подключать в порт A или B?: ').upper()
            if port=='A':
                r=build_in.add_connection_out(c, 1)
            elif port=='B':
                r=build_in.add_connection_out(c, 2)
            else:
                raise Exception('Введён неверный порт')
            port1=port
        else:
            build_in.add_connection_out(c)
        if r is not None:
            if r==False:
                c.remove_connection()
        n=1
        print('Выберите постройку из списка, вход которой будет подключён:')
        for b in current_factory.builds:
            print(f'{n}. {b.title} ({b.type})')
            n += 1

        k = int(input('Введите номер постройки: '))
        build_out = current_factory.builds[k - 1]
        if build_in==build_out:
            raise Exception('Нельзя подключать постройку саму к себе!')
        port='A'
        port2=port
        r=None
        if build_out.max_connections_in == 0:
            raise Exception('У этой постройки нет портов для подключений')
        elif build_out.max_connections_in == 2:
            port = input('Подключать в порт A или B?: ').upper()
            if port == 'A':
                r=build_out.add_connection_in(c, 1)
            elif port == 'B':
                r=build_out.add_connection_in(c, 2)
            else:
                raise Exception('Введён неверный порт')
            port2=port
        if r is not None:
            if r==False:
                c.remove_connection()
        else:
            r=build_out.add_connection_in(c)

        build_in.update_res()
        if r:
            cons.append(c)
            update_data()
            return {'success': True}
        else:
            return {'success': False, 'error': 'Порт уже занят'}
    # except Exception as e:
    #     return {'success': False, 'error': e}




def show_graph(current_factory):
    nodes=[]
    edges=[]

    for b in current_factory.builds:
        nodes.append(b.title)
        if b.connection_out1!=None:
            edges.append([b.title, b.connection_out1.output_build.title])
        if b.connection_out2 != None:
            edges.append([b.title, b.connection_out2.output_build.title])

    graph=DiGraph(directrd=True)
    for node in nodes:
        graph.add_node(node)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    draw(graph, with_labels=True)
    show()


def remove_connection(current_factory):
    n = 1
    try:
        print('Выберите постройку, соединение которой необходимо удалить:')
        for b in current_factory.builds:
            print(f'{n}. {b.title} ({b.type})')
            n += 1

        k = int(input('Введите номер постройки: '))
        c=current_factory.builds[k - 1].remove_connection()
        cons.remove(c)
        update_data()

        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': e}

def destroy(current_factory):
    r=current_factory.destroy()
    if r:
        update_data()
        return {'success': True}
    else:
        return {'success': False}


def set_team_name(current_team, args):
    if args!='':
        if args in team_names:
            return {'success': False, 'error': 'Команда с таким названием уже есть!'}
        current_team.title=args
        update_data()
        return {'success': True}
    else:
        return {'success': False, 'error': 'Нет аргументов'}

def set_factory_name(current_factory, args):
    if args!='':
        if args in current_factory.team.factories_names:
            return {'success': False, 'error': 'Фабрика с таким названием уже есть!'}
        current_factory.title=args
        update_data()
        return {'success': True}
    else:
        return {'success': False, 'error': 'Нет аргументов'}

def add_res(current_team, args):

    if args!='':
        s=args.rfind(' ')
        resource=args[:s]
        amount=args[s+1:]
        if not amount.isdigit():
            return {'success': False, 'error': 'Неверный аргумент'}
        r=current_team.add_res(resource, int(amount))
        update_data()

        if r['success']:
            return {'success': True}
        else:
            return {'success': False, 'error': r['error']}
    else:
        resource=input('Какой тип ресурсов необходимо прибавить?: ')
        amount=input('На сколько?: ')
        if not amount.isdigit():
            return {'success': False, 'error': 'Неверный аргумент'}
        r = current_team.add_res(resource, int(amount))
        update_data()
        if r['success']:
            return {'success': True}
        else:
            return {'success': False, 'error': r['error']}


def set_res(current_team, args):
    if args != '':
        s = args.rfind(' ')
        resource = args[:s]
        amount = args[s + 1:]
        if not amount.isdigit():
            return {'success': False, 'error': 'Неверный аргумент'}
        r = current_team.set_res(resource, int(amount))

        if r['success']:
            return {'success': True}
        else:
            return {'success': False, 'error': r['error']}
    else:
        resource = input('Какой тип ресурсов необходимо установить?: ')
        amount = input('Сколько?: ')
        if not amount.isdigit():
            return {'success': False, 'error': 'Неверный аргумент'}
        r = current_team.set_res(resource, int(amount))

        if r['success']:
            return {'success': True}
        else:
            return {'success': False, 'error': r['error']}



def set_mode(current_factory):
    b=current_factory.builds
    droids=[]
    s=1
    for i in b:
        if i.type=='Станция дроидов':
            print(f'{s}. {i.title} ({i.type})')
            droids.append(i)
            s+=1
    n= int(input('Введите номер постройки: '))
    build = droids[n-1]
    build.profit={}
    print('1. accept')
    print('2. donor')
    n=int(input('Выберите режим: '))
    if n==1:
        build.mode='accept'
    if n==2:
        build.mode='donor'
    current_factory.team.update()
    update_data()
    return {'success': True}

def set_profit(current_factory):
    b = current_factory.builds
    droids = []
    s = 1
    for i in b:
        if i.type == 'Станция дроидов':
            print(f'{s}. {i.title} ({i.type})')
            droids.append(i)
            s += 1
    n = int(input('Введите номер постройки: '))
    build = droids[n - 1]
    res = build.set_profit()
    update_data()
    if res['success']:
        return {'success': True}
    else:
        return {'success': False, 'error': res['error']}


def add_player(current_team):
    id=len(list(current_team.players))
    inventory=[]
    nickname=input('Введите имя: ')
    card_id=0
    print('Приложите карту:')
    player={
        'id': id,
        'nickname': nickname,
        'inventory': inventory,
        'card_id': card_id,
        'advanced_recipes': [],
        'balance': 0,

    }
    current_team.players[id] = player
    update_data()
    return {'success': True}

def inventory(current_team, player):
    print('Какое действие хотите сделать с инвентарём?')
    print('1. Взять')
    print('2. Положить')
    print('3. Удалить')
    print('4. Посмотреть')
    n = input('Выберите действие: ')
    if n in ['1', '2', '3', '4']:
        if n == '1':
            return _grab(current_team, player['id'])
        elif n == '2':
            return _add_inv(current_team, player['id'])
        elif n == '3':
            return _del_inv(current_team, player['id'])
        else:
            return _show_inventory(current_team, player['id'])
    else:
        return {'success': False, 'error': 'Неверный ввод'}

def _grab(current_team, player_id):
    player=current_team.players[player_id]
    print(f'Инвентарь {player["nickname"]}:')
    s=1
    for item in player['inventory']:
        print(f'{s}. {item}')
        s+=1
    objects=[]
    numbers=[]
    print('Введите номера предметов, которые нужно взять')
    print('(Введите не больше 3 номеров, завершите последовательность цифрой 0)')
    n=int(input('Номер: '))
    while n!=0:
        numbers.append(n)
        if n<0 or n > len(player['inventory']):
            print('Нет такого предмета')
        else:
            objects.append(player['inventory'][n-1])
            if len(objects)==3:
                break
        while n in numbers:
            n = int(input('Номер: '))
            if n in numbers:
                print('Нельзя брать один и тот же предмет!')
    if len(objects)==0:
        return {'success': True}
    print('Вот предметы, которые вы хотите взять. Всё верно? (Y/n)')
    print(*objects)
    ans=input()
    if ans.lower()=='y':
        for i in objects:
            current_team.players[player_id]['inventory'].remove(i)
            if player_id in current_team.grabbed_resources.keys():
                current_team.grabbed_resources[player_id].append(i)
            else:
                current_team.grabbed_resources[player_id] = [i]
        update_data()
        return {'success': True}
    else:
        return _grab(current_team, player_id)

def _add_inv(current_team, player_id):
    obj=input('Предмет, который вы хотите положить в инвентарь: ')
    if obj=='':
        return {'success': False, 'error': 'Пустой объект'}
    current_team.players[player_id]['inventory'].append(obj)
    update_data()
    return {'success': True}


def _del_inv(current_team, player_id):
    player=current_team.players[player_id]
    print(f'Инвентарь {player["nickname"]}:')
    s = 1
    for item in player['inventory']:
        print(f'{s}. {item}')
        s+=1

    print('Введите номер предмета, который нужно удалить')
    n = int(input('Номер: '))
    current_team.players[player_id]['inventory'].pop(n-1)
    update_data()
    return {'success': True}

def _show_inventory(current_team, player_id):
    player=current_team.players[player_id]
    print(f'Инвентарь {player["nickname"]}:')
    s = 1
    for item in player['inventory']:
        print(f'{s}. {item}')
        s += 1
    return {'success': True}


def return_inv(current_team):
    if current_team.grabbed_resources=={}:
        print('Нечего возвращать')
        return {'success': True}

    ans=input('Все колонисты вернули свой инвентарь? (Y/n) ')
    if ans.lower()=='y':
        for k, v in current_team.grabbed_resources.items():
            for i in v:
                current_team.players[k]['inventory'].append(i)


    else:
        for k, v in current_team.grabbed_resources.items():
            ans=input(f'Вернул ли {current_team.players[k]["nickname"]} все свои вещи? (Y/n) ')
            if ans.lower()=='y':
                for i in v:
                    current_team.players[k]['inventory'].append(i)
            else:
                for i in v:
                    ans = input(f'Вернул ли {current_team.players[k]["nickname"]} {i}? (Y/n) ')
                    if ans.lower()=='y':
                        current_team.players[k]['inventory'].append(i)

    current_team.grabbed_resources = {}
    update_data()
    return {'success': True}


def set_drin(current_team):
    drin = int(input(f'Введите значение ДРИН в % от 1 до 100 (текущее значение: {current_team.drin}) '))
    if drin>100 or drin<1:
        return {'success': False, 'error': 'Неверный ввод'}
    current_team.drin = drin
    res=current_team.update_drin_res()
    if res['success']:
        update_data()
        return {'success': True}


def craft(current_team, player):
    return current_team.craft(player['id'])



def set_player(current_team):
    print('Какой способ выбора колониста?')
    print('1. По номеру')
    print('2. По карте')
    mode = input('Выберите способ: ')
    if mode == '1':
        players = []
        print('Игроки:')
        for k, v in current_team.players.items():
            print(f'{k + 1}. {v["nickname"]}')
            players.append(v)
        n = input('Выберите колониста: ')
        if n.isdigit() and int(n) > 0 and int(n) <= len(players):
            return {'success': True, 'result':players[int(n) - 1]}
        else:
            return {'success': False, 'error': 'Неверный ввод'}


def add_balance(current_team, player):
    n=int(input('На сколько?: '))
    player['balance']+=n
    update_data()
    return {'success': True}

def buy(current_team, player):
    res = current_team.buy(player)
    if res['success']:
        update_data()
    return res

def update_day():
    res=world.update_day()
    damaged=[]
    destroyed=[]
    if res['success']:
        print(res['result'])
        for team, v1 in res['result'].items():
            for fac, v2 in v1.items():
                for dam in v2['damaged_builds']:
                    damaged.append({'name': dam[0].title,'health': dam[0].health, 'max_health': dam[0].max_health, 'type': dam[0].type, 'factory': fac, 'team': team, 'damage': dam[1]})
                for des in v2['destroyed_builds']:
                    destroyed.append({'name': des[0].title, 'health': des[0].health, 'max_health': des[0].max_health,  'type': des[0].type, 'factory': fac, 'team': team, 'damage': des[1]})

    print('Повреждённые постройки:')
    s=1
    for i in damaged:
        if i is None:
            continue
        print(f'{s}. {i["name"]} ({i["type"]}) - {i["health"]}/{i["max_health"]} (-{i["damage"]}) Команда: {i["team"]} Фабрика: ({i["factory"]})')
        s+=1
    print()
    print('Разрушенные постройки:')
    s = 1
    for i in destroyed:
        if i is None:
            continue
        print(f'{s}. {i["name"]} ({i["type"]}) - {i["health"]}/{i["max_health"]} (-{i["damage"]}) Команда: {i["team"]} Фабрика: ({i["factory"]})')
        s += 1
    update_data()
    return {'success': True}

def fix(current_team):
    print('Починить всё?')
    print('Общая стоимость:')
    s=1
    for k, v in current_team.fix_price().items():
        print(f'{s}. {k}: {v}')
        s+=1
    ans=input('Починить? (Y/n): ')
    if ans.lower() == 'n':
        for fac in current_team.factories:
            if fac.fix_price()=={}:
                continue

            print(f'Починить всё на фабрике {fac.title}?')
            print('Общая стомость:')
            s=1
            for k, v in fac.fix_price().items():
                print(f'{s}. {k}: {v}')
                s += 1
            ans = input('Починить? (Y/n): ')
            if ans.lower() == 'n':
                ans = input('Починить что-либо на этой фабрике? (Y/n): ')
                if ans.lower() == 'n':
                    continue
                else:
                    s=1
                    builds=[]
                    for b in fac.builds:
                        if b.health==b.max_health:
                            continue
                        print(f'{s}. {b.title} ({b.health}/{b.max_health}) - {b.fix_price()}')
                        s+=1
                        builds.append(b)
                    print('Вводите номера для починки (0 для выхода)')
                    n=int(input('Номер: '))
                    while n!=0:
                        res=fac.fix_build(builds[n-1])
                        if res['success']:
                            print('Успешно!')
                        else:
                            print(res['result'])
                        n = int(input('Номер: '))

            else:
                res=current_team.fix_factory(fac)
                if res['success']:
                    print('Успешно!')
                else:
                    print(res['result'])
                update_data()
                return {'success': True}
        update_data()
        return {'success': True}

    else:
        res=current_team.fix_all()
        if res['success']:
            update_data()
            return {'success': True}
        else:
            update_data()
            return {'success': False, 'error': res['result']}

def res(current_team):
    print('Ресурсы команды:')
    for k, v in current_team.res().items():
        if v!=0:
            print(f'{k}: {v}')
    return {'success': True}

def set_difficulty():

    n=input(f'Введите сложность (текущая: {world.difficulty}): ')
    if n.isdigit() and int(n)>0:
        world.difficulty=int(n)
        update_data()
        return {'success': True}
    else:
        return {'success': False, 'error': 'Неверный ввод'}


def show_health(current_factory):
    for b in current_factory.builds:
        print(f'{b.title} ({b.health}/{b.max_health})')
    return {'success': True}


def set_build(current_factory):
    builds=[]
    s=1
    for b in current_factory.builds:
        print(f'{s}. {b.title} ({b.type})')
        builds.append(b)
        s+=1
    n=input('Выберите здание: ')
    print([x.title for x in builds])
    if n.isdigit() and int(n)>0 and int(n)<=len(current_factory.builds):
        build=builds[int(n)-1]
        print()
        print(f'{build.title} ({build.type}) ({build.health}/{build.max_health})')
        print(f'Текущий рецепт: {build.recipe_id}')
        print(f'Подключено к сети: {build.is_energy_connected}')
        print()
        print('1. Отключить/подключить к сети')
        print('2. Починить')
        print('3. Установить рецепт')
        print('4. Сменить название')
        print('5. Разрушить')
        print('6. Выход')
        print()
        n=input('Выберите действие: ')
        if n.isdigit() and int(n)>0 and int(n)<=6:
            if n == '1':
                res = _switch_energy(build)


            elif n == '2':
                f = current_factory.fix_build(build)
                if f['success']:
                    res=f
                else:
                    res={"success": False, 'error': f['result']}

            elif n == '3':
                r=input('Введите номер рецепта: ')
                if r.isdigit():
                    build.set_recipe(int(r))
                    res = {'success': True}
                else:
                    res = {'success': False, 'error': 'Неверный ввод'}


            elif n == '4':
                res = _set_build_name(build)

            elif n == '5':
                res = current_factory.destroy_build(build, res=True)

            else:
                res = {'success': True}

            current_factory.team.update()
            update_data()
            return res

        else:
            return {'success': False, 'error': 'Неверный ввод'}
    else:
        return {'success': False, 'error': 'Неверный ввод'}

def _switch_energy(build):
    if build.is_energy_connected==True:
        build.is_energy_connected=False
        print('Постройка отключена')
    else:
        build.is_energy_connected=True
        print('Постройка подключена')
    return {'success': True}


def _set_build_name(b):
    title = input('Введите название постройки: ')
    if title == '':
        return {'success': False, 'error': 'Пустое название!'}
    build_names=[]
    for build in b.factory.builds:
        build_names.append(build.title)

    if title not in build_names:
        b.title = title
    else:
        counter = 1
        while True:
            new_title = f"{title} ({counter})"
            if new_title not in build_names:
                b.title = new_title
                break
            counter += 1
    return {'success': True}


def parse_commands(text):
    parts = text.split(maxsplit=1)
    command = parts[0]
    args = parts[1] if len(parts) > 1 else ''
    return (command, args)

def main():
    load_data()

    global current_factory, current_team, current_player

    while True:

            text = input('> ').strip()
            if text == '':
                continue
            command, args = parse_commands(text)


            if command=='/add_team':
                if args:
                    res=add_team(title=args)
                    if res['success']:
                        current_team=res['result']
                    else:
                        print(f'Произошла ошибка! {res["error"]}')
                else:
                    print('Нет аргументов!')


            elif command=='/add_factory':
                if args:
                    res=add_factory(title=args, current_team=current_team)
                    if res['success']:
                        current_factory=res['result']
                    else:
                        print(f'Произошла ошибка! {res["error"]}')
                else:
                    print('Нет аргументов!')

            elif command=='/set_team':
                res=set_current_team()
                if res['success']:
                    current_team=res['result']
                    update_data(current_team=current_team.title)


            elif command=='/set_factory':
                res=set_current_factory(current_team=current_team)
                if res['success']:
                    current_factory=res['result']
                    update_data(current_factory=current_factory.title)


            elif command=='/exit':
                break

            elif command=='/remove_team':
                res=remove_team()
                if res['success']:
                    pass
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/test':
                print(world.teams[0].factories)


            elif command=='/remove_factory':
                res=remove_factory(current_team=current_team)
                if res['success']:
                    pass
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/build':
                res=build(current_factory=current_factory, current_team=current_team)
                if res['success']:
                    pass
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/info':
                info(current_team)

            elif command=='/set_recipe': #перенести принты об успешной смене сюда (придётся ещё переносить об неуспешной смене)
                res=set_recipe(current_factory)
                if res['success']:
                    print('Рецепт успешно сменён!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/add_connection':
                res=add_connection(current_factory)
                if res['success']:
                    print('Соединение успешно создано!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/show':
                show_graph(current_factory)

            elif command=='/remove_connection':
                res=remove_connection(current_factory)
                if res['success']:
                    print('Соединение успешно удалено')
                else:
                    print(f'Произошла ошибка! {res["error"]}')
            elif command=='/destroy':
                res=destroy(current_factory)
                if res['success']:
                    pass
                else:
                    print('Произошла ошибка')
            elif command=='/update':
                current_team.update()

            elif command=='/add_res':
                res=add_res(current_team, args)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/set_res':
                res=set_res(current_team, args)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command == '/set_mode':
                res = set_mode(current_factory)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command == '/set_profit':
                res = set_profit(current_factory)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/add_player':
                res=add_player(current_team)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/inv':
                res=inventory(current_team, current_player)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/return_inv':
                res=return_inv(current_team)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')


            elif command=='/set_drin':
                res=set_drin(current_team)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/craft':
                res=craft(current_team, current_player)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/set_team_name':
                res=set_team_name(current_team, args)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/set_factory_name':
                res=set_factory_name(current_factory, args)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/add_balance':
                res=add_balance(current_team, current_player)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/buy':
                res=buy(current_team, current_player)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')

            elif command=='/set_player':
                res=set_player(current_team)
                if res['success']:
                    current_player=res['result']
                    print('Успешно!')

            elif command=='/update_day':
                res=update_day()
                if res['success']:
                    print('Успешно!')


            elif command=='/fix':
                res=fix(current_team)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')


            elif command=='/set_build':
                res=set_build(current_factory)
                if res['success']:
                    print('Успешно!')
                else:
                    print(f'Произошла ошибка! {res["error"]}')







main()