import dronekit
import time

vehicle = dronekit.connect (ip='127.0.0.1:14550', wait_ready=True)

print ("Vehicle is ready")
vehicle.parameters ['ARMING_CHECK'] = 1
while not vehicle.is_armable:
    print ("Drone is not armable")
    print (vehicle.is_armable)

while not vehicle.armed:
    vehicle.armed = True
    time.sleep(2)
print (vehicle.armed)


