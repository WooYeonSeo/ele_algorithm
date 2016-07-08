
# -*- coding: utf-8 -*-
class Getui(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Getui, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print("__getui__ \n")

        pass
    def setui(self, ui):
        self.ui = ui

    def goup(self,index):
        self.ui.up(index)

    def godown(self,index):
        self.ui.down(index)

