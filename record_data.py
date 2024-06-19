from camera.camera import Cam
from data_storing.store_data import StoreData
from data_recording.record import Record
import time

r = Record(index=[1])

while True:
       r.record_data()
       time.sleep(0.5)
