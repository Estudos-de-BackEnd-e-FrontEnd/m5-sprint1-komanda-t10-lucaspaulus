import json

def read_menu_list(filepath: str) -> list[dict]:
    try:
        with open(filepath, 'r', encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_menu_list(filepath: str, payload: dict):
    menu_list = read_menu_list(filepath)
    id_int = len(menu_list) + 1
    

    for item in menu_list:
        if item['name'] == payload['name']:
            print('item ja existe')
            return 'item ja existe'

    new_item = {'id': id_int, **payload}
    menu_list.append(new_item)

    with open(filepath, 'w') as file:
        json.dump(menu_list, file, indent=2)

