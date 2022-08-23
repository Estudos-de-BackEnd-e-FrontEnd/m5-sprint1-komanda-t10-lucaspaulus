 
from datetime import datetime
from utils.json_handler import read_menu_list
FILEPATH = 'menu.json'

def get_item_menu(filepath: str, id: int):
    items_list = read_menu_list(filepath)

    for items in items_list:
        if items['id'] == id:
            return items
       
    return 'item não encontrado'


def calc_menu(table):
    date_time_format = '%d/%m/%Y, %H:%M:%S'
    total = 0

    for item in table:
        id = item['id']
        qtd = item['amount']
        get_item = get_item_menu(FILEPATH, id)
        price = get_item['price']

        total += price * qtd


    output = {'subtotal': total, 'created_at': datetime.now().strftime(date_time_format)}
    return output


    