# -*- coding:cp949 -*-
# -*- coding: utf-8 -*-
import constant
class Call(object):

    # call 객체에 destinamtion departure state(upcall downcall)의 값을 지정해준다(키값은 시간값이다. - 해당 투플 라인을 값으로 전달) - 이건 아마 콜 클래스에서 할듯
    def __init__(self, register_time, departure_floor,destination_floor, isup, passenger, dbn_register_time, day_of_week, iserror, weekend, register15min):
        #registertime,departurefloor,destinationfloor,el_idatfield,waitingtime,ridingtime,servicetime,registertime_year,
        # registertime_quarter,registertime_month,registertime_day,registertime_hour,registertime_dayofweek,iserroroccured,
        # isup,registertime_30min,registertime_15min,registertime_5min

        # self.call_id = id
        self.register_time = register_time

        self.departure = departure_floor
        self.destination = destination_floor
        self.isup =  isup  # true
        self.passengers = passenger
        self.duration = 0 # 운행되는 초를 담는 곳

        self.regist_sec =0
        self.getin_sec = 0
        self.getout_sec = 0 # 타고 도착해서 내리는 시간까지

        self.waiting = 0


        self.dbn_register_time = dbn_register_time
        self.day_of_week = day_of_week
        self.iserror = iserror
        self.weekend =weekend
        self.register_time_15min =register15min



        self.flag = 0




    def record_time(self):
        self.duration += 3

    def setwaiting(self,regist ,getin):
        self.waiting = regist - getin
        self.regist_sec = regist
        self.getin_sec = getin


