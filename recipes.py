import json



def from_json(name: str):
    try:
        result={}
        with open('recipes.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            f.close()
        if not name in data.keys():
            print(f'Нет поля {name} в файле с данными!')
            return None
        if type(data[name]) != dict:
            return data[name]
        for k, v in data[name].items():
            if k.isdigit() or k =='-1':
                result[int(k)]=v
            else:
                result[k]=v
        return result
    except Exception as e:
        print(e)
        return None



recipes = from_json('recipes')
recipes_level = from_json('recipes_level')
rocket_level = from_json('rocket_level')
rockets = from_json('rockets')
transport = from_json('transport')
transport_levels=from_json('transport_levels')
craft_recipes=from_json('craft_recipes')
craft_levels=from_json('craft_levels')
advanced=from_json('advanced')
prices=from_json('prices')
resources=from_json('resources')
builds_data=from_json('builds')