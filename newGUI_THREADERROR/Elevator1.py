# -*- coding: utf-8 -*-
import threading


import time
import DBN_ELEVATOR.constant
import datetime


def asc_destlist(list):
   return list.departure


class ElavatorThread1(threading.Thread):

   dasom = 23
   # dialog = simulator.Ui_Dialog()
   # ui = simulator.Ui_MainWindow()
   # dialog = simulator.Ui_Dialog()



   def __init__(self, parent = None):
       threading.Thread.__init__(self)


       super(ElavatorThread1, self).__init__()
       self._stop = threading.Event()

       self.dests = []
       self.departure_floors = []
       self.destination_floors = []
       self.call_number = 0
       self.destination_floor = 0

       self.total_waiting =0
       self.current_waiting = 0
       self.max_waiting = 0
       self.now = 0
       self.dbn_calls =[]






   def stop(self):
       self._stop.set() # 1

   def clear(self):
       return self._stop.clear() #0



   def setDasom(self, uidasom):
       self.tn =uidasom

   def getDasom(self):
       return self.dasom


   def setUI(self, uiUI):
       self.ui =uiUI

   def getUI(self):
       return self.ui

   def setDialog(self,uiDialog):
       self.dialog = uiDialog
   def setElevator_rack(self, elevator_rack, re):
       self.elevator_rack = elevator_rack
       self.re = re


   def run(self):

       print("thread 1 ")

       # print('thread 2 ')
       # 콜이 있는지 없는지 확인하는 것
       while (1):



           #if(self.elevator_rack.ready_calls[0] != None or len(self.dests) != 0):
           if(len(self.elevator_rack.ready_calls) != 0 ):
                   self.now =0

                   if(self.elevator_rack.state == DBN_ELEVATOR.constant.IDLE_STATE):
                       print('____IDLE STATE1___', self.elevator_rack.ready_calls[0].departure ,'->', self.elevator_rack.ready_calls[0].destination )
                       self.ui.showcall( 0,self.elevator_rack.ready_calls[0].departure ,self.elevator_rack.ready_calls[0].destination, 'GO TO DEP')
                       # 나보다 위에 층이면 올라간다

                       # 같은 충이면 태운다
                       if(int(self.elevator_rack.floor) == int(self.elevator_rack.ready_calls[0].departure)):
                           time.sleep(1.33)
                           print('arrived to destination floor..')
                           self.elevator_rack.state = DBN_ELEVATOR.constant.LOAD_STATE
                           if( self.elevator_rack.ready_calls[0].isup == 't'):
                               self.elevator_rack.direction = DBN_ELEVATOR.constant.UP_DIRECTION # 1이 up 2 가 down
                           else:
                               self.elevator_rack.direction = DBN_ELEVATOR.constant.DOWN_DIRECTION

                           # 목적층을 도착층으로 바꾼다.
                           self.destination_floor = self.elevator_rack.ready_calls[0].destination



                       # 나보다 위면 방향설정
                       elif(int(self.elevator_rack.floor) < int(self.elevator_rack.ready_calls[0].departure)):
                           time.sleep(1)
                           print('UP_DIRECTION :: elevator_floor : ' ,self.elevator_rack.floor, 'call departure : ' , self.elevator_rack.ready_calls[0].departure)
                           #self.elevator_rack.floor +=1
                           #self.ui.up(1)


                           self.elevator_rack.state = DBN_ELEVATOR.constant.LOAD_STATE
                           self.elevator_rack.direction = DBN_ELEVATOR.constant.UP_DIRECTION

                           #print('self.elevator_rack' , self.elevator_rack.ready_calls[0].destination)
                           self.destination_floor = self.elevator_rack.ready_calls[0].departure

                           # print('elevator pop :  ', self.elevator_rack.ready_calls[0].destination)

                           #self.dests.append(self.elevator_rack.ready_calls.pop())
                       # 나보다 아래면 내려가는 방향으로 설정
                       elif(int(self.elevator_rack.floor) > int(self.elevator_rack.ready_calls[0].departure)):
                           time.sleep(1)
                           # print('1floor down')
                           #self.elevator_rack.floor -=1
                           #self.ui.down(1)

                           self.elevator_rack.state = DBN_ELEVATOR.constant.LOAD_STATE
                           self.elevator_rack.direction = DBN_ELEVATOR.constant.DOWN_DIRECTION

                           self.destination_floor = self.elevator_rack.ready_calls[0].departure

                           #self.dests.append(self.elevator_rack.ready_calls.pop())

                   if(self.elevator_rack.state == DBN_ELEVATOR.constant.LOAD_STATE):
                       #print('____LOADSTATE_____')
                       ### 1. 레디콜스에 새 콜이 있자나 그 콜을 데스트에 들어갈 수 있는지 검사해서 담는다(departure, destination).
                       ### 2. 오름차순 또는 내림차순으로 정렬한다.

                       #

                       # 로드스테이트여도 엘레베이터의 층과 콜의 0번의 출발층이 같으면 기다리면서
                       # 출발층에 에 해당하는 층에 도착했는가
                       if(int(self.elevator_rack.floor) == int(self.elevator_rack.ready_calls[0].departure) and self.elevator_rack.ready_calls[0].flag == 0 ):
                           print('ThreadEli2 :: arrived at calls departure floor ' )
                           print('ThreadEli2 :: people get in...')
                           self.ui.showcall( 0,self.elevator_rack.ready_calls[0].departure ,self.elevator_rack.ready_calls[0].destination, 'ARRIVED DEP')
                           # 출발 목적층에 도착하였으니 멈춤 상태로 전환
                           #self.elevator_rack.state = constant.STOP_STATE
                           # 사람이 타고 내리는 시간 sleep

                           st = str(self.elevator_rack.ready_calls[0].register_time)
                           print(st)
                           dateSplit = st.split('.')
                           registertime = datetime.datetime.strptime(dateSplit[0], "%Y-%m-%d %H:%M:%S")


                           regist_sec = registertime.hour*3600 + registertime.minute *60 +registertime.second
                           self.getin_sec = self.dialog.timer[2]  + self.dialog.timer[1]*60 + self.dialog.timer[0] * 3600

                           self.elevator_rack.ready_calls[0].setwaiting(regist_sec,self.getin_sec)

                           #self.elevator_rack.ready_calls[0].waiting
                           self.total_waiting += self.getin_sec - regist_sec
                           print('E1 : total waiting : sum ', self.total_waiting)

                           self.current_waiting = self.getin_sec - regist_sec

                           if(self.current_waiting > self.max_waiting):
                               self.max_waiting = self.current_waiting

                           self.ui.waiting(0, self.total_waiting)
                           print('E1_totalWaiting!!!!!!!!!!')
                           print(self.max_waiting)



                           self.elevator_rack.ready_calls[0].flag = 1
                           self.elevator_rack.state = DBN_ELEVATOR.constant.LOAD_STATE
                           self.destination_floor = self.elevator_rack.ready_calls[0].destination
                           time.sleep(2)
                           self.ui.showcall( 0,self.elevator_rack.ready_calls[0].departure ,self.elevator_rack.ready_calls[0].destination, 'GO TO DES')

                       if(int(self.elevator_rack.floor) == int(self.elevator_rack.ready_calls[0].destination) and self.elevator_rack.ready_calls[0].flag == 1):
                           self.ui.showcall( 0,self.elevator_rack.ready_calls[0].departure ,self.elevator_rack.ready_calls[0].destination, 'ARRIVED DES')
                           print('elevator current floor info :equal: ', self.elevator_rack.floor)
                           # 제일 앞에 꺼 제거거

                           self.getout_sec = self.dialog.timer[2]  + self.dialog.timer[1] *60 + self.dialog.timer[0] * 3600
                           self.elevator_rack.ready_calls[0].setriding(self.getout_sec,self.getin_sec)


                           # 출발 목적층에 도착하였으니 멈춤 상태로 전환
                           self.elevator_rack.state = DBN_ELEVATOR.constant.STOP_STATE
                           # 사람이 타고 내리는 시간 sleep
                           time.sleep(2)





                       elif(int(self.elevator_rack.floor) < int(self.destination_floor)):

                           time.sleep(1.33)
                           self.ui.up(1)
                           self.elevator_rack.floor += 1

                           print('elevator current floor info :lower: ', self.elevator_rack.floor, ' int(self.destination_floor)  :: ',int(self.destination_floor))

                           self.elevator_rack.state = DBN_ELEVATOR.constant.LOAD_STATE

                           #destination_list.sort(key=asc_destlist, reverse=True)
                           # 지금 층이랑 디파처플로어 목록중에 출발층이랑 같니?
                           #for i in range(0,3):
                           #print('desti list : ' ,self.departure_floors[0].departure)

                           #self.dests.append(self.elevator_rack.ready_calls.pop())

                       elif(int(self.elevator_rack.floor) > int(self.destination_floor)):
                           time.sleep(1.33)
                           self.ui.down(1)
                           self.elevator_rack.floor -= 1
                           print('elevator current floor info :higher: ', self.elevator_rack.floor)
                           self.elevator_rack.state = DBN_ELEVATOR.constant.LOAD_STATE
                           # self.dests.append(self.elevator_rack.ready_calls.pop())

                   # 사람을 태우려고 멈추었을 때. 또는 동작을 만족하였을때.
                   if(self.elevator_rack.state == DBN_ELEVATOR.constant.STOP_STATE):
                       print('people get in…')

                       # 시간 가지고 와서 - + 10분

                       # 10 분 을 그 시간에 더해주고 그 사이에 콜이 있는지 검사
                       time.sleep(5)#가지고 온 사람 타는 시간만틈 더해서 슬립)
                       self.ui.showcall( 0,self.elevator_rack.ready_calls[0].departure ,self.elevator_rack.ready_calls[0].destination, 'IDLE')
                       callrecord = self.elevator_rack.ready_calls.pop(0)
                       self.dbn_calls.append(callrecord)
                       self.elevator_rack.record_calls.append(callrecord)
                       #self.dbn_calls.append(self.elevator_rack.ready_calls.pop(0))
                       self.elevator_rack.state = DBN_ELEVATOR.constant.IDLE_STATE

                       self.now = self.dialog.timer[2]
                       self.now_min = self.dialog.timer[1]


           else:
               if(self.now == 0):
                   print("E1 now가 0일때")
                   #self.now = time.localtime()
                   #self.now = self.dialog.timer[2]
                   #self.now_min = self.dialog.timer[1]
                   self.now = self.dialog.timer[2]
                   self.now_min = self.dialog.timer[1]
                   time.sleep(1)


               else:

                   #if(self.now.tm_min == time.localtime().tm_min and self.now.tm_sec+20 <= time.localtime().tm_sec):
                   if self.dialog.timer[1]*60 +self.dialog.timer[2] >= self.now_min*60 + self.now+20 :
                       print(" E1 : 20초가 지났을 때")
                       #print self.dbn_calls[-1]매개변수로 넣기

                       if(len(self.dbn_calls)!=0):
                           self.destination_floor = DBN_ELEVATOR.dbn.predict(self.dbn_calls.pop(-1))
                           #self.dbn_calls.pop(0)
                           #for i in range(0,len(self.dbn_calls)):
                           #    self.dbn_calls.pop(i)

                       if(int(self.elevator_rack.floor) == int(self.destination_floor)):
                           self.elevator_rack.state = DBN_ELEVATOR.constant.IDLE_STATE
                           self.now = 0
                           # 여기서 쓰레드 stop
                           #self.__suspend = True
                           print("E1 suspended")
                           self.re.record(self.elevator_rack)
                           self._stop.clear()

                           self._stop.wait() # 1이면 즉시 리턴해 주는 함수 : 기본이 0이므로 기다린다.
                           print("E1 suspended FREE")



                       elif(int(self.elevator_rack.floor) < int(self.destination_floor)):
                           time.sleep(1.33)
                           self.ui.up(1)
                           self.elevator_rack.floor += 1
                           print('elevator current floor info :lower: ', self.elevator_rack.floor, ' int(self.destination_floor)  :: ',int(self.destination_floor))
                           self.elevator_rack.state = DBN_ELEVATOR.constant.DEEP_STATE


                       elif(int(self.elevator_rack.floor) > int(self.destination_floor)):
                           time.sleep(1.33)
                           self.ui.down(1)
                           self.elevator_rack.floor -= 1
                           print('elevator current floor info :higher: ', self.elevator_rack.floor)
                           self.elevator_rack.state = DBN_ELEVATOR.constant.DEEP_STATE
                       """
                       for i in range(0,len(self.dbn_calls)):
                           self.dbn_calls.pop(i)
                       """
