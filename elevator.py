# -*- coding: utf-8 -*-


import constant
#import poisson
#import passnger as passenger
import dataParsing as data


class Elevator:
    def __init__(self, id):
        self.elevator_id = id
        self.ele_pass = [] # 승객수
        self.pass_on_floor = [] # 층의 승객수?

        self.ready_calls = []
        self.destination_list =[]
        self.destination = 0


        self.total_passenger_count = 0
        self.passengers_on_board = 0
        self.total_duration =0

        self.floor = constant.LOBBY_FLOOR
        self.direction = constant.NO_DIRECTION # up, down, stop
        self.state = constant.IDLE_STATE

        print(constant.MAX_FLOORS -1)

        #self.poisson1 = poisson.Poisson()
        #poisson.Poisson.put_interval(self.poisson1, constant.MAX_FLOORS-1)#

        self.total_dyratuib =0.0

        for idx1 in range(0,constant.MAX_FLOORS):
            self.pass_on_floor.append(0)



    def run(self):
        #self.calls.pop(1)
        self.total_dyratuib =0.0
            ######
            ## 스탑워치시간이 변하면.. 데이터를 하나 읽는다. 만약에 호수 가 맞고 시간이 맞으면 움직인다.
            ## 스탑워치 시간을 가져온다 레지스터타임과 엘베번호를 비교

            # (엘베번호, 시간)
            # (o,o) - 일 시키고 dasom +=1
            # (o,x) - dasom 그대로
            # (x,o) - dasom +=1
            # (x,x) - dasom +=1





    def current_duration(self):
        return self.total_duration


    def passenger_flow_rate(self):
        self.flow = 0
        hours = self.total_duration / (60.0*60.0)
        if hours > 0.0:
            self.flow = self.total_passenger_count/hours
        else:
            self.flow = 0.0

        return self.flow

    def current_total_passenger_count(self):
        return self.total_passenger_count

    def current_passengers_on_board(self):
        return self.passengers_on_board

    def current_floor(self):
        return self.floor
    def durrent_direction(self):
        return self.direction

    def current_state(self):
        return self.state

    def current_id(self):
        return self.elevator_id

    def pass_on_floor_array(self):#여기 약간 주의
        return self.pass_on_floor















