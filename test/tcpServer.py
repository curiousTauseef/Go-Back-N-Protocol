import socket
import threading
import sys 

args = sys.argv 

def receive(name, sock):
    print ("In Receive")
    while True:
        data = sock.recv(1024)     #Buffer we want to receive is max of 1024 bytes 
        if not data:
            break
        print "from connected user: " + str(data)
    sock.close()

def send(name, sock):
    print ("In Send")
    while True:
        data = raw_input("-> ")
        print "sending: " + str(data)
        sock.send(data)
    sock.close()


def Main(mode=0):
    host = '127.0.0.1'
    port = 5001

    s = socket.socket()
    print(mode)
    if mode == 0:
        s.bind((host,port))
        s.listen(1) 
        c, addr = s.accept()
        print "Connection from: " + str(addr)
    

    else : 
        s.connect((host, port))
        c = s

    t_rec = threading.Thread(target=receive, args=("RetThread", c))
    t_send = threading.Thread(target=send, args=("SendThread", c))
    
    t_rec.start()
    t_send.start()


    

if __name__ == '__main__':
    Main(int(args[1]))