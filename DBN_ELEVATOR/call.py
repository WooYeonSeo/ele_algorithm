# -*- coding:cp949 -*-
# -*- coding: utf-8 -*-
import constant
class Call(object):

    # call ��ü�� destinamtion departure state(upcall downcall)�� ���� �������ش�(Ű���� �ð����̴�. - �ش� ���� ������ ������ ����) - �̰� �Ƹ� �� Ŭ�������� �ҵ�
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
        self.duration = 0 # ����Ǵ� �ʸ� ��� ��

        self.regist_sec =0
        self.getin_sec = 0
        self.getout_sec = 0 # Ÿ�� �����ؼ� ������ �ð�����

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


