# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает
вывод команды show dhcp snooping binding из разных файлов и записывает обработанные данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21


Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.
Первый столбец в csv файле имя коммутатора надо получить из имени файла, остальные - из содержимого в файлах.

"""

import re
import csv


def write_dhcp_snooping_to_csv(filenames, output):
    data = [['switch', 'mac', 'ip', 'vlan', 'interface']]
    regex = (r'(?P<mac>[\S+\:]+) +'
             r'(?P<ip>[\d+\.]+).* '
             r'(?P<vlan>\d+) +'
             r'(?P<interface>\w+\d+\S+)')
    for file in filenames:
        device = str(file).split('_')
        with open(file, 'r') as src:
            match_iter = re.finditer(regex, src.read())
            for match in match_iter:
                if match:
                    command = list(match.groups())
                    command.insert(0, device[0])
                    data.append(command)
    with open(output, 'w') as dst:
        writer = csv.writer(dst)
        for row in data:
            writer.writerow(row)