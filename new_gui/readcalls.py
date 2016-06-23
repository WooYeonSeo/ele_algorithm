# -*- coding: utf-8 -*-
import threading
import simulator
import dataParsing as gdata
import constant
import math
import random
import time
import call as c

# http://saelly.tistory.com/510
class Readcalls(threading.Thread):
    def __init__(self, parent=None):
        threading.Thread.__init__(self)
        self.call_number = 0
        self.current_floor_term = 20  # 층 차이값일단 최대로 줌
        self.threadFlag = [0]*4


    def settn(self, tn):
        self.tn = tn

    def setElevator_rack(self, elevator_rack, t1, t2, t3, t4):
        self.elevator_rack = elevator_rack
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4

    def setUI(self, uiUI):
        self.ui = uiUI

    def getUI(self):
        return self.ui

    def setDialog(self, uiDialog):
        self.dialog = uiDialog

    def setcalllist(self, elevator_calls):
        self.elevator_calls = elevator_calls

    def run(self):
        self.tn += 1  # 다음 투플로 넘긴다음에 와일문 돌리기
        while (self.tn < 10000):
            if self.tn < 10000:
                # dataSplit = gdata.dataSet[self.tn][0].split('.')
                registertime = gdata.getData(
                    self.tn)  # gdata.datetime.datetime.strptime(dataSplit[0],"%Y-%m-%d %H:%M:%S")

                if self.dialog.timer[2] == registertime.second and self.dialog.timer[1] == registertime.minute and \
                                self.dialog.timer[0] == registertime.hour:
                    call = self.getcall(self.tn)  # 시간 같으면 콜을 발생시킨다.
                    allocated_elevator = self.allocate2(call)
                    allocated_elevator = int(allocated_elevator)

                    print("getcall!!!  + allocated elevator num : ", allocated_elevator)

                    # flag가 1로 스탑이라는데 할당된 엘리베이터가 0번 이면(새 콜이 들어왔다는 거) 다시 플래그를 운행중인 0 으로 바꾸어준다
                    # if( self.threadFlag ==1 and allocated_elevator == 0 ): # 정지상태가 아닌
                    #    self.threadFlag = 0

                    # 할당받은 엘리베이터의 배열에 넣겠다
                    self.elevator_rack[allocated_elevator].ready_calls.append(call)
                    self.tn += 1

                     # 1이면 즉시 리턴해 주는 함수 : 기본이 0이므로 기다린다. set - run :  clear - stop
                    for i in range(0, 4):
                        # 콜이 없는데 실행중이면 멈추고 스탑으로flag=1바꿈
                        if (i == 0):
                            print("EL1 flag : ", self.threadFlag[i], "readycall length",len(self.elevator_rack[i].ready_calls))
                            if (len(self.elevator_rack[i].ready_calls) == 0 and self.threadFlag[i] == 0):
                                print('EL1 콜이 없고 실행플래그 : 정지시킨다, 정지로 플래그 변경')
                                self.t1._stop.clear()
                                self.threadFlag[i] = 1
                            elif (len(self.elevator_rack[i].ready_calls) != 0 and self.threadFlag[i] == 1):
                                print('EL1 콜이 있는데 정지플래그 : 쓰레드 실행시킨다, 실행으로 플래그 변경')
                                self.t1._stop.set()
                                self.threadFlag[i] = 0

                        elif (i == 1):
                            print("EL2 flag : ", self.threadFlag[i], "readycall length",len(self.elevator_rack[i].ready_calls))
                            if (len(self.elevator_rack[i].ready_calls) == 0 ):
                                print('EL2 콜이 없고 실행플래그 : 정지시킨다, 정지로 플래그 변경')
                                self.t2._stop.clear()
                                #self.threadFlag[i] = 1
                            elif (len(self.elevator_rack[i].ready_calls) != 0 ):
                                print('EL2 콜이 있는데 정지플래그 : 쓰레드 실행시킨다, 실행으로 플래그 변경')
                                self.t2._stop.set()
                                #self.threadFlag[i] = 0

                        elif (i == 2):
                            print("EL3 flag : ", self.threadFlag[i], "readycall length",len(self.elevator_rack[i].ready_calls))
                            if (len(self.elevator_rack[i].ready_calls) == 0 ):
                                print('EL3 콜이 없고 실행플래그 : 정지시킨다, 정지로 플래그 변경')
                                self.t3._stop.clear()
                                #self.threadFlag[i] = 1
                            elif (len(self.elevator_rack[i].ready_calls) != 0 ):
                                print('EL3 콜이 있는데 정지플래그 : 쓰레드 실행시킨다, 실행으로 플래그 변경')
                                self.t3._stop.set()
                                #self.threadFlag[i] = 0
                        elif (i == 3):
                            print("EL4 flag : ", self.threadFlag[i], "readycall length",len(self.elevator_rack[i].ready_calls))
                            if (len(self.elevator_rack[i].ready_calls) == 0 ):
                                print('EL4 콜이 없고 ')
                                self.t4._stop.clear()
                                #self.threadFlag[i] = 1
                            elif (len(self.elevator_rack[i].ready_calls) != 0 ):
                                print('EL4 콜이 있는데 ')
                                self.t4._stop.set()
                                #self.threadFlag[i] = 0



                time.sleep(0.4)


                # 가지고 온 시간이 지난 시간의 것이면 pass
            # self.tn이 100번째가 넘어가면 나간다 와일문
            else:
                break

    def getcall(self, tn):  # ui객체를 받아와야 된다
        # index = 0
        # 데이터의 시간을 가지고와서 배열에 넣어 놓는다,- 아무튼 시간을 가지고 온다는 뜻

        # tn = 투플넘버를가지고 옵시다 - dataparsing에 접근
        registertime = gdata.getData(tn)

        departure_floor = gdata.dataSet[tn][2]
        destination_floor = gdata.dataSet[tn][3]
        # iserroroccured = gdata.dataSet[tn][13]
        is_up = gdata.dataSet[tn][4]
        passenger = 3  # 일단은 세명이라고 했음

        # 데이터 추가
        dbn_register_time = gdata.dataSet[tn][1]  # 수정
        day_of_week = gdata.dataSet[tn][5]
        iserror = gdata.dataSet[tn][6]
        weekend = gdata.dataSet[tn][7]  # 수정
        register15min = gdata.dataSet[tn][8]

        # call생성
        # self, register_time, departure_floor,destination_floor, isup, passenger, dbn_register_time, day_of_week, iserror, weekend, register15min)

        # register_time, departure_floor,destination_floor, isup, passenger, dbn_register_time, day_of_week, iserror, weekend, register15min):
        new_call = c.Call(registertime, departure_floor, destination_floor, is_up, passenger, dbn_register_time,
                          day_of_week, iserror, weekend, register15min)  # 1이 up, 0이 down

        # register_time, departure_floor,destination_floor, isup, passenger, dbn_register_time, day_of_week, iserror, weekend, register15min):
        # new_call = c.Call(registertime, departure_floor, destination_floor, is_up, passenger, dbn_register_time,day_of_week,iserror,weekend, register15min)  # 1이 up, 0이 down
        self.elevator_calls.append(new_call)
        print('departure_floor : ', new_call.departure, ' --> ', new_call.destination)
        self.elevator_calls.append(new_call)  # 나중에 waitingtime 계산할때 쓸라고 배열에 담아놓는다.

        # print( self.elevator_calls[0].departure + ' ::: departure')

        return new_call

    # allocate for one by one
    def allocate2(self, call):
        # 엘레베이터들의 위치를 가진다

        close_ele = 0  # 가장 가까운 엘레베이터 번호
        # 층 차이값일단 최대로 줌
        floor_term = 0
        self.current_floor_term = 20
        # 각각의 엘리베이터들마다 상황을 비교한다
        # for i in range(0,4):
        for index in range(0, 4):  # constant.MAX_ELEVATORS
            # while(index < 4):
            # 같은층인데 idle
            if (int(self.elevator_rack[index].floor) == call.departure and self.elevator_rack[index].state == constant.IDLE_STATE):
                print("AAAAA")
                close_ele = index
            # 같은층은 아닌데 idle
            elif (self.elevator_rack[index].state == constant.IDLE_STATE):
                close_ele = index
            elif (int(self.elevator_rack[index].floor) < call.destination and (call.isup) == 1):  # 1이 up, 0이 down
                # 층 차이
                floor_term = abs(int(call.departure) - int(self.elevator_rack[index].floor))

                if (floor_term < self.current_floor_term):
                    self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.
            # 내 콜이 내려가는콜이고 , 내위치보다 엘레베이터가 위에 있을 때
            elif (call.destination < int(self.elevator_rack[index].floor) and (call.isup) == 0):
                # 층차이

                floor_term = abs(int(self.elevator_rack[index].floor) - int(call.departure))

                if (floor_term < self.current_floor_term):  # 제일 짧은 층 차이보다 더 층 차이가 짧을 때
                    self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.
            else:
                if (floor_term < self.current_floor_term):  # 제일 짧은 층 차이보다 더 층 차이가 짧을 때
                    self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = random.randrange(0, 4)  # 할당하는 엘레베이터 번호를 바꾼다.

        return close_ele

    def allocate(self, call):
        # 엘레베이터들의 위치를 가진다

        close_ele = 0  # 가장 가까운 엘레베이터 번호

        # 각각의 엘리베이터들마다 상황을 비교한다

        for index in range(0, constant.MAX_ELEVATORS):
            if (self.elevator_rack[index].floor == call.departure):

                close_ele = index
                self.elevator_rack[index].state = constant.LOAD_STATE  # 이거 다시 해야됨 아무튼 태운다는 뜻입니다
            # 엘베 위치가 나의 출발층보다 아래이고  call이 위로 올라가는 콜이면 할당리스트에 넣겠다.
            elif (int(self.elevator_rack[index].floor) < int(call.departure) and self.elevator_rack[
                index].direction == constant.UP_DIRECTION and call.isup == 1):  # 1이 up, 0이 down
                # 층 차이
                floor_term = int(call.departure) - int(self.elevator_rack[index].floor)
                print('floorterm2 : ', floor_term)
                if (floor_term < self.current_floor_term):
                    self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.

            # 내 콜이 내려가는콜이고 , 내위치보다 엘레베이터가 위에 있을 때
            elif (int(self.elevator_rack[index].floor) > int(call.departure) and self.elevator_rack[
                index].direction == constant.DOWN_DIRECTION and call.isup == 0):
                # 층차이
                floor_term = int(self.elevator_rack[index].floor) - int(call.departure)
                print('floorterm 3: ', floor_term)
                if (floor_term < self.current_floor_term):  # 제일 짧은 층 차이보다 더 층 차이가 짧을 때
                    self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.
            elif (self.elevator_rack[index].state == constant.IDLE_STATE):
                floor_term = abs(int(self.elevator_rack[index].floor) - int(call.departure))
                print('floorterm 4: ', floor_term)
                if (floor_term < self.current_floor_term):  # 제일 짧은 층 차이보다 더 층 차이가 짧을 때
                    self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.
            else:
                floor_term = abs(int(self.elevator_rack[index].floor) - int(call.departure))

                print('floorterm :: when else: ', floor_term)
                print('current_floor_term', self.current_floor_term)

                # self.current_floor_term = floor_term  # 층 차이를 업데이트한다

                if (floor_term < self.current_floor_term):  # 제일 짧은 층 차이보다 더 층 차이가 짧을 때
                    self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.
                    print('index : ', index)

            print('readcalls.py : allocated elevator  :', close_ele)

        return close_ele
