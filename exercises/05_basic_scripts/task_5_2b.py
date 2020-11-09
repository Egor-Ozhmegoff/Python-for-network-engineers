# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
network=argv[1]
ip, mask = network.split('/')
ip_list=ip.split('.')
mask = int(mask)

ip1,ip2,ip3,ip4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3])
]
bin_ip = "{:08b}{:08b}{:08b}{:08b}".format(ip1,ip2,ip3,ip4)
bin_subnet = bin_ip[:mask]+"0"*(32-mask)

oct1,oct2,oct3,oct4 = [
    int(bin_subnet[0:8],2),
    int(bin_subnet[8:16],2),
    int(bin_subnet[16:24],2),
    int(bin_subnet[24:32],2)
]
bin_mask ="1"*int(mask)+"0"*(32-int(mask))

m1,m2,m3,m4 = [
    int(bin_mask[0:8],2),
    int(bin_mask[8:16],2),
    int(bin_mask[16:24],2),
    int(bin_mask[24:32],2)
]
ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
mask_template = '''
Mask:
/{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:08b}
'''
print(ip_template.format(oct1,oct2,oct3,oct4))
print(mask_template.format(mask,m1,m2,m3,m4))
