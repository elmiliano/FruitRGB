import socket 


HOST = '10.12.56.46'
PORT = 5001
BUFFER_SIZE = 1024


class Server:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.buffer = BUFFER_SIZE
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host,self.port))
        self.conn = None
        self.addr = None
        self.messages = []

    def up(self):
        self.server.listen(100)
        print('Server up')
    

    def connect(self):
        self.conn, self.addr = self.server.accept()
        print('Connected to: self.addr')
        


    
    def clientthread(self):
            while True:
                try:
                    message = self.conn.recv(self.buffer)
                    if message:
                        print(message)
                        message = str(message).split(',')
                        self.messages.append(message) 
                    else:
                        break
                except:
                    continue

    def handlebyte(self):
        for i in range(len(self.messages)):
            self.messages[i] = str(self.messages[i].decode('UTF-8'))
            self.messages[i] = self.messages[i][:-1]


if __name__ == '__main__':
    server = Server()
    server.up()
    while True:
        server.connect()
        server.clientthread()
        server.messages[-1]




