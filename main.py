from classes import *

world=World()

def add_team(title):
    try:
        team=Team(title=title)
        world.add_team(team)
        return {'succes': True}
    except:
        return {'succes': False}

def add_factory(title, current_team):
    if current_team==None:
        print('Нет команд')
        return {'succes': False}
    try:
        factory=Factory(title=title)
        current_team.factories.append(factory)
        return {'succes': False}
    except:
        return {'succes': False}

def set_current_team():
    teams=[]
    n=1
    print('Выберите команду:')
    for team in world.teams:
        teams.append(team)
        print(f'{n}. {team.title}')
        n+=1
    t = int(input('Введите номер команды: '))
    try:
        return {'succes': True, 'result': teams[t-1]}
    except:
        print('Введён неверный номер')
        return {'succes': False}



def build():
    pass


def parse_commands(text):
    command=text.split(maxsplit=1)[0]
    args=text.split(maxsplit=1)[-1]
    return (command, args)

def main():
    current_team=None
    pass