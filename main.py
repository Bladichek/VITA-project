from classes import *
from Builds import *
import json
world=World()
from matplotlib.pyplot import show
from networkx import DiGraph, draw

builds = [Build1, Drill_I, HUB, Smelter, Node, Storage]
cons=[]
team_names=[]


data={'difficulty': world.difficulty, 'teams': {}}

def load_data():
    global data
    try:
        with open('data.json', 'r') as f:
            data=json.load(f)
            f.close()
            for team_name, value in data['teams'].items():
                team_names.append(team_name)
                team = Team(title=team_name)
                team.energy=value['energy']
                team.resources=value['resources']
                team.is_energy_active=value['is_energy_active']
                team.produce=value['produce']
                team.factories_names=value['factories_names']

                for factories_name, value1 in value['factories'].items():
                    factory = Factory(title=factories_name, team=team)
                    factory.profit=value1['profit']
                    factory.builds=[]

                    for build_name, value3 in value1['builds'].items():
                        if value3['max_health']==-1:
                            h=float('inf')
                        else:
                            h=value3['max_health']
                        b=builds[value3['build_type']](factory)
                        b.price=value3['price']
                        b.destroy_price=value3['destroy_price']
                        b.title=build_name
                        b.type=value3['type']
                        b.description=value3['description']
                        b.max_connections_in=value3['max_connections_in']
                        b.max_connections_out=value3['max_connections_out']
                        b.max_health=h
                        b.health=value3['health']
                        b.default_energy_profit=value3['default_energy_profit']
                        b.current_energy_profit=value3['current_energy_profit']
                        b.is_energy_connected=value3['is_energy_connected']
                        b.efficiency=value3['efficiency']
                        b.out=value3['out']
                        b.recipes=value3['recipes']
                        b.recipe_id=value3['recipe_id']
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



                world.teams.append(team)

        print('Данные успешно загружены!')
    except Exception as e:
        with open('data.json', 'w') as f:
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
    }


def _connection_to_dict(c):
    in_title = c.input_build.title if c.input_build is not None else None
    out_title = c.output_build.title if c.output_build is not None else None

    # порт приёмника: connection_in2 -> 'B', иначе 'A'
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

    # Соединение относится к фабрике, если оба его конца — её постройки.
    # Перебираем порты построек и берём каждое соединение один раз (по id).
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
    """Сериализует команду со всеми фабриками."""
    factories_dict = {f.title: _factory_to_dict(f) for f in team.factories}
    return {
        'factories': factories_dict,
        'resources': team.resources,
        'energy': team.energy,
        'is_energy_active': team.is_energy_active,
        'produce': team.produce,
        'factories_names': team.factories_names,
    }


def update_data():
    """Универсальное сохранение: полностью перестраивает data из объекта world
    и записывает его в data.json. Вызывается без аргументов — обратно совместима
    со старой версией."""
    global data
    data = {
        'difficulty': world.difficulty,
        'teams': {team.title: _team_to_dict(team) for team in world.teams},
    }
    with open('data.json', 'w', encoding='utf-8') as f:
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

        update_data()

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
        update_data()

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


        for build in builds:
            b=build()
            print(f'{n}. {b.type}')
            n+=1

        k=int(input('Введите номер постройки: '))
        b=builds[k-1](current_factory)
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

        current_factory.build(build=b)
        if b.max_health==float('inf'):
            h=-1
        else:
            h=b.max_health
        # data['teams'][current_team.title]['factories'][current_factory.title]['builds'][b.title]={'build_type': k-1,
        #                                                                     'price': b.price,
        #                                                                     'destroy_price': b.destroy_price,
        #                                                                     'type': b.type,
        #                                                                     'description': b.description,
        #                                                                     'recipe_id': b.recipe_id,
        #                                                                     'max_connections_in': b.max_connections_in,
        #                                                                     'max_connections_out': b.max_connections_out,
        #                                                                     'max_health': h,
        #                                                                     'health': b.health,
        #                                                                     'default_energy_profit': b.default_energy_profit,
        #                                                                     'current_energy_profit': b.current_energy_profit,
        #                                                                     'is_energy_connected': b.is_energy_connected,
        #                                                                     'efficiency': b.efficiency,
        #                                                                     'out': b.out,
        #                                                                     'recipes': b.recipes,
        #                                                                     }
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
            print(f'\t' * tabs + f'default_energy_profit: {build.default_energy_profit}')
            print(f'\t' * tabs + f'current_energy_profit: {build.current_energy_profit}')
            print(f'\t' * tabs + f'is_energy_connected: {build.is_energy_connected}')
            print(f'\t' * tabs + f'efficiency: {build.efficiency}')
            print(f'\t' * tabs + f'out: {build.out}')
            print(f'\t' * tabs + f'recipes: {build.recipes}')
            print()
        tabs-=1
    for c in cons:
        print(c.info())

def set_recipe(current_factory: Factory):
    n = 1
    try:
        print('Выберите постройку из списка:')
        for b in current_factory.builds:

            print(f'{n}. {b.title} ({b.type})')
            n += 1

        k = int(input('Введите номер постройки: '))
        recipe_id=int(input('Введите номер рецепта: '))
        if current_factory.builds[k - 1].type == 'Node':
            raise Exception('У узла нет рецептов')
        current_factory.builds[k - 1].set_recipe(recipe_id)
        #data['teams'][current_factory.team.title]['factories'][current_factory.title]['builds'][current_factory.builds[k - 1].title]['recipe_id']=recipe_id
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
            build_out.add_connection_in(c)
        build_in.update_res()
        # data['teams'][current_factory.team.title]['factories'][current_factory.title]['connections'][f'{build_out.title}-{build_in.title}']={'res': c.res,
        #                                                                                                                'input_build': build_in.title,
        #                                                                                                                'output_build': build_out.title,
        #                                                                                                                'speed': c.speed,
        #                                                                                                                                      'port1': port1,
        #
        #                                                                                                                                      'port2': port2}
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


def set_team_name():
    pass

def set_factory_name():
    pass


def parse_commands(text):
    parts = text.split(maxsplit=1)
    command = parts[0]
    args = parts[1] if len(parts) > 1 else ''
    return (command, args)

def main():
    load_data()
    current_team=None
    current_factory=None

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


            elif command=='/set_factory':
                res=set_current_factory(current_team=current_team)
                if res['success']:
                    current_factory=res['result']


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





main()