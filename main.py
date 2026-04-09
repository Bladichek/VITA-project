from classes import *

world=World()

def add_team(title):
    try:
        team=Team(title=title)
        world.add_team(team)
        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': e}

def add_factory(title, current_team):
    if current_team==None:
        print('Нет команд')
        return {'success': False}
    try:
        factory=Factory(title=title,  team=current_team)
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
        return {'success': True, 'result': teams[t-1]}
    except Exception as e:
        print('Введён неверный номер')
        return {'success': False, 'error': e}

def set_current_factory(current_team):
    if current_team==None:
        print('Нет команд')
        return {'success': False}
    factories=[]
    n=1
    print('Выберите фабрику:')
    for factory in current_team.factories:
        factories.append(factory)
        print(f'{n}. {factory.title}')
        n+=1
    try:
        f=int(input('Введите номер фабрики: '))
        return {'success': True, 'result': factories[f-1]}
    except Exception as e:
        print('Введён неверный номер')
        return {'success': False, 'error': e}





def build():
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
                        print('Команда успешно добавлена!')
                    else:
                        print(f'Произошла ошибка! {res["error"]}')
                else:
                    print('Нет аргументов!')


            elif command=='/add_factory':
                if args:
                    res=add_factory(title=args, current_team=current_team)
                    if res['success']:
                        print('Фабрика успешно добавлена!')
                    else:
                        print(f'Произошла ошибка! {res["error"]}')
                else:
                    print('Нет аргументов!')

            elif command=='/set_team':
                res=set_current_team()
                if res['success']:
                    current_team=res['result']
                    print('Команда успешно выбрана!')

            elif command=='/set_factory':
                res=set_current_factory(current_team=current_team)
                if res['success']:
                    current_factory=res['result']
                    print('Фабрика успешно выбрана')

            elif command=='/exit':
                break

            elif command=='/test':
                print(world.teams[0].factories)

        except:
            pass


main()