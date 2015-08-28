#version python3
__author__ = 'ahmet'

from socket import *
import _thread
import sys

portSend = 13001
portRec = 13000
ipSend = "127.0.0.1"

codec = {'ç':"__c__",'ğ':"__g__",'ü':"__u__",'ö':"__o__",'ı':"__i__",'ş': '__s__','Ç':"__C__",'Ğ':"__G__",'Ü':"__U__",'Ö':"__O__",'İ':"__I__",'Ş':"__S__    ",};
isCodec = True

def encode(kelime,dict):
    for k in dict.keys():
        kelime=kelime.replace(k,dict[k])
    return kelime

def decode(kelime,dict):
    for k in dict.values():
        if k in kelime:
            for c in dict.keys():
                if dict[c] == k:
                    kelime = kelime.replace(k,c)
    return kelime

def rec(socket):
    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        data = data.decode('utf-8')
        if isCodec:
            data = decode(data,codec)
        print(data,"\n->")
       # sys.stdout.write(data)
        if data == "exit":
            socket.close()
            os._exit(0)
        sys.stdout.write("->")

def send(socket):
    while True:
        message = input("->")
        if isCodec:
            message = encode(message,codec)

        UDPSock.sendto(bytes(message,'utf-8'),addrsend)


host = ""
buf = 1024
addr = (host, portRec)
addrsend = (ipSend, portSend)

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
UDPSock.bind(addr)


_thread.start_new_thread(rec,(UDPSock,))

send(UDPSock)


UDPSock.close()
os._exit(0)

