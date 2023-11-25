from serial import Serial
from time import sleep
import socket

#PORT DEFINITION
stm32_port = Serial('/dev/cu.usbmodem1103', 115200, timeout=1)
host = "10.12.56.46"
server_port = 5001

count = 0
message = []

while True:

    if stm32_port.in_waiting > 0:
        data = stm32_port.read_until()
        data = data.decode("utf-8")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if count < 10:
            try:
                s.connect((host, server_port))
                # message.append(data)
                print(data)
                s.sendall(data)
                # sleep(3)
            finally:
                # s.close()
                # sleep(1)
                pass

            count = count + 1
        else:
            sleep(1)
            # try:
            #     print(message)
            #     s.sendall(message)
            # finally:
            #     sleep(1)

