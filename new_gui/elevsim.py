# -*- coding: utf-8 -*-



# import elevsupp
# import display
# import sys
# sys.path.append("C:\Users\DS\PycharmProjects\untitled2\elevator_algorithm")
# import elevsim

import ThreadEli2
import call as c
import constant
import dataParsing as gdata
import elevator
import readcalls
import simulator


class Elevsim(object):
    def __init__(self, dialog):

        print("__elevsim__ \n")
        self.current_floor_term = 20
        # self.ui = simulator.ui.getUI()
        #self.ui = ui  # simulator.Ui_MainWindow()
        self.dialog = dialog # 다이얼로그 받아온다
        self.index = 0
        self.tn = 0 # 가지고 올 데이터의 우치
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

    # 이건 시뮬에서 불러진다. - 엘베심에서 init다음으로 제일 먼저 실행됨
    def run(self,data, ui):
        #self.ui.toggle()
        self.ui = ui
        # 1. 엘레베이터 먼저 생성하겠음
        for index in range(0, constant.MAX_ELEVATORS):
            # print(self.elevator_rack[index])
            if (index < constant.MAX_ELEVATORS):  # 엘베 갯수 받은 것 보다 작은 인덱스만큼 돌려준다.
                self.elevator_rack[index] = elevator.Elevator(index + 1)  # 1번 엘베 2번엘베 3번엘베 4번엘베

            else:
                self.elevator_rack[index] = None  # 나머지는 걍 null

        # 2. 처음에 가지고 온 시간을 콜 할당. 입력한 시간에 해당하는 투플 숫자를 가지고 온다
        self.tn = data #data.generateData(self.ui)
        registertime = gdata.getData(self.tn)
        # 해당 투플 (= 콜) 생성시 들어가는 데이터를 읽어온다 - 보기 좋으라고 이렇게 해놈
        departure_floor = gdata.dataSet[self.tn][2]
        destination_floor = gdata.dataSet[self.tn][3]
        # iserroroccured = gdata.dataSet[tn][13]
        is_up = gdata.dataSet[self.tn][4]
        passenger = 3  # 일단은 세명이라고 했음

        # 데이터 추가
        dbn_register_time = gdata.dataSet[self.tn][1] # 수정
        day_of_week = gdata.dataSet[self.tn][5]
        iserror = gdata.dataSet[self.tn][6]
        weekend = gdata.dataSet[self.tn][7] # 수정
        register15min = gdata.dataSet[self.tn][8]

        # call생성
        # registertime,departurefloor,destinationfloor,el_idatfield,waitingtime,ridingtime,servicetime,6
        # registertime_year,registertime_quarter,registertime_month,registertime_day,registertime_hour,registertime_dayofweek, 12
        # iserroroccured,isup,registertime_30min,registertime_15min,registertime_5min 17

        # register_time, departure_floor,destination_floor, isup, passenger, dbn_register_time, day_of_week, iserror, weekend, register15min):
        first_call = c.Call(registertime, departure_floor, destination_floor, is_up, passenger, dbn_register_time,day_of_week,iserror,weekend, register15min)  # 1이 up, 0이 down

        # 나중에 웨이팅 구할때 사용 배열에 담는다
        self.elevator_calls.append(first_call)
        # 어느 엘리베이터에 할당할지를 고른다

        allocated_elevator = int(self.allocate2(first_call))
        # 할당 될 엘리베이터에 첫 콜을 레디리스트에 추가해 준다.
        self.elevator_rack[allocated_elevator].ready_calls.append(first_call)

        # 3. 시간이 같을 때마다 콜을 발생시켜야 된다.

        # 가정 : 시간순으로 데이터가 정렬되어있다, 시간이 지나기 전에검색 할 수 있다.
        # 해당 투플 다음 한줄씩 읽는다
        # 스레드 실행



        t1 = ThreadEli2.ElavatorThread1()
        #t1.setDaemon(True)
        t1.setUI(self.ui)
        t1.setDasom(self.tn)
        t1.setDialog(self.dialog)
        t1.setElevator_rack(self.elevator_rack[0])

        t2 = ThreadEli2.ElavatorThread2()
        #t2.setDaemon(True)
        t2.setUI(self.ui)
        t2.setDasom(self.tn)
        t2.setDialog(self.dialog)
        t2.setElevator_rack(self.elevator_rack[1])

        t3 = ThreadEli2.ElavatorThread3()
        #t3.setDaemon(True)
        t3.setUI(self.ui)
        t3.setDasom(self.tn)
        t3.setDialog(self.dialog)
        t3.setElevator_rack(self.elevator_rack[2])

        t4 = ThreadEli2.ElavatorThread4()
        #t4.setDaemon(True)
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

        readcall = readcalls.Readcalls()
        readcall.setUI(self.ui)
        readcall.setDialog(self.dialog)
        readcall.settn(self.tn)
        readcall.setcalllist(self.elevator_calls)
        readcall.setElevator_rack(self.elevator_rack,t1,t2,t3,t4)
        readcall.start()











        # #eleThread1 = ElavatorThread1()
        # eleThread1.start()

    def getcall(self, tn):  # ui객체를 받아와야 된다
        # index = 0
        # 데이터의 시간을 가지고와서 배열에 넣어 놓는다,- 아무튼 시간을 가지고 온다는 뜻

        # tn = 투플넘버를가지고 옵시다 - dataparsing에 접근
        registertime = gdata.getData(tn)
        # 해당 투플 (= 콜) 생성시 들어가는 데이터를 읽어온다 - 보기 좋으라고 이렇게 해놈
        departure_floor = gdata.dataSet[tn][2]
        destination_floor = gdata.dataSet[tn][3]
        # iserroroccured = gdata.dataSet[tn][13]
        is_up = gdata.dataSet[tn][4]
        passenger = 3  # 일단은 세명이라고 했음

        # 데이터 추가
        dbn_register_time = gdata.dataSet[tn][1] # 수정
        day_of_week = gdata.dataSet[tn][5]
        iserror = gdata.dataSet[tn][6]
        weekend = gdata.dataSet[tn][7] # 수정
        register15min = gdata.dataSet[tn][8]

        # call생성
        # registertime,departurefloor,destinationfloor,el_idatfield,waitingtime,ridingtime,servicetime,6
        # registertime_year,registertime_quarter,registertime_month,registertime_day,registertime_hour,registertime_dayofweek, 12
        # iserroroccured,isup,registertime_30min,registertime_15min,registertime_5min 17

        # register_time, departure_floor,destination_floor, isup, passenger, dbn_register_time, day_of_week, iserror, weekend, register15min):
        new_call = c.Call(registertime, departure_floor, destination_floor, is_up, passenger, dbn_register_time,day_of_week,iserror,weekend, register15min)  # 1이 up, 0이 down
        #new_call = c.Call(registertime, departure_floor, destination_floor, is_up, passenger)  # 1이 up, 0이 down
        self.elevator_calls.append(new_call)
        print('departure_floor : ',new_call.departure )
        self.elevator_calls.append(new_call)  # 나중에 waitingtime 계산할때 쓸라고 배열에 담아놓는다.


        return new_call


    # allocate for one by one
    def allocate2(self, call):
        # 엘레베이터들의 위치를 가진다

        close_ele = 0  # 가장 가까운 엘레베이터 번호
          # 층 차이값일단 최대로 줌

        # 각각의 엘리베이터들마다 상황을 비교한다

        for index in range(0, constant.MAX_ELEVATORS):
            if (int(self.elevator_rack[index].floor) == call.departure):
                print('check1   :', close_ele)
                close_ele = index
                # self.elevator_rack[index].state = constant.LOAD_STATE  # 이거 다시 해야됨 아무튼 태운다는 뜻입니다
            # 엘베 위치가 나의 출발층보다 아래이고  call이 위로 올라가는 콜이면 할당리스트에 넣겠다.
            elif (int(self.elevator_rack[index].floor) < call.departure and int(call.isup) == 1):  # 1이 up, 0이 down
                # 층 차이
                print('check2   :', close_ele)
                floor_term = int(call.departure) - int(self.elevator_rack[index].floor)
                if (floor_term < self.current_floor_term):
                    self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.
            # 내 콜이 내려가는콜이고 , 내위치보다 엘레베이터가 위에 있을 때
            elif (call.departure < int(self.elevator_rack[index].floor) and int(call.isup) == 0):
                # 층차이
                print('check3   :', close_ele)
                floor_term = int(self.elevator_rack[index].floor) - int(call.departure)
                if (floor_term < self.current_floor_term):  # 제일 짧은 층 차이보다 더 층 차이가 짧을 때
                    self.current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.

        print('closest elevator  :', close_ele)
        return close_ele






    def allocate(self, call):
        close_ele = 0  # 가장 가까운 엘레베이터 번호

        for index in range(0, constant.MAX_ELEVATORS):
            if (self.elevator_rack[index].floor == call.departure):
                close_ele = index
                # self.elevator_rack[index].state = constant.LOAD_STATE  # 이거 다시 해야됨 아무튼 태운다는 뜻입니다
            # 엘베 위치가 나의 출발층보다 아래이고  call이 위로 올라가는 콜이면 할당리스트에 넣겠다.
            elif (self.elevator_rack[index].floor < call.departure and call == 1):  # 1이 up, 0이 down
                # 층 차이

                floor_term = call.departure - self.elevator_rack[index].floor
                if (floor_term < self.current_floor_term):
                    current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.
            # 내 콜이 내려가는콜이고 , 내위치보다 엘레베이터가 위에 있을 때
            elif (call.departure < self.elevator_rack[index].floor and call == 0):
                # 층차이
                floor_term = self.elevator_rack[index].floor - call.departure
                if (floor_term < self.current_floor_term):  # 제일 짧은 층 차이보다 더 층 차이가 짧을 때
                    current_floor_term = floor_term  # 층 차이를 업데이트한다
                    close_ele = index  # 할당하는 엘레베이터 번호를 바꾼다.

            print('closest elevator  :', close_ele)
            return close_ele











            # 각 엘베처럼
            # 내가 올라가는 방향의 콜일 때.
            # 엘베위치가 해당 콜의 위치보다 아래라면 , 그 엘베를 할당 후보군(리스트)에 포함시킨다.
            # 내가 내려가는 방향의 콜일 때.
            # 엘베위치가 해당 콜의 위치보다 위라면 , 그 엘베를 할당 후보군(리스트)에 포함시킨다.

            # 콜의 위치보다 아래라면

    """
    def run(self):
        #1.  엘레베이터를 생성한다 - 4
        for index in range(0, constant.MAX_ELEVATORS):
            # print(self.elevator_rack[index])
            if(index<constant.MAX_ELEVATORS): # 엘베 갯수 받은 것 보다 작은 인덱스만큼 돌려준다.
                self.elevator_rack[index] = elevator.Elevator(index+1) # 1번 엘베 2번엘베 3번엘베 4번엘베
            else:
                self.elevator_rack[index] = None # 나머지는 걍 null



        # getcall함수로 콜이 발생하는지 계속 체크한다


        # simulator ui 를 이런식으로 전달해도 되는지
        call = self.getcall(ui = self.ui, tn = 1)
        # 콜이 발생했다고 치고 이게 이제 할당되야 된다
        self.allocate(call)
    """
