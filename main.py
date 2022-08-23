from utils.json_handler import write_menu_list
from managemant.tab_handler import calc_menu

FILEPATH = 'menu.json'


def main():
    new_item = {"name": "CHURROS DO M8", "price": 5.0}

    write_menu_list(FILEPATH, new_item)
    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
    table_2 = [
      {"id": 10, "amount": 3},
      {"id": 20, "amount": 2},
      {"id": 21, "amount": 5},
    ]

    return calc_menu(table_1)

if __name__ == "__main__":
    # Utilize essa área para testes com print
    
    print(main())

    ...

