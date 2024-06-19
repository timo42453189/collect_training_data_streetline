import camera

c = camera.Cam(index = [0, 1])

frame0 = c.get_frame(0)
frame0 = c.prepare_image(frame0)
frame1 = c.get_frame(1)
frame1 = c.prepare_image(frame1)
frame = c.combine_images(frame0, frame1)
c.show_image(frame)