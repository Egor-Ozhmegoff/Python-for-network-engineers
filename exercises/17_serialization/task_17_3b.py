# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует функция draw_topology из файла draw_network_graph.py).

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology из файла draw_network_graph.py.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""


import yaml
import re
from draw_network_graph import draw_topology


def transform_topology(topology):
    cdp_dict = {}
    cdp_dict2 = {}
    with open(topology, 'r') as f:
        cdp = yaml.safe_load(f)
        for key in cdp.keys():
            for value in cdp[key].keys():
                match = re.search(r"{'(\S+)': '(\w+ \S+)'}", str(cdp[key][value]))
                cdp_dict[(key, value)] = (match.group(1), match.group(2))
        for key2, value2 in cdp_dict.items():
            key2, value2 = sorted([key2, value2])
            cdp_dict2[key2] = value2
    return cdp_dict2


if __name__ == "__main__":
    print(transform_topology('topology.yaml'))
    draw_topology(transform_topology('topology.yaml'))
