from camera.camera import Cam
from data_storing.store_data import StoreData
import serial

class Record:
    def __init__(self, index = [0]):
        self.cams_used = len(index)
        self.c = Cam(index=index)
        self.s = StoreData()
        self.ser = serial.Serial(
        port='COM7',
        baudrate = 9600)


    def getPotValue(self):
        self.ser.reset_input_buffer()
        return self.ser.readline().decode().rstrip()
    
    def record_data(self):
        if self.cams_used == 2:
            frame = self.c.combine_images(self.c.prepare_image(self.c.get_frame(0)), self.c.prepare_image(self.c.get_frame(1)))
        if self.cams_used == 1:
            frame = self.c.get_frame()
            #frame = self.c.prepare_image(frame)
        
        # Pot is irrelevant at this time
        pot = 10
        print(pot)
        self.s.store_automatic(frame, pot, "database")
