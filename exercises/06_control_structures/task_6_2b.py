# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите ip адрес в формате 10.0.1.1:")
ip_list = list(ip.split("."))
correct_ip = True

while correct_ip :
    if len(ip_list) != 4:
        correct_ip = False
    else:
        for oct in ip_list :
            if not (oct.isdigit() and int(oct) in range(256)) :
                correct_ip = False
                break
    if not correct_ip :
        print("Неправильный IP-адрес")
        ip = input("Введите ip адрес в формате 10.0.1.1:")
        ip_list = list(ip.split("."))
        correct_ip = True
    else :
        correct_ip = False
        oct1 = int(ip_list[0])
        if oct1 >= 1 and oct1 <= 223 :
            print("unicast")
        elif oct1 >= 224 and oct1 <= 239 :
            print("multicast")
        elif ip == '255.255.255.255' :
            print("broadcast")
        elif ip == '0.0.0.0' :
            print("unassigned")
        else :
            print("unused")
