import call
import time
c = call.Call(0,1,3,0,0)
c2 = call.Call(0,2,4,0,0)
c3 = call.Call(0,7,1,0,0)


def asc_destlist(list):
    return list.destination

destination_list = []

destination_list.append(c)
destination_list.append(c3)
destination_list.append(c2)


def asc_deplist(list):
    return list.departure



destination_list.sort(key=asc_destlist, reverse=True)

for i in range(0,3):
    print('desti list : ' ,destination_list[i].destination)


print('desti list : ' ,destination_list[0].destination)
# print('popped', destination_list.pop(0))

destination_list.sort(key=asc_deplist, reverse=True)

for i in range(0,3):
    print(' desti list : ' ,destination_list[i].departure)

"""
i = 0
while(i<6):


    print('destination : ',destination_list[i].destination)
    destination_list.pop()
    #time.sleep(1)
    i = i+1
"""