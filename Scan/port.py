import socket
import threading
import time
import pyfiglet

index = pyfiglet.figlet_format("SecuNet")
print(index)

def getPortBaner(ip , p):
    try:
        port=int(p)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if port == 3363 or port==22 or port==23 or port==1521:
                s.settimeout(5)
        else:
                s.settimeout(0.2)
                s.connect((ip,port))
                s.send("Hello\r\n")
    except Exception as e:
        #print(e)
        pass
    
    finally:
        s.close()

def GetPortsBanner(ip, ports):
        for p in ports:
              banner = GetPortsBanner(ip, str(p))

def CscanPortBanner(ip,ports): 
	if '/24' in ip:
		print 'ip/24: '+ip
		ipc = (ip.split('.')[:-1])
		for i in range(1,256):
			ip = ('.'.join(ipc)+'.'+str(i))
			threading._start_new_thread(GetPortsBanner,(ip,ports,))
			time.sleep(0.1)
	else:
		GetPortsBanner(ip,ports)
def BscanPortBanner(ip,ports): 
	if '/16' in ip:
		print 'ip/16: '+ip
		ipc = (ip.split('.')[:-2])
		for i in range(1,256):
			ip = ('.'.join(ipc)+'.'+str(i)+'.0/24')
			CscanPortBanner(ip,ports)
def AscanPortBanner(ip,ports): 
	if '/8' in ip:
		print 'ip/8: '+ip
		ipc = (ip.split('.')[:-3])
		for i in range(1,256):
			ip = ('.'.join(ipc)+'.'+str(i)+'.0/16')
			BscanPortBanner(ip,ports)