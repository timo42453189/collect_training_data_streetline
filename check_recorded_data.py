from camera.camera import Cam
from data_storing.store_data import StoreData
import cv2 

s = StoreData()
c = Cam(index=[])


image_name = "8.h5"

image, _ = s.read(image_name)
median_blur = cv2.medianBlur(image, 5)
downsampled = cv2.resize(median_blur, (image.shape[1] // 2, image.shape[0] // 2), interpolation=cv2.INTER_LINEAR)
original_image = downsampled[110:190, :]
c.show_image(original_image)