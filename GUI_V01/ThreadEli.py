# -*- coding: utf-8 -*-
"""
import threading
import dataParsing as data
import elevatorMove as move
import simulator
import time
import constant

def asc_destlist(list):
    return list.departure


class ElavatorThread1(threading.Thread):

    dasom = 23
    ui = simulator.Ui_MainWindow()
    dialog = simulator.Ui_Dialog()

    def __init__(self, parent = None):
        threading.Thread.__init__(self)
        self.call_number = 0

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
    def setElevator_rack(self, elevator_rack):
        self.elevator_rack = elevator_rack


    def run(self):

        print("thread 1 ")






class ElavatorThread2(threading.Thread):
    dasom = 23
    ui = simulator.Ui_MainWindow()
    dialog = simulator.Ui_Dialog()


    def __init__(self, parent = None):
        threading.Thread.__init__(self)
        self.dests = []
        self.departure_floors = []
        self.destination_floors = []

        self.destination_floor = 0

    def setDasom(self, uidasom):
        self.dasom =uidasom

    def getDasom(self):
        return self.dasom

    def setUI(self, uiUI):
        self.ui =uiUI

    def getUI(self):
        return self.ui

    def setDialog(self, uidialog):
        self.dialog = uidialog
    def setElevator_rack(self, elevator_rack):
        self.elevator_rack = elevator_rack

    def run(self):
        print('thread 2 ')
        # 콜이 있는지 없는지 확인하는 것
        while (1):

            #if(self.elevator_rack.ready_calls[0] != None or len(self.dests) != 0):
            if(len(self.elevator_rack.ready_calls) != 0 or len(self.dests) != 0):
                # print(self.elevator_rack.ready_calls[0].departure)
                #  엘레베이터의 스테이트를 계속 확인하는 while문
                # while(1):
                    # 1. idle 일 때 - 첫번째 콜을 받아서 목적층 콜리스트에 넣고 운행상태로 바꾼다
                    # if( len(self.elevator_rack.ready_calls) == 1):
                    #    print('one value : ', len(self.elevator_rack.ready_calls) )

                    if(self.elevator_rack.state == constant.IDLE_STATE):
                        print('____IDLE STATE___')
                        # 나보다 위에 층이면 올라간다
                        if(int(self.elevator_rack.floor) == int(self.elevator_rack.ready_calls[0].departure)):
                            time.sleep(1.33)
                            print('arrived to destination floor..')
                            self.elevator_rack.state = constant.LOAD_STATE
                            self.elevator_rack.direction = self.elevator_rack.ready_calls[0].isup+1 # 1이 up 2 가 down
                            # 목적콜들로 담는다 - 전체 관리하는 dests, 콜의 출발층만 관리 departure_floor, 콜의 목적층만 관리 destination_floor
                            self.dests.append(self.elevator_rack.ready_calls[0])
                            self.destination_floors.append(self.elevator_rack.ready_calls[0])
                            self.departure_floors.append(self.elevator_rack.ready_calls.pop(0))



                        elif(int(self.elevator_rack.floor) < int(self.elevator_rack.ready_calls[0].departure)):
                            time.sleep(1)
                            print('elevator_floor : ' ,self.elevator_rack.floor, 'call departure : ' , self.elevator_rack.ready_calls[0].departure)
                            #self.elevator_rack.floor +=1
                            #self.ui.up(1)

                            self.elevator_rack.state = constant.LOAD_STATE
                            self.elevator_rack.direction = constant.UP_DIRECTION
                            self.dests.append(self.elevator_rack.ready_calls[0])
                            self.destination_floors.append(self.elevator_rack.ready_calls[0])
                            print('self.elevator_rack' , self.elevator_rack.ready_calls[0].destination)
                            self.departure_floors.append(self.elevator_rack.ready_calls.pop(0))

                            # print('elevator pop :  ', self.elevator_rack.ready_calls[0].destination)

                            #self.dests.append(self.elevator_rack.ready_calls.pop())
                        # 나보다 아래면 내려간다
                        elif(int(self.elevator_rack.floor) > int(self.elevator_rack.ready_calls[0].departure)):
                            time.sleep(1)
                            print('1floor down')
                            #self.elevator_rack.floor -=1
                            #self.ui.down(1)

                            self.elevator_rack.state = constant.LOAD_STATE
                            self.elevator_rack.direction = constant.DOWN_DIRECTION

                            self.dests.append(self.elevator_rack.ready_calls[0])
                            self.destination_floors.append(self.elevator_rack.ready_calls[0])
                            self.departure_floors.append(self.elevator_rack.ready_calls.pop(0))

                            #self.dests.append(self.elevator_rack.ready_calls.pop())

                    if(self.elevator_rack.state == constant.LOAD_STATE):
                        #print('____LOADSTATE_____')
                        ### 1. 레디콜스에 새 콜이 있자나 그 콜을 데스트에 들어갈 수 있는지 검사해서 담는다(departure, destination).
                        ### 2. 오름차순 또는 내림차순으로 정렬한다.


                        # 같은 방향이고 업이면 위거나 다운이면 아래일 때 담는다.

                        # 1. dests 에 콜이 없을 때는 readycalls 에서 제일 앞의 콜 객체를 데스트에 가지고 온다.
                        # ready_calls에 남아있니?
                        #if(self.elevator_rack.ready_calls[0] != None): # ready_calls에 콜이 남아있으면 처리한다  : if(self.elevator_rack.ready_calls != None )
                        if(len(self.elevator_rack.ready_calls) > 0):
                            if(self.dests == None): # dests배열이 너이면
                                #제일 가까운 걸 가지고 온다.
                                self.dests.append(self.elevator_rack.ready_calls[0]) # 일단은 0번콜
                            else:
                                # 2. 콜이 있을때는, 방향 체크(엘레베이터의 방향 == ready_calls에서 막 가지고 온 그 콜) 같은방향, 진행방향보다 앞인 콜만 가지고 온다.
                                # self.dests에 담는다
                                #print(' self.elevator.ready_calls[0] ::', self.elevator_rack.ready_calls[0].isup)
                                if(self.elevator_rack.direction == self.dests[0].isup): #몰라 알수가없어 이렇게 ㅘㅏㅛㅓ러홍츠프ㅗ 그 콜의 방향이랑 엘베 방향이랑 같니?
                                    self.dests.append(self.elevator_rack.ready_calls[0])
                                    self.departure_floors.append(self.elevator_rack.ready_calls[0])
                                    self.destination_floors.append(self.elevator_rack.ready_calls.pop(0))
                                else: #방향이 다를 때
                                    # 일단 맨 뒤로 보낼까
                                    sendtoback = self.elevator_rack.ready_calls.pop(0)
                                    self.elevator_rack.ready_calls.append(sendtoback)

                        elif(self.elevator_rack.ready_calls == None): # no
                            if(self.dests  == None):
                                self.elevator_rack.state = constant.IDLE_STATE
                            else:
                                print('pass on this time : ')


                        ### 2. 여기서 목적지 콜 목록 정렬 -  self.destination_floor 랑 departure_floor

                        # 목적지로 정렬함수
                        def asc_destlist(list):
                            return list.destination

                        # 출발지로 정렬함수
                        def asc_deplist(list):
                            return list.departure


                        # 오름차순으로 내림차순으로 정렬 - if(up이면 오름차순) else(down이면 내림차순)
                        if( self.destination_floors !=None and self.departure_floors != None and self.dests[0].isup == 1 ): # 1 up
                            self.destination_floors.sort(key=asc_destlist, reverse=True)
                            self.departure_floors.sort(key=asc_deplist, reverse=True)
                        elif(self.destination_floors !=None and self.departure_floors != None and self.dests[0].isup == 0): # 0 down
                            self.destination_floors.sort(key=asc_destlist, reverse=False)
                            self.departure_floors.sort(key=asc_deplist, reverse=False)

                        # if dest None 이면 - ready_calls랑 현재 위치에서 제일 가까운 목적지 지정해서 변수로 갖는다.


                        # destination_floors 와 departure_floors[0]을 비교해서 더 작은 게 self.destination_floor의 값이다.
                        if(self.destination_floors[0] < self.departure_floors[0]):
                            self.destination_floor = self.destination_floors[0].destination
                        else:
                            self.destination_floor = self.departure_floors[0].departure

                         #if(self.departure_floors == self.departure_floors[0].departure):
                         #    self.destination_floor = self.departure_floors[0]
                         #if( self.departure_floors == self.destination_floors[0].destination):
                         #     self.destination_floor = self.departure_floors[0]


                        #

                        # 로드스테이트여도 엘레베이터의 층과 콜의 0번의 출발층이 같으면 기다리면서
                        # departure_floor 에 해당하는 층에 도착했는가
                        if(int(self.elevator_rack.floor) == self.destination_floor ):
                            print('ThreadEli :: arrived at calls departure floor ' )
                            print('ThreadEli :: people get in...')
                            print('elevator current floor info :equal: ', self.elevator_rack.floor)
                            # 출발 목적층에 도착하였으니 멈춤 상태로 전환
                            self.elevator_rack.state = constant.STOP_STATE


                            # departure_floors 검색해서 같은 값 삭제하고,
                            #순차검색
                            for i in range(0, len(self.departure_floors)):
                                if self.departure_floors[i].departure == self.destination_floor:
                                    self.departure_floors.pop(i)




                            # destination_floors 검색해서 같은 값 삭제하고, --> 이 때 dests 의 해당 콜을 삭제
                            for i in range(0, len(self.destination_floors)):
                                if self.destination_floors[i].departure == self.destination_floor:

                                    for j in range(0, len(self.dests)):
                                        if self.dests[j].register_time == self.destination_floors[i].register_time:
                                            self.destination_floors.pop(i)
                                            self.dests.pop(j)

                            time.sleep(2)

                            current_call = self.departure_floors.pop(0)



                        elif(int(self.elevator_rack.floor) < int(self.destination_floor)):

                            time.sleep(1.33)
                            self.ui.up(1)
                            self.elevator_rack.floor += 1

                            print('elevator current floor info :lower: ', self.elevator_rack.floor, ' int(self.destination_floor)  :: ',int(self.destination_floor))

                            self.elevator_rack.state = constant.LOAD_STATE

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
                            self.elevator_rack.state = constant.LOAD_STATE
                            # self.dests.append(self.elevator_rack.ready_calls.pop())

                    # 사람을 태우려고 멈추었을 때. 또는 동작을 만족하였을때.
                    if(self.elevator_rack.state == constant.STOP_STATE):
                        if(int(self.elevator_rack.floor) == int(self.destination_floor)):
                            print('people get in…')


                            time.sleep(2)#가지고 온 사람 타는 시간만틈 더해서 슬립)
                            self.elevator_rack.state = constant.IDLE_STATE

            else:
                self.elevator_rack.state = constant.IDLE_STATE
                print('no value ')










class ElavatorThread3(threading.Thread):
    dasom = 23
    ui = simulator.Ui_MainWindow()
    dialog = simulator.Ui_Dialog()

    def __init__(self, parent = None):
        threading.Thread.__init__(self)

    def setDasom(self, uidasom):
        self.dasom =uidasom

    def getDasom(self):
        return self.dasom

    def setUI(self, uiUI):
        self.ui =uiUI

    def getUI(self):
        return self.ui

    def setDialog(self, uidialog):
        self.dialog = uidialog
    def setElevator_rack(self, elevator_rack):
        self.elevator_rack = elevator_rack

    def run(self):
        print('thread 3 ')


class ElavatorThread4(threading.Thread):
    dasom = 23
    ui = simulator.Ui_MainWindow()
    dialog = simulator.Ui_Dialog()
    def __init__(self, parent = None):
        threading.Thread.__init__(self)

    def setDasom(self, uidasom):
        self.dasom =uidasom

    def getDasom(self):
        return self.dasom

    def setUI(self, uiUI):
        self.ui =uiUI

    def getUI(self):
        return self.ui

    def setDialog(self, uidialog):
        self.dialog = uidialog

    def setElevator_rack(self, elevator_rack):
        self.elevator_rack = elevator_rack

    def run(self):
        print('thread 4 ')
"""