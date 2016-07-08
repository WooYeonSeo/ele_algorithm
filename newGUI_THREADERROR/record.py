

class Record():

    #def __init__(self, parent = None):
       #self.f = open("/Users/vantovan/Projects/elev_pro/newGUI_THREADERRORC/record.txt", 'w')


    def record(self, elevator_rack ):
        f = open("record-data.txt", 'a')
        lent = len(elevator_rack.record_calls)

        if(lent !=0):
            for i in range(0,lent):
                record =elevator_rack.record_calls.pop()
                data = ""
                data += 'Elevator'+str(elevator_rack.elevator_id)+","+ str(record.register_time) + "," + str(record.departure)+ ","+ str(record.destination)+ ","+ str(record.isup)+","+ str(record.passengers) +","+ str(record.waiting)+ ","+str(record.riding)+ "\n"
                f.write(data)


        f.close()



