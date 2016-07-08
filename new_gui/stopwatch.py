
import threading
import main
import time

class StopWatch(threading.Thread):
    def __init__(self, dialog, parent = None):
        threading.Thread.__init__(self)
        self.dialog = dialog



    def run(self):
        while(1):

            self.dialog.update_timeText()

            time.sleep(1)