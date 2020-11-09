# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
interface = {
    "access" : {
        "template": access_template,
        "vlan": 'VLAN',
    },
    "trunk" : {
        "template" : trunk_template,
        "vlan" : 'VLANы',
    }
}
int_mode = input('Введите режим работы интерфейса:')
int_number = input ('Введите номер интерфейса :')
int_vlan = input (f'Введите номер {interface[int_mode]["vlan"]} :')

print('interface {}'.format(int_number))
print('\n'.join(interface[int_mode]["template"]).format(int_vlan))

