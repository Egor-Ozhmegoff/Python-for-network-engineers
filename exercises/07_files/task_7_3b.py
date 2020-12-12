# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
what_vlan = int(input('Введите номер vlan:'))

mac_table = []

with open('CAM_table.txt','r') as f:
    for line in f:
        line = line.split()
        if line and line[0].isdigit():
            vlan,mac,_,interface = line
            mac_table.append([int(vlan),mac,interface])
    for vlan,mac,interface in sorted(mac_table):
        if what_vlan == vlan:
            print("{:<4}  {:<14}  {:<6}".format(vlan,mac,interface))
