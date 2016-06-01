

import call
import dataParsing as gdata

c = call.Call(0,0,3,0,0)
c2 = call.Call(0,0,4,0,0)
c3 = call.Call(0,0,1,0,0)


def asc_destlist(list):
    return list.destination

destination_list = []

destination_list.append(c)
destination_list.append(c3)
destination_list.append(c2)


destination_list.sort(key=asc_destlist, reverse=True)

for i in range(0,3):
    print('desti list : ' ,destination_list[i].destination)
                            

print('popped', destination_list.pop(0))

for i in range(0,3):
    print('\ndesti list : ' ,destination_list[i].destination)

tn = 0
while tn <100:
    registertime = gdata.getData(tn)
    if(10 == registertime.minute):
         if(self.dialog.timer[2] == registertime.second and self.dialog.timer[1] == registertime.minute and self.dialog.timer[0] == registertime.hour):
                call = self.getcall(self.ui, self.tn)  # 시간 같으면 콜을 발생시킨다.
                allocated_elevator = self.allocate(call)
                allocated_elevator = int(allocated_elevator)
                # 할당받은 엘리베이터의 배열에 넣겠다
                    self.elevator_calls.append(call)
                    self.elevator_rack[allocated_elevator].ready_calls.append(call)
                    if(allocated_elevator == 4):
                        t4.setElevator_rack(self.elevator_rack[3])

                    print "elevator"
                    print self.elevator_rack[allocated_elevator].ready_calls[0]
                    self.tn +=1