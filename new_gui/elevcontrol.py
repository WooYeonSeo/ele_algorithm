# -*- coding: utf-8 -*-
import threading
import simulator
import ThreadEli2
import dataParsing as gdata
import constant
import math
import random
import elevator
import time
import call as c


# http://saelly.tistory.com/510
class Elevcontrol(threading.Thread):
    def __init__(self, parent=None):
        threading.Thread.__init__(self)
        self.call_number = 0
        self.current_floor_term = 20  # 층 차이값일단 최대로 줌
        self.threadFlag = [0] * 4

        print("__elevsim__ \n")
        self.current_floor_term = 20
        # self.ui = simulator.ui.getUI()
        # self.ui = ui  # simulator.Ui_MainWindow()

        # self.dialog = dialog # 다이얼로그 받아온다
        self.index = 0
        self.tn = 0  # 가지고 올 데이터의 우치
        self.elevator_rack = []  # 엘레베이터 호기

        self.elevator_calls = []  # 엘리베이터 콜들
        self.last_floor = []  # 마지막 층 : 최근층

        self.floor_passengers = []  # 엘베 승객수

        for index in range(0, constant.MAX_ELEVATORS):  # 메인에서 max elevators - 4 정의
            self.elevator_rack.append(None)  # null값 넣어야 됨, elevator_rack -
            self.last_floor.append(constant.TOP_FLOOR)

        for index in range(0, constant.MAX_FLOORS):
            self.floor_passengers.append(0)

            # initialize at something other than zero - 0 말고 다른 것으로 초기화 하시오
            self.last_max_flow_rate = 1  # 일단 1으로 넣어놓음 - 어차피 나중에 max_flow_rate로 치환된다.
            self.last_min_flow_rate = 1

            # initialize rtfgjtt6\]
            # the rest
            self.min_flow_rate = 0
            self.max_flow_rate = 0
            self.total_passengers = 0
            self.min_duration = 0
            self.max_duration = 0
    def setdata(self, data):
        self.data = data

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
        for index in range(0, constant.MAX_ELEVATORS):
            # print(self.elevator_rack[index])
            if (index < constant.MAX_ELEVATORS):  # 엘베 갯수 받은 것 보다 작은 인덱스만큼 돌려준다.
                self.elevator_rack[index] = elevator.Elevator(index + 1)  # 1번 엘베 2번엘베 3번엘베 4번엘베

            else:
                self.elevator_rack[index] = None  # 나머지는 걍 null


        self.tn += 1  # 다음 투플로 넘긴다음에 와일문 돌리기
        t1 = ThreadEli2.ElavatorThread1()
        # t1.setDaemon(True)
        t1.setUI(self.ui)
        t1.setDasom(self.tn)
        t1.setDialog(self.dialog)
        t1.setElevator_rack(self.elevator_rack[0])

        t2 = ThreadEli2.ElavatorThread2()
        # t2.setDaemon(True)
        t2.setUI(self.ui)
        t2.setDasom(self.tn)
        t2.setDialog(self.dialog)
        t2.setElevator_rack(self.elevator_rack[1])

        t3 = ThreadEli2.ElavatorThread3()
        # t3.setDaemon(True)
        t3.setUI(self.ui)
        t3.setDasom(self.tn)
        t3.setDialog(self.dialog)
        t3.setElevator_rack(self.elevator_rack[2])

        t4 = ThreadEli2.ElavatorThread4()
        # t4.setDaemon(True)
        t4.setUI(self.ui)
        t4.setDasom(self.tn)
        t4.setDialog(self.dialog)
        t4.setElevator_rack(self.elevator_rack[3])

        ch = ThreadEli2.check()

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        ch.start()

        while (self.tn < 10000):
            if self.tn < 10000:
                # dataSplit = gdata.dataSet[self.tn][0].split('.')
                registertime = gdata.getData(self.tn)  # gdata.datetime.datetime.strptime(dataSplit[0],"%Y-%m-%d %H:%M:%S")
                # self.t2._stop.set()

                if self.dialog.timer[2] == registertime.second and self.dialog.timer[1] == registertime.minute and \
                                self.dialog.timer[0] == registertime.hour:
                    call = self.getcall(self.tn)  # 시간 같으면 콜을 발생시킨다.
                    allocated_elevator = self.allocate3(call)
                    allocated_elevator = int(allocated_elevator)

                    print("getcall!!!  + allocated elevator num : ", allocated_elevator)

                    # flag가 1로 스탑이라는데 할당된 엘리베이터가 0번 이면(새 콜이 들어왔다는 거) 다시 플래그를 운행중인 0 으로 바꾸어준다
                    # if( self.threadFlag ==1 and allocated_elevator == 0 ): # 정지상태가 아닌
                    #    self.threadFlag = 0
                    print('EL1 CALLNUM ', len(self.elevator_rack[0].ready_calls))
                    print('EL2 CALLNUM ', len(self.elevator_rack[1].ready_calls))
                    print('EL3 CALLNUM ', len(self.elevator_rack[2].ready_calls))
                    print('EL4 CALLNUM ', len(self.elevator_rack[3].ready_calls))

                    # 할당받은 엘리베이터의 배열에 넣겠다
                    self.elevator_rack[allocated_elevator].ready_calls.append(call)
                    self.tn += 1

                    if (allocated_elevator == 0):
                        print('EL1 할당되서 변수 바꿈 ', len(self.elevator_rack[0].ready_calls))
                        self.t1._stop.set()
                        # self.t2._stop.set()
                    if (allocated_elevator == 1):
                        print('EL2 할당되서 변수 바꿈 ', len(self.elevator_rack[1].ready_calls))
                        self.t2._stop.set()
                    if (allocated_elevator == 2):
                        print('EL3 할당되서 변수 바꿈 ', len(self.elevator_rack[2].ready_calls))
                        self.t3._stop.set()
                    if (allocated_elevator == 3):
                        print('EL4 할당되서 변수 바꿈 ', len(self.elevator_rack[3].ready_calls))
                        self.t4._stop.set()

                time.sleep(0.1)

            # self.tn이 100번째가 넘어가면 나간다 와일문
            else:
                break

    def getcall(self, tn):  # ui객체를 받아와야 된다
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

        new_call = c.Call(registertime, departure_floor, destination_floor, is_up, passenger, dbn_register_time,
                          day_of_week, iserror, weekend, register15min)  # 1이 up, 0이 down

        self.elevator_calls.append(new_call)
        print('departure_floor : ', new_call.departure, ' --> ', new_call.destination)
        self.elevator_calls.append(new_call)  # 나중에 waitingtime 계산할때 쓸라고 배열에 담아놓는다.

        # print( self.elevator_calls[0].departure + ' ::: departure')

        return new_call

    # allocate for one by one
    def allocate3(self, call):
        floor_term = 0
        self.current_floor_term = 20

        self.idle_term = 17
        keep = []
        close_ele = 0  # 가장 가까운 엘레베이터 번호

        # 각각의 엘리베이터들마다 상황을 비교한다
        for index in range(0, 4):  # constant.MAX_ELEVATORS

            # 층 차이값일단 최대로 줌
            if (self.elevator_rack[index].state == constant.IDLE_STATE and len(
                    self.elevator_rack[index].ready_calls) == 0):
                # 처음이든 아니든 모두 층 차이를 계산하고 idleterm 보다 작으면 가장가까운 엘베로 해서 리턴한다
                floor_term = abs(int(self.elevator_rack[index].floor) - int(call.departure))
                if floor_term < self.idle_term:
                    self.idle_term = floor_term
                    close_ele = index
                    # return close_ele

            else:  # idle이 아니면
                if (call.destination < int(self.elevator_rack[index].floor) and (call.isup) == 0):
                    # 층차이
                    floor_term = abs(int(self.elevator_rack[index].floor) - int(call.departure))
                    if (floor_term < self.current_floor_term):  # 제일 짧은 층 차이보다 더 층 차이가 짧을 때
                        self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                        close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.

                if (int(self.elevator_rack[index].floor) < call.destination and (call.isup) == 1):  # 1이 up, 0이 down
                    # 층 차이
                    floor_term = abs(int(call.departure) - int(self.elevator_rack[index].floor))

                    if (floor_term < self.current_floor_term):
                        self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                        close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.
                else:
                    if (floor_term < self.current_floor_term):  # 제일 짧은 층 차이보다 더 층 차이가 짧을 때
                        self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                        close_ele = random.randrange(0, 4)  # 할당하는 엘레베이터 번호를 바꾼다.

        return close_ele
