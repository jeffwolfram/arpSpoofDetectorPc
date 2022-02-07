import os
from datetime import datetime

def get_arp_table():
    parsed_log = {}
    list3 = []
    list2 = []
    list1 = []
    data = os.popen('arp -a').read()
    for line in data.splitlines():
        line.strip()
        parse = line.split(" ")
        b = ''.join(str(parse).split(','))
        c = ''.join(str(b).split("'"))
        list1.append(" ".join(str(c).split()))

    for i in list1[3::]:
        b = i.replace(" ", ",")
        list2.append(b[2:-2])

    for i in list2:
        if "nterface" in i or "Internet" in i:
            pass
        else:
            b = i.split(",")
            list3.append(b)
    for i in list3:
        if i != ['']:
            parsed_log[i[0]]=i[1]
    # for key, value in parsed_log.items():
    #     return parsed
    return parsed_log


def check_for_dups():
    mac_list = []
    dups = False
    for key, value in get_arp_table().items():
        if value != "ff-ff-ff-ff-ff-ff":
            mac_list.append(value)
    for mac_address in mac_list:
        if mac_list.count(mac_address) > 1:
            dups = True
    if dups:
        print("A duplicate Mac address has been detected.")
        return mac_list
    else:
        print("No duplicate mac address were found at this time.")

def add_to_log(data):
    if data != None:
        with open("dups.txt", "a+") as dups:
            dups.write(f"Duplicate found: {str(data)} - at: {datetime.now()} \n")

add_to_log(check_for_dups())