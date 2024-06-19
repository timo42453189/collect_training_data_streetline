import h5py
import os
#import cv2
class StoreData:

    def __init__(self):
        pass

    def store_manual(self, image, potentiometer, filename):
        with h5py.File(f"{os.getcwd()}/data_storing/database/{filename}", 'w') as f:
            f.create_dataset('image', data=image)
            f.create_dataset('potentiometer', data=potentiometer)
    
    def store_automatic(self, image, potentiometer, directory):
        filename = str(len(os.listdir(f"{os.getcwd()}/data_storing/{directory}")) + 1)
        with h5py.File(f"{os.getcwd()}/data_storing/{directory}/{filename}.h5", 'w') as f:
            f.create_dataset('image', data=image)
            f.create_dataset('potentiometer', data=potentiometer)
            
    def read(self, filename):
        with h5py.File(f"{os.getcwd()}/data_storing/database/{filename}", 'r') as f:
            return f['image'][()], f['potentiometer'][()]
        
    def read2(self, filename):
        with h5py.File(f"{os.getcwd()}/data_storing/train_images_2/{filename}", 'r') as f:
            return f['image'][()], f['potentiometer'][()]
        