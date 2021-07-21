# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов
 
Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess


def ping_ip_addresses(ip_list):
    reachable = []
    unreachable = []
    for ip in ip_list:
        ping = subprocess.run(['ping', '-c', '4', '-n', ip], stdout=subprocess.DEVNULL)
        if ping.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    result = (reachable, unreachable)
    return result


