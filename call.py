# -*- coding:cp949 -*-
# -*- coding: utf-8 -*-
import constant
class Call(object):

    # call 객체에 destinamtion departure state(upcall downcall)의 값을 지정해준다(키값은 시간값이다. - 해당 투플 라인을 값으로 전달) - 이건 아마 콜 클래스에서 할듯
    def __init__(self, register_time, departure_floor,destination_floor, isup, passenger):
        # self.call_id = id
        self.register_time = register_time
        self.departure = departure_floor
        self.destination = destination_floor
        self.isup =  isup  # true
        self.passengers = passenger
        self.duration = 0 # 운행되는 초를 담는 곳



    def record_time(self):
        self.duration += 3


