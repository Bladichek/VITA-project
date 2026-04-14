from classes import *

world=World()
builds = [Build1]
def add_team(title):
    try:
        team=Team(title=title)
        world.add_team(team)
        print('Команда успешно добавлена!')
        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': e}

def add_factory(title, current_team):
    if current_team==None:
        print('Нет команд')
        return {'success': False, 'error': 'Нет команд!'}
    try:
        factory=Factory(title=title,  team=current_team)
        print('Фабрика успешно добавлена!')
        return {'success': True}
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

def set_current_factory(current_team):
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
        world.teams.pop(t-1)
        print('Команда успешно удалена!')
        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': e}



def remove_factory(current_team):
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
        current_team.factories.pop(f - 1)
        print('Фабрика успешно удалена!')
        return {'success': True}

    except Exception as e:
        return {'success': False, 'error': e}




def build(current_factory):
    n=1
    try:
        print('Выберите постройку из списка:')
        for build in builds:
            b=build()
            print(f'{n}. {b.title}')
            n+=1

        k=int(input('Введите номер постройки: '))
        b=builds[k-1](current_factory)
        current_factory.build(build=b)
    except Exception as e:
        return {'success': False, 'error': e}


def set_team_name():
    pass

def set_factory_name():
    pass


def parse_commands(text):
    command=text.split(maxsplit=1)[0]
    args=text.split(maxsplit=1)[-1]
    return (command, args)

def main():
    current_team=None
    current_factory=None

    while True:
        try:
            text = input('> ').strip()
            if text == '':
                continue
            command, args = parse_commands(text)


            if command=='/add_team':
                if args:
                    res=add_team(title=args)
                    if res['success']:
                        pass
                    else:
                        print(f'Произошла ошибка! {res["error"]}')
                else:
                    print('Нет аргументов!')


            elif command=='/add_factory':
                if args:
                    res=add_factory(title=args, current_team=current_team)
                    if res['success']:
                        pass
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
                res=build(current_factory=current_factory)
                if res['success']:
                    pass
                else:
                    print(f'Произошла ошибка! {res["error"]}')

        except:
            pass



main()