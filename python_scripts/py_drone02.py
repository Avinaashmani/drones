import dronekit
import time

vehicle = dronekit.connect (ip='127.0.0.1:14550', wait_ready=True)

print ("Connected to vehicle")

time.sleep(1)

print(vehicle.location.global_relative_frame.alt)

time.sleep (3)
vehicle.send_calibrate_barometer()
print ("Calibrated barrometer") 
print(vehicle.location.global_relative_frame.alt)


