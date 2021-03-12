# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""

import task_12_1
import task_12_2
from sys import argv
from tabulate import tabulate


def print_ip_table(ip_list):
    ip_dict = {}
    Reachable, Unreachble = ip_list
    ip_dict['Reachable'] = Reachable
    ip_dict['Unreachable'] = Unreachble
    print(tabulate(ip_dict, headers='keys'))


convert_ip = task_12_2.convert_ranges_to_ip_list(argv[1:])
sort_ip = task_12_1.ping_ip_addresses(convert_ip)