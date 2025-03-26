import pymavlink.mavutil as utility
import time 

vehicle = utility.mavlink_connection(device='udpin:127.0.0.1:14550', udp_timeout=5)

if vehicle.wait_heartbeat():
    print("Connecteed to vehicle")
    print("System ID: ", vehicle.target_system, "Component ID: ", vehicle.target_component)

while True:
    try:
        message = vehicle.recv_match(blocking=True)
        # if message != None:
        time.sleep(2)
        print (message)

    except ConnectionError as e:
        print(f"Connection lost: {e}")
    
    except TimeoutError:
        print("Timeout while waiting for a response. The drone may be offline.")
    
    except Exception as e:
        print(f"Unexpected error: {e}")