# -*- coding: utf-8 -*-
"""
Задание 20.5a

Создать функцию configure_vpn, которая использует шаблоны из задания 20.5 для настройки VPN на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве с помощью netmiko.
Функция возвращает вывод с набором команд с двух марушртизаторов (вывод, которые возвращает метод netmiko send_config_set).

При этом, в словаре data не указан номер интерфейса Tunnel, который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 9.
И надо будет настроить интерфейс Tunnel 9.

Для этого задания нет теста!
"""


import os
from task_20_5 import create_vpn_config
from netmiko import (ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException)
from jinja2 import Environment, FileSystemLoader


data = {
    "tun_num": None,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}

def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    try:
        src_int = []
        dst_int = []
        with ConnectHandler(**src_device_params) as ssh_src, ConnectHandler(**dst_device_params) as ssh_dst:
            src_tun_info = ssh_src.send_command('sh ip int brief')
            dst_tun_info = ssh_dst.send_command('sh ip int brief')
            for line in src_tun_info:
                if 'Tunnel' in line:
                    src_int.append(line.split(' ')[0])
            for line in dst_tun_info:
                if 'Tunnel' in line:
                    dst_int.append(line.split(' ')[0])
            int_info = list(set(zip(src_int, dst_int)))
            for num in range(100):
                if f'Tunnel{num}' not in int_info:
                    vpn_data_dict["tun_num"] = f'Tunnel{num}'
                    break
            template = create_vpn_config(src_template, dst_template, vpn_data_dict)
            result_src = ssh_src.send_config_set(template[0])
            result_dst = ssh_dst.send_config_set(template[1])
        return result_src, result_dst
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)