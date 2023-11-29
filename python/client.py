from serial import Serial
from time import sleep
import socket

#PORT DEFINITION
stm32_port = Serial('/dev/cu.usbmodem1103', 115200, timeout=100)

#SERVER DEFINITION
host = "10.12.56.46"
server_port = 5001

grade = "not great"
message = []

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# while True:
#     test = int(input(">> "))
#     print(test)
#     if test == 1:
#         try:
#             stm32_port.write(grade.encode()) # send to stm32
#             print("sent: "+grade)
#         finally:
#             pass
#         test = 0

while True:
    try:
        # s.connect((host, server_port)) # connect to server
        # stm32_port.write(grade.encode()) # send to stm32
        # print(grade)

        if stm32_port.in_waiting > 0: # wait for message from stm32
            sleep(2)
            stm32_port.write(grade.encode()) # send to stm32
            print(grade)
            break
        #     data = stm32_port.read_until()
        #     data = data.decode("utf-8")
        #     print(data)
        #     sleep(1)
        #     # s.sendall(message) # send to server
        # else:
        #     # try:
        #     #     #grade = s.recv(1024).decode() # receive grade from server
        #         stm32_port.write(grade.encode()) # send to stm32
        #         print(grade)
        #     # finally:
        #         sleep(1)
            # pass
    finally:
        pass

    # if stm32_port.in_waiting > 0:
    #     data = stm32_port.read_until()
    #     data = data.decode("utf-8")
        
    #     if count < 10:
    #         try:
    #             s.connect((host, server_port))
    #             # message.append(data)
    #             print(data)
    #             s.sendall(data)
    #             # sleep(3)
    #         finally:
    #             # s.close()
    #             # sleep(1)
    #             pass

    #         count = count + 1
    #     else:
    #         sleep(1)
    #         # try:
    #         #     print(message)
    #         #     s.sendall(message)
    #         # finally:
    #         #     sleep(1)

