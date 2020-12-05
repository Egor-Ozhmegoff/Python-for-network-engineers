# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input("Введите ip адрес в формате 10.0.1.1:")
ip_list = list(ip.split("."))
correct_ip = False

if len(ip_list) != 4:
    correct_ip = True
else:
    for oct in ip_list :
        if not (oct.isdigit() and int(oct) in range(256)) :
	        correct_ip = True
        	break
if correct_ip :
    print("Неправильный IP-адрес")
else :
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
