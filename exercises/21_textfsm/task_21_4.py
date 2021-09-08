# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
"""

from netmiko import ConnectHandler
from textfsm import clitable


def send_and_parse_show_command(device_dict, command, templates_path, index='index'):
    attributes = {'Command': command}
    cli_table = clitable.CliTable(index, templates_path)
    with ConnectHandler(**device_dict) as ssh:
        output = ssh.send_command(command)
        print(output)
        cli_table.ParseCmd(output, attributes)
        result = [dict(zip(cli_table.header, value)) for value in cli_table]
    return result
