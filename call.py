# -*- coding:cp949 -*-
# -*- coding: utf-8 -*-
import constant
class Call(object):

    # call ��ü�� destinamtion departure state(upcall downcall)�� ���� �������ش�(Ű���� �ð����̴�. - �ش� ���� ������ ������ ����) - �̰� �Ƹ� �� Ŭ�������� �ҵ�
    def __init__(self, register_time, departure_floor,destination_floor, isup, passenger):
        # self.call_id = id
        self.register_time = register_time
        self.departure = departure_floor
        self.destination = destination_floor
        self.isup =  isup  # true
        self.passengers = passenger
        self.duration = 0 # ����Ǵ� �ʸ� ��� ��



    def record_time(self):
        self.duration += 3


