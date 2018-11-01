"""
Jack Shirley
624003478
CSCE 315-503
Due: September 10, 2018
project1.py
python2 code to query an NTP time server
Posted at https://stackoverflow.com/questions/12664295/ntp-client-in-python
"""

from contextlib import closing
from socket import socket, AF_INET, SOCK_DGRAM
from array import array
import sys
import struct
import time
import signal


#Lists are initialized
serverList = ["0.us.pool.ntp.org", "1.us.pool.ntp.org", "2.us.pool.ntp.org", "0.ubuntu.pool.ntp.org", 
"1.ubuntu.pool.ntp.org", "2.ubuntu.pool.ntp.org", "3.ubuntu.pool.ntp.org", "ntp.ubuntu.com", 
"time.apple.com", "time.windows.com", "time1.google.com", "time2.google.com", "time3.google.com", 
"time4.google.com", "ntp1.tamu.edu", "ntp2.tamu.edu", "ntp3.tamu.edu", "ops1.engr.tamu.edu", 
"ops2.engr.tamu.edu", "ops3.engr.tamu.edu", "ops4.engr.tamu.edu", "filer.cse.tamu.edu", 
"compute.cse.tamu.edu", "linux2.cse.tamu.edu", "dns1.cse.tamu.edu", "dns2.cse.tamu.edu", 
"dhcp1.cse.tamu.edu", "dhcp2.cse.tamu.edu"]
serverDifference = []
serverDiscrepency = []


NTP_PACKET_FORMAT = "!12I"
NTP_DELTA = 2208988800 # 1970-01-01 00:00:00
NTP_QUERY =  b'\x1b' + 47 * b'\0'  


#THIS FUNCTION WAS TAKEN FROM STACK OVERFLOW - CREDIT GOES TO AUTHOR "tomasz"
class Timeout():
    """Timeout class using ALARM signal."""
    class Timeout(Exception):
        pass
 
    def __init__(self, sec):
        self.sec = sec
 
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)
 
    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm
 
    def raise_timeout(self, *args):
        raise Timeout.Timeout()

    
#Function given in skeleton code that defines and retrieves data from servers
def ntp_time(host="", port=""):
	with closing(socket( AF_INET, SOCK_DGRAM)) as s:
		s.sendto(NTP_QUERY, (host, port))
		msg, address = s.recvfrom(1024)
	unpacked = struct.unpack(NTP_PACKET_FORMAT,
			msg[0:struct.calcsize(NTP_PACKET_FORMAT)])
	return unpacked[10] + float(unpacked[11]) / 2**32 - NTP_DELTA


#Main Function
if __name__ == "__main__":

    #Initialize Variables
    timeTotal = 0
    successCounter = 0

    for server in serverList:
        print(server)
        try:
            with Timeout(5):
                print(abs(ntp_time(server,123) - time.time()))
                if(abs(ntp_time(server,123) - time.time())) > 1:
                    print("Timeout")
                    serverDifference.append(0)
                else:
                    serverDifference.append(abs(ntp_time(server,123) - time.time()))
                    timeTotal += abs(ntp_time(server,123) - time.time())
                    successCounter += 1
                print("#########################")
                time.sleep(.1)
        except:
            print("Timeout")
            serverDifference.append(0)
            print("#########################")
        continue

    average = timeTotal / successCounter

    for difference in serverDifference:
        if difference != 0:
            serverDiscrepency.append(abs(difference - average))
        else:
             serverDiscrepency.append(0)

             
    print(serverList[serverDiscrepency.index(max(serverDiscrepency))], "has the greatest discrepancy at:", max(serverDiscrepency))

